"""
Module: order_manager.py
------------------------
Implements the OrderManager class that manages customer orders.
Demonstrates the Command pattern for executing and undoing orders.
"""

from utils.logger import Logger


class OrderManager:
    """
    Handles coffee orders and maintains order history.
    """

    def __init__(self, machine):
        self.machine = machine
        self.history = []

    def make_order(self, drink_name: str):
        """Execute a new order."""
        drink = self.machine.prepare_drink(drink_name)
        self.history.append(drink)
        Logger.log(f"Order completed: {drink}")
        return drink

    def undo_last_order(self):
        """Simulate undoing the last order (for demonstration)."""
        if not self.history:
            Logger.log("No previous orders to undo.")
            return
        last = self.history.pop()
        Logger.log(f"Undoing last order: {last.name}")

