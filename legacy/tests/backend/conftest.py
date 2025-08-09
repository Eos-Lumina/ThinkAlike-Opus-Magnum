import logging

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def client(monkeypatch):
    """
    This fixture uses monkeypatching to ensure the FastAPI app uses
    a test database.

    It replaces the production `engine` and `SessionLocal` in the
    `db.session` module *before* the application is imported.
    This ensures that all parts of the app, including dependencies,
    use the test database from the very beginning.
    """
    logger.info("Setting up client fixture with monkeypatch...")

    # 1. Set up a completely separate test database engine and session factory
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    test_engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )

    # 2. Monkeypatch the session module *before* importing the app
    from src.backend.app.db import session as db_session_module

    monkeypatch.setattr(db_session_module, "engine", test_engine)
    monkeypatch.setattr(db_session_module, "SessionLocal", TestingSessionLocal)
    logger.info("Monkeypatched db.session.engine and db.session.SessionLocal")

    # 3. Now that patching is complete, import the app and its dependencies
    from src.backend.app.db.base_class import Base
    from src.backend.app.main import app

    # 4. Create all tables in the test database
    logger.info(
        "METADATA TABLES BEFORE CREATE: %s",
        list(Base.metadata.tables.keys()),
    )
    Base.metadata.create_all(bind=test_engine)
    logger.info("Tables created on test engine.")

    # Verify tables are created using an inspector
    inspector = inspect(test_engine)
    tables = inspector.get_table_names()
    logger.info(
        f"Tables found by inspector: {tables}",
    )
    assert "users" in tables  # Add assertion for clarity

    # 5. Yield the configured TestClient
    with TestClient(app) as c:
        yield c

    # 6. Teardown: drop all tables.
    #    Monkeypatch is reverted automatically by pytest.
    Base.metadata.drop_all(bind=test_engine)
    logger.info("Client fixture torn down.")


@pytest.fixture(scope="function")
def db():
    """
    Provides a direct, isolated database session for tests.

    Allows tests to interact with the database layer without
    going through the API.
    """
    # 1. Set up a completely separate test database engine
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    # 2. Import app dependencies
    from src.backend.app.db.base_class import Base

    # 3. Create the tables in the test database
    Base.metadata.create_all(bind=engine)

    # 4. Yield a session
    db_session = TestingSessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

    # 5. Teardown
    Base.metadata.drop_all(bind=engine)
