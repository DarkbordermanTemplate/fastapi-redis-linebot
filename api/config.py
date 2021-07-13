import os


class Config:
    """Service configurations"""

    APP_TITLE = os.environ.get("APP_TITLE", "FastAPI template")
    APP_DESCRIPTION = os.environ.get("APP_DESCRIPTION", "A template for FastAPI.")
    VERSION = os.environ.get("VERSION", "0.0.0")
    OPENAPI_URL = os.environ.get("OPENAPI_URL", "/openapi.json")
    # Cache configuration
    REDIS_URL = os.environ.get("REDIS_URL", "redis://:password@localhost:6379/0")
    LINE_TOKEN = os.environ.get("LINE_TOKEN", "")
