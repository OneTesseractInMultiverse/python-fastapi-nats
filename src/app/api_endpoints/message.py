from fastapi import APIRouter, Depends
from app.schemas.message import Message
from app.messaging import get_messaging_middleware as messaging_middleware
from app.messaging.nats_messaging_client import NATSMessagingClient
router = APIRouter()


# -----------------------------------------------------------------------------
# POST MESSAGE
# -----------------------------------------------------------------------------
@router.post('/message', tags=['Message'])
async def broadcast_message(
        message: Message,
        messaging: NATSMessagingClient = Depends(messaging_middleware)
):
    await messaging.broadcast_message(
        message=message.body,
        subject=message.subject
    )
    return message.body


# -----------------------------------------------------------------------------
# POST MESSAGE
# -----------------------------------------------------------------------------
@router.post('/message-response', tags=['Message'])
async def request_message_with_response(
        message: Message,
        messaging: NATSMessagingClient = Depends(messaging_middleware)
):
    return await messaging.submit_message_with_response(
        message=message.body,
        subject=message.subject
    )
