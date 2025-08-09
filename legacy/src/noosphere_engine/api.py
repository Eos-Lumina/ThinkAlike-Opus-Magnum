"""
Noosphere Engine API: RESTful interface for knowledge operations
Purpose: Allow agents, realms, and modules to interact with the distributed ledger
"""

from fastapi import APIRouter, HTTPException
from .engine import NoosphereEngine

router = APIRouter()
engine = NoosphereEngine()

@router.post("/noosphere/add")
def add_entry(key: str, value: str, agent_id: str = None, realm: str = None):
    engine.add_entry(key, value, agent_id, realm)
    return {"status": "success", "key": key}

@router.get("/noosphere/query")
def query_entry(key: str):
    entry = engine.query(key)
    if entry:
        return entry
    raise HTTPException(status_code=404, detail="Entry not found")

@router.get("/noosphere/all")
def get_all_entries():
    return engine.get_all_entries()
