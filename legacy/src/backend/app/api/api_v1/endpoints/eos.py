from fastapi import APIRouter, WebSocket, Depends, Body
from ....agents.eos_lumina.core import eos_core, AgentContext

router = APIRouter(prefix="/eos")

async def get_user_context(session_id: str, user_id: str):
    return AgentContext(session_id=session_id, user_id=user_id)

@router.post("/events/system")
async def system_event(event_type: str = Body(...), context=Depends(get_user_context)):
    context = await eos_core.handle_event(event_type, context)
    return {"response": context.response}

@router.websocket("/ws/{session_id}/{user_id}")
async def ws_endpoint(ws: WebSocket, session_id: str, user_id: str):
    await ws.accept()
    ctx = AgentContext(session_id, user_id)
    while True:
        data = await ws.receive_json()
        ctx.last_input = data.get("payload")
        ctx = await eos_core.handle_event(data.get("type"), ctx)
        await ws.send_json(ctx.response)
