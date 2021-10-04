from app.messaging.nats_messaging_client import NATSMessagingClient
from app.logging.syslog_impl import StandardOutputLogger
import logging


async def get_messaging_middleware() -> NATSMessagingClient:
    return NATSMessagingClient(logger=StandardOutputLogger())
