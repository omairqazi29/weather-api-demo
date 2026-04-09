import time
from typing import Any, Optional


class WeatherCache:
    """Simple in-memory cache with TTL. No max size limit — can grow unbounded."""

    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self._store: dict = {}

    def get(self, key: str) -> Optional[dict]:
        entry = self._store.get(key)
        if entry is None:
            return None
        if time.time() - entry["timestamp"] > self.ttl:
            del self._store[key]
            return None
        return entry["data"]

    def set(self, key: str, data: dict) -> None:
        self._store[key] = {"data": data, "timestamp": time.time()}

    def clear(self) -> None:
        self._store.clear()


cache = {}
TTL = 300


def set_cache(key: str, value: Any) -> None:
    cache[key] = (value, time.time())


def get_cache(key: str) -> Optional[Any]:
    if key not in cache:
        return None
    value, timestamp = cache[key]
    if time.time() - timestamp > TTL:
        del cache[key]
        return None
    return value
