# Plugin-Based Application Framework

A small, extensible plugin framework in Python demonstrating:
- plugin lifecycle (initialize, execute, shutdown)
- dynamic discovery and loading of plugins
- Observer/EventBus pattern for inter-plugin communication
- Singleton registry (PluginManager) and factory/load strategies

## Project Structure
```
plugin_framework/
├── main.py
├── core/
│ ├── app.py
│ ├── plugin_interface.py
│ ├── plugin_manager.py
│ └── event_bus.py
├── plugins/
│ ├── hello_plugin.py
│ └── metrics_plugin.py
├── utils/
│ ├── id_generator.py
│ └── logger.py
└── README.md
```


## Features & Patterns

- **Singleton**: `PluginManager` ensures a single registry for plugins.
- **Factory / Registry**: `PluginManager.load()` supports either `create_plugin()` factory or a `PluginImpl` class.
- **Observer**: `EventBus` for publish/subscribe messaging between app and plugins.
- **Modular**: Clear separation of core, plugins, and utilities.

## How to run

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/plugin_framework.git
cd plugin_framework
```
Run demo:
```
python main.py
```

Extending the framework

Drop new plugin modules into the plugins/ package that either expose:

create_plugin() factory returning a Plugin instance, or

a PluginImpl class inheriting from core.plugin_interface.Plugin.

Plugins receive app_context with useful objects:

```
{
  "event_bus": EventBus instance,
  "id_generator": IDGenerator
}
```

Example output

```
[App] Loaded plugin plugins.hello_plugin as 1a2b3c4d
[App] Loaded plugin plugins.metrics_plugin as 9f8e7d6c
[App] Running plugins...
[HelloPlugin] received greet event: {'message': 'Hello from HelloPlugin'}
[MetricsPlugin] {'runs': 1, 'uptime_seconds': 0}
[App] metrics event: {'runs': 1, 'uptime_seconds': 0}
[App] Run complete.
[HelloPlugin] shutdown complete
[MetricsPlugin] shutdown complete
[App] Shutdown complete.
```


```
## What I recommend you do next
- Copy these files into a new repo `plugin_framework` on GitHub.
- Add a `.replit` and `.devcontainer` if you want to enable one-click run and Codespaces support (I can generate those files for you).
- Add unit tests for the `PluginManager` and `EventBus` to demonstrate testable architecture.
- Add a third sample plugin that integrates with an external service (e.g., send metrics to a mock HTTP endpoint) to show real-world extensibility.
```

