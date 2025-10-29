"""
metrics_plugin.py
-----------------
A sample plugin that collects basic metrics when executed and exposes them
via the plugin execute() return value or by publishing an event.
"""

from core.plugin_interface import Plugin
from typing import Dict, Any
import time


def create_plugin():
    """
    Alternate plugin factory function. Demonstrates the load() path that
    uses a create_plugin() callable instead of a PluginImpl class.
    """
    return MetricsPlugin()


class MetricsPlugin(Plugin):
    def __init__(self):
        self._counters = {"runs": 0}
        self._start = None

    @property
    def name(self) -> str:
        return "MetricsPlugin"

    def initialize(self, app_context: Dict[str, Any]) -> None:
        self.app_context = app_context
        self._start = time.time()

    def execute(self, *args, **kwargs) -> None:
        self._counters["runs"] += 1
        uptime = time.time() - self._start
        summary = {"runs": self._counters["runs"], "uptime_seconds": int(uptime)}
        # publish metrics on event bus for other consumers
        event_bus = self.app_context.get("event_bus")
        if event_bus:
            event_bus.publish("metrics", summary)
        # print for demo visibility
        print(f"[MetricsPlugin] {summary}")

    def shutdown(self) -> None:
        print("[MetricsPlugin] shutdown complete")

