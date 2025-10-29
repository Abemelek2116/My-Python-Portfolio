"""
event_bus.py
------------
A simple publish/subscribe event bus implementing the Observer pattern.
Plugins can subscribe to events by name, and the application or other plugins
can publish events with payloads.
"""

from typing import Callable, Dict, List, Any


class EventBus:
    """
    Lightweight event bus.
    Maintains mapping of event name -> list of subscriber callables.
    """

    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Any], None]]] = {}

    def subscribe(self, event_name: str, handler: Callable[[Any], None]) -> None:
        """Subscribe a handler to a named event."""
        self._subscribers.setdefault(event_name, []).append(handler)

    def unsubscribe(self, event_name: str, handler: Callable[[Any], None]) -> None:
        """Unsubscribe a handler from a named event."""
        handlers = self._subscribers.get(event_name, [])
        if handler in handlers:
            handlers.remove(handler)

    def publish(self, event_name: str, payload: Any = None) -> None:
        """Publish an event to all subscribers (synchronous delivery)."""
        for handler in list(self._subscribers.get(event_name, [])):
            try:
                handler(payload)
            except Exception as exc:
                # avoid breaking other handlers; host app or a logger should manage errors
                print(f"[EventBus] handler error for '{event_name}': {exc}")

