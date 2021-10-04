import os

NATS_SERVER: str = os.environ.get('NATS_SERVER')
JWT_TOKEN_ALGORITHM: str = 'HS256'
JWT_SECRET_KEY: str = os.environ.get('JWT_SECRET_KEY')
NATS_REQUEST_TIMEOUT: int = 30
