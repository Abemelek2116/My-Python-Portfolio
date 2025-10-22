"""
Main Script: Coffee Machine Simulator
-------------------------------------
Entry point demonstrating coffee machine operation using
OOP principles and multiple design patterns.
"""

from services.coffee_machine import CoffeeMachine
from services.order_manager import OrderManager
from utils.logger import Logger, ConsoleLogger
from utils.file_handler import export_orders_to_csv


def main():
    """Run the Coffee Machine simulation."""
    Logger.subscribe(ConsoleLogger())

    machine = CoffeeMachine.get_instance()
    manager = OrderManager(machine)

    # Display machine status
    machine.display_status()

    # Place some orders
    manager.make_order("espresso")
    manager.make_order("latte")
    manager.make_order("cappuccino")

    # Undo last order (Command pattern)
    manager.undo_last_order()

    # Export orders to CSV
    export_orders_to_csv(manager.history)
    Logger.log("Order history exported to orders.csv")

    # Final resource status
    machine.display_status()


if __name__ == "__main__":
    main()

