import pytest
from cache import REDIS


def init_cache():
    pass


@pytest.fixture(autouse=True)
def preinit():
    """
    Pytest decorator to run preprcessing proceduce before each test case
    ex: init database and cache
    """
    REDIS.flushdb()
    init_cache()
