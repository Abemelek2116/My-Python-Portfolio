"""
plugin_interface.py
-------------------
Defines the base Plugin interface that all plugins should implement.
This enforces a contract for lifecycle methods (initialize, execute, shutdown)
and metadata (name, version).
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class Plugin(ABC):
    """
    Abstract base class for plugins.
    Plugins must implement initialize, execute, and shutdown methods.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable plugin name."""
        pass

    @property
    def version(self) -> str:
        """Plugin version (defaults to '0.1'). Override if needed."""
        return "0.1"

    @abstractmethod
    def initialize(self, app_context: Dict[str, Any]) -> None:
        """
        Initialize plugin with app context.
        :param app_context: Shared resources provided by the host application.
        """
        pass

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """
        Execute the plugin's primary functionality.
        Return value is plugin-specific.
        """
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Perform cleanup before the plugin is unloaded or app exits."""
        pass

