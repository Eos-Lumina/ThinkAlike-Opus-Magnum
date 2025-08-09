"""
Noosphere Engine: Distributed Knowledge Ledger for ThinkAlike
Purpose: Centralized, auditable, and extensible knowledge system for agents, realms, and protocols.
"""

from typing import Dict, Any, Optional
import threading

class NoosphereEngine:
    def __init__(self):
        self.ledger: Dict[str, Dict[str, Any]] = {}
        self.lock = threading.Lock()

    def add_entry(self, key: str, value: Any, agent_id: Optional[str] = None, realm: Optional[str] = None):
        with self.lock:
            self.ledger[key] = {
                "value": value,
                "agent_id": agent_id,
                "realm": realm
            }

    def query(self, key: str) -> Optional[Dict[str, Any]]:
        with self.lock:
            return self.ledger.get(key)

    def update_entry(self, key: str, value: Any):
        with self.lock:
            if key in self.ledger:
                self.ledger[key]["value"] = value

    def get_all_entries(self):
        with self.lock:
            return self.ledger.copy()

    # Future: Add distributed storage, audit trail, and API integration
