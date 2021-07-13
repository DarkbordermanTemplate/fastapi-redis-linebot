import json
from typing import Any, Union

from config import Config
from loguru import logger
from redis import StrictRedis

REDIS: StrictRedis = StrictRedis.from_url(Config.REDIS_URL)


class CacheBase:
    prefix: str = ""

    @classmethod
    def get(cls, key: str, jsonify=False) -> Union[Any, None]:
        """
            Get data from Redis
            (Currently) Format of Redis key is <idenify prefix> + _ + <key>

        Args:
            key (str): key string of data
            jsonify (bool, optional): The data is jsonify(dumps/loads) or not. Defaults to False

        Returns:
            Union[Any, None]: Any data, return None if cache not hit
        """
        logger.info(f"Redis get {cls.prefix}_{key}")
        cache = REDIS.get(f"{cls.prefix}_{key}")
        if cache:
            if jsonify:
                return json.loads(cache.decode())
            return cache.decode()
        return None

    @classmethod
    def set(cls, key: str, value: Any, jsonify=False, ex: int = None) -> None:
        """
            Set data to Redis
            (Currently) Format of Redis key is <idenify prefix> + _ + <key>

        Args:
            key (str): key string of data
            value (Any): data to be stored in Redis
            ex (int, optional): data expire time in second. Default to None(no expire)
            jsonify (bool, optional): The data is jsonify(dumps/loads) or not. Defaults to False

        Returns:
            None
        """
        logger.info(f"Redis set {cls.prefix}_{key} to {value}")
        if jsonify:
            REDIS.set(f"{cls.prefix}_{key}", json.dumps(value), ex=ex)
        else:
            REDIS.set(f"{cls.prefix}_{key}", value, ex=ex)

    @classmethod
    def delete(cls, key: str) -> None:
        """Remove data from Redis

        Args:
            key (str): key string of data
        """
        logger.info(f"Redis delete {cls.prefix}_{key}")
        REDIS.delete(f"{cls.prefix}_{key}")


# pylint: disable=W0221
class CacheUser(CacheBase):
    """
    Cache used to store session of users, use user ID as reference key
    """

    prefix = "line"

    @classmethod
    def get(cls, key: str) -> Union[dict, None]:
        return super().get(key, jsonify=True)

    @classmethod
    def set(cls, key: str, value: dict) -> None:
        return super().set(key, value, jsonify=True)


def init_cache():
    pass
