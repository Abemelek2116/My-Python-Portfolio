"""
hello_plugin.py
---------------
A trivial example plugin that demonstrates lifecycle and event subscription.
"""

from core.plugin_interface import Plugin
from typing import Dict, Any


class PluginImpl(Plugin):
    @property
    def name(self) -> str:
        return "HelloPlugin"

    def initialize(self, app_context: Dict[str, Any]) -> None:
        self.app_context = app_context
        # subscribe to a custom event
        event_bus = app_context.get("event_bus")
        if event_bus:
            event_bus.subscribe("greet", self._on_greet)

    def execute(self, *args, **kwargs) -> None:
        # simple execution: publish a greet event
        event_bus = self.app_context.get("event_bus")
        if event_bus:
            event_bus.publish("greet", {"message": "Hello from HelloPlugin"})

    def _on_greet(self, payload):
        # handler for greet event
        print(f"[HelloPlugin] received greet event: {payload}")

    def shutdown(self) -> None:
        # clean-up if necessary
        event_bus = self.app_context.get("event_bus")
        if event_bus:
            event_bus.unsubscribe("greet", self._on_greet)
        print("[HelloPlugin] shutdown complete")

