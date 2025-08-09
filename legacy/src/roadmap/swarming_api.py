"""
Swarming API for Roadmap Collaboration
Implements endpoints for creating/joining swarms, tracking progress, and distributing Chrona rewards.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter()

swarms = {}

@router.post("/roadmap/swarms/create")
def create_swarm(swarm_id: str, quest: str, members: List[str]):
    if swarm_id in swarms:
        raise HTTPException(status_code=400, detail="Swarm already exists")
    swarms[swarm_id] = {"quest": quest, "members": members, "progress": 0, "rewards": {}}
    return swarms[swarm_id]

@router.post("/roadmap/swarms/join")
def join_swarm(swarm_id: str, user_id: str):
    if swarm_id not in swarms:
        raise HTTPException(status_code=404, detail="Swarm not found")
    swarms[swarm_id]["members"].append(user_id)
    return swarms[swarm_id]

@router.post("/roadmap/swarms/progress")
def update_progress(swarm_id: str, progress: int):
    if swarm_id not in swarms:
        raise HTTPException(status_code=404, detail="Swarm not found")
    swarms[swarm_id]["progress"] = progress
    return swarms[swarm_id]

@router.post("/roadmap/swarms/reward")
def distribute_rewards(swarm_id: str, rewards: Dict[str, float]):
    if swarm_id not in swarms:
        raise HTTPException(status_code=404, detail="Swarm not found")
    swarms[swarm_id]["rewards"] = rewards
    return swarms[swarm_id]
