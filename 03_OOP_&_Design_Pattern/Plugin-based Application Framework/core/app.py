"""
app.py
------
Host application that wires components together and provides a simple API
to manage plugins and dispatch events.
"""

from core.plugin_manager import PluginManager
from core.event_bus import EventBus
from utils.logger import Logger


class App:
    """
    Central application class. This is what an embedding application would use.
    """

    def __init__(self):
        # Event bus shared across plugins
        self.event_bus = EventBus()
        # Plugin manager is a singleton but we pass our event bus for cohesion
        self.plugin_manager = PluginManager(event_bus=self.event_bus)
        # attach a basic logger subscriber
        Logger.subscribe(self._log_consumer)

    def _log_consumer(self, message: str):
        """Consume log messages from utils.logger and forward to event bus (optional)."""
        # For demo, just print; advanced systems might route to a file or telemetry
        print(f"[App Log] {message}")

    def discover_and_load(self, package: str = "plugins") -> None:
        """Discover plugin modules in a package and load them."""
        module_paths = self.plugin_manager.discover(package)
        for mp in module_paths:
            try:
                pid = self.plugin_manager.load(mp)
                print(f"[App] Loaded plugin {mp} as {pid}")
            except Exception as exc:
                print(f"[App] Failed to load {mp}: {exc}")

    def run(self) -> None:
        """Run main application loop. For demo, execute all plugins once."""
        print("[App] Running plugins...")
        self.plugin_manager.execute_all()
        print("[App] Run complete.")

    def shutdown(self) -> None:
        """Shutdown all plugins cleanly."""
        for pid in list(self.plugin_manager.get_plugins().keys()):
            self.plugin_manager.unload(pid)
        print("[App] Shutdown complete.")

