"""
plugin_manager.py
-----------------
Responsible for discovering, loading, registering and managing plugin lifecycle.
Implements the Singleton pattern to ensure a single plugin registry.
Supports dynamic loading by module path (simple factory/registry approach).
"""

import importlib
import pkgutil
import types
from typing import Dict, List, Any, Type
from utils.id_generator import IDGenerator
from core.plugin_interface import Plugin
from core.event_bus import EventBus


class PluginManagerMeta(type):
    """Metaclass to enforce a Singleton PluginManager."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PluginManager(metaclass=PluginManagerMeta):
    """
    Manages plugin lifecycle: discovery, load, initialize, execute, shutdown.
    Plugins are stored in a registry keyed by unique plugin_id.
    """

    def __init__(self, event_bus: EventBus = None):
        self._registry: Dict[str, Plugin] = {}
        self._modules: Dict[str, types.ModuleType] = {}
        self.event_bus = event_bus or EventBus()
        # application-level context passed to plugins
        self.app_context: Dict[str, Any] = {"event_bus": self.event_bus, "id_generator": IDGenerator}

    def discover(self, package: str) -> List[str]:
        """
        Discover plugin module names inside a package (e.g., 'plugins').
        Returns list of full module paths.
        """
        discovered = []
        package_mod = importlib.import_module(package)
        for finder, name, ispkg in pkgutil.iter_modules(package_mod.__path__, package_mod.__name__ + "."):
            discovered.append(name)
        return discovered

    def load(self, module_path: str) -> str:
        """
        Dynamically import a plugin module and instantiate its `Plugin` subclass.
        Expects the module to expose a `create_plugin()` factory function OR a
        subclass of Plugin named `PluginImpl`.
        Returns the assigned plugin_id.
        """
        mod = importlib.import_module(module_path)
        self._modules[module_path] = mod

        # Strategy 1: module exposes create_plugin()
        if hasattr(mod, "create_plugin") and callable(getattr(mod, "create_plugin")):
            plugin_obj = mod.create_plugin()
        # Strategy 2: module exposes PluginImpl subclass
        else:
            cls = getattr(mod, "PluginImpl", None)
            if cls and issubclass(cls, Plugin):
                plugin_obj = cls()
            else:
                raise ImportError(f"Module {module_path} does not provide a plugin factory or PluginImpl class")

        # Assign a stable unique ID, register and initialize plugin
        plugin_id = IDGenerator.generate_id()
        self._registry[plugin_id] = plugin_obj
        plugin_obj.initialize(self.app_context)
        return plugin_id

    def unload(self, plugin_id: str) -> None:
        """Shutdown and remove plugin by plugin_id."""
        plugin = self._registry.get(plugin_id)
        if not plugin:
            return
        try:
            plugin.shutdown()
        finally:
            del self._registry[plugin_id]

    def execute_all(self, *args, **kwargs) -> None:
        """Execute all registered plugins. Plugins decide what execute() does."""
        for pid, plugin in list(self._registry.items()):
            try:
                plugin.execute(*args, **kwargs)
            except Exception as exc:
                print(f"[PluginManager] error executing plugin {pid}: {exc}")

    def get_plugins(self) -> Dict[str, Plugin]:
        """Return current registry snapshot."""
        return dict(self._registry)

