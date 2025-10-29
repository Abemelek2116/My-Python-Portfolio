"""
main.py
-------
Demo of the Plugin-Based Application Framework.
Discovers plugins under the `plugins` package, loads them, runs them,
and then shuts down cleanly.
"""

from core.app import App

def main():
    app = App()
    try:
        app.discover_and_load("plugins")
        # Optionally: subscribe a quick listener for metrics events
        app.event_bus.subscribe("metrics", lambda payload: print(f"[App] metrics event: {payload}"))
        app.run()
    finally:
        app.shutdown()

if __name__ == "__main__":
    main()
