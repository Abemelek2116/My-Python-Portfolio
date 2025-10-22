"""
Module: ingredient.py
---------------------
Defines the Ingredient class representing raw materials used
in drink recipes for the coffee machine.
"""

class Ingredient:
    """
    Represents a single ingredient (e.g., water, milk, coffee beans).
    """

    def __init__(self, name: str, quantity: float, unit: str):
        """
        Initialize an ingredient with its name, available quantity, and unit.

        :param name: Ingredient name
        :param quantity: Quantity available
        :param unit: Unit of measurement (e.g., ml, g)
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def use(self, amount: float) -> None:
        """
        Consume a specific amount of this ingredient.

        :param amount: Quantity to use
        :raises ValueError: If insufficient quantity
        """
        if amount > self.quantity:
            raise ValueError(f"Not enough {self.name} available.")
        self.quantity -= amount

    def refill(self, amount: float) -> None:
        """Add more of this ingredient."""
        self.quantity += amount

    def __str__(self):
        """Readable representation of the ingredient."""
        return f"{self.name}: {self.quantity:.1f}{self.unit}"

