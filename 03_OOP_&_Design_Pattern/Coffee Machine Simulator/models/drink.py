"""
Module: drink.py
----------------
Defines the Drink class representing a beverage produced by the coffee machine.
"""

class Drink:
    """
    Represents a drink with a name, price, and recipe requirements.
    """

    def __init__(self, name: str, price: float, recipe):
        """
        Initialize a drink.

        :param name: Name of the drink
        :param price: Selling price
        :param recipe: Recipe object specifying required ingredients
        """
        self.name = name
        self.price = price
        self.recipe = recipe

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

