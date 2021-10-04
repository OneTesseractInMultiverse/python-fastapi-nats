from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api_endpoints import (
    message,
    item
)


# -----------------------------------------------------------------------------
# Instance of FastAPI Application
# -----------------------------------------------------------------------------
app = FastAPI(
    title="FastAPI + NATS Example Microservice",
    description="This is a template project that uses NATS to generate events",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url=None
)


# -----------------------------------------------------------------------------
# CORS RULES
# -----------------------------------------------------------------------------
origins = [
    "*"
]

# Default configuration is to ALLOW ALL from EVERYWHERE. You might want to
# restrict this.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(message.router, prefix="/api/v1")
app.include_router(item.router, prefix="/api/v1")
