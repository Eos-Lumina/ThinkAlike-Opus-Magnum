from sqlalchemy import inspect


def test_tables_created(db):
    """Tests that the database tables are being created by the fixture."""
    inspector = inspect(db.bind)
    tables = inspector.get_table_names()
    assert "users" in tables
    assert "profiles" in tables
    assert "items" in tables
