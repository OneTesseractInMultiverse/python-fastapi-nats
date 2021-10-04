import json
from app.settings import NATS_SERVER
from app.logging import AbstractLogger
from nats.aio.client import Client as NATSClient
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers


class NATSMessagingClient:

    # -------------------------------------------------------------------------
    # CLASS CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self, logger: AbstractLogger):
        """
        Create instances of NATSMessagingClient

        **WARNING** this class is not Thread Safe.
        If multiple threads are used, each thread needs to have
        its own instance of this class.

        :param logger: Injected through dependency inversion. Implementation of
                       the logger to be used by this class.
        """
        self._nats_client = NATSClient()
        self._connected = False
        self._logger = logger
        self._response = None

    # -------------------------------------------------------------------------
    # PROPERTY CONNECTED
    # -------------------------------------------------------------------------
    @property
    def connected(self) -> bool:
        """
        If there is an active connection with NATS server this will return True
        :return:
        """
        return self._connected

    # -----------------------------------------------------------------------------
    # BROADCAST WITH LOOP
    # -----------------------------------------------------------------------------
    async def _broadcast_message(self, message: dict, subject: str) -> bool:
        """
        Submits a message to be broadcast without expecting a response
        from any event subscriber. This is a  basic building block of NATS
        messaging so it has been extracted to protected function so it
        can be reused by classes that extend this class.

        :param message: the message to be sent
        :param subject: the subject to where the message is going to be
               published.
        :return: True if the message was sent
        """
        try:
            self._connected = await self._connect()
            await self._nats_client.publish(
                subject,
                json.dumps(message).encode()
            )
            await self._nats_client.close()
            self._connected = False
            return True
        except ErrTimeout as et:
            self._logger.error(message=str(et))
        except ErrConnectionClosed as ecc:
            self._logger.error(message=str(ecc))
        except Exception as ex:
            self._logger.error(message=str(ex))
        return False

    # -----------------------------------------------------------------------------
    # REQUEST
    # -----------------------------------------------------------------------------
    async def submit_message_with_response(self, message: dict,
                                           subject: str) -> dict or None:
        """
        Submits a message that requires a response from the subscriber.

        :param message: JSON serializable dictionary.
        :param subject: Subject in which the message will be published.
        :return: Response dictionary or None
        """

        try:
            self._connected = await self._connect()
            response = await self._nats_client.request(
                subject,
                json.dumps(message).encode(),
                timeout=5
            )
            # Read message before connection to NATS closes
            response_data = json.loads(response.data.decode())
            return response_data
        except ErrTimeout as et:
            self._logger.error(message=str(et))
        except ErrConnectionClosed as ecc:
            self._logger.error(message=str(ecc))
        except Exception as ex:
            self._logger.error(message=str(ex))
        finally:
            await self._nats_client.close()
            self._connected = False

    # -----------------------------------------------------------------------------
    # BROADCAST MESSAGE
    # -----------------------------------------------------------------------------
    async def broadcast_message(self, message: dict, subject: str):
        """
        Send a message to a given subject and do not expect any response.
        :param message:
        :param subject:
        :return:
        """
        await self._broadcast_message(
            message=message,
            subject=subject
        )

    # -------------------------------------------------------------------------
    # METHOD CONNECT
    # -------------------------------------------------------------------------
    async def _connect(self) -> bool:
        """
        Creates a connection to a given set of NATS server.

        :return: True if connection was successful. False if
                 connection was not successful
        """
        try:
            await self._nats_client.connect(
                servers=[NATS_SERVER]
            )
            return True
        except ErrNoServers as ens:
            self._logger.error(message=str(ens))
        except Exception as e:
            self._logger.error(message=str(e))
