"""
logger.py
---------
Tiny publish-style logger that other components can subscribe to.
This is intentionally simple; in production you'd use structlog/logging.
"""

from typing import Callable, List


class Logger:
    _subscribers: List[Callable[[str], None]] = []

    @classmethod
    def subscribe(cls, handler: Callable[[str], None]) -> None:
        cls._subscribers.append(handler)

    @classmethod
    def log(cls, message: str) -> None:
        for h in list(cls._subscribers):
            try:
                h(message)
            except Exception:
                # swallow subscriber exceptions to keep logging robust
                pass

