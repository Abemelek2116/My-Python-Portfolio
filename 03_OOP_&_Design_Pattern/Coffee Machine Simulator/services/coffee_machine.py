"""
Module: coffee_machine.py
-------------------------
Implements the CoffeeMachine class that manages ingredients, recipes,
and drink preparation. Demonstrates the Singleton and Factory patterns.
"""

from models.drink import Drink
from models.recipe import Recipe
from models.ingredient import Ingredient
from utils.id_generator import generate_id
from utils.logger import Logger


class CoffeeMachine:
    """
    Singleton class representing the coffee machine.
    """

    __instance = None

    @staticmethod
    def get_instance():
        """Return the single CoffeeMachine instance."""
        if CoffeeMachine.__instance is None:
            CoffeeMachine()
        return CoffeeMachine.__instance

    def __init__(self):
        if CoffeeMachine.__instance is not None:
            raise Exception("CoffeeMachine is a Singleton. Use get_instance().")

        # Initialize machine resources
        self.ingredients = {
            "water": Ingredient("Water", 2000, "ml"),
            "milk": Ingredient("Milk", 1000, "ml"),
            "coffee": Ingredient("Coffee Beans", 500, "g"),
            "sugar": Ingredient("Sugar", 300, "g"),
        }

        # Initialize recipes (Factory concept)
        self.menu = {
            "espresso": Drink("Espresso", 2.5, Recipe({"water": 50, "coffee": 18})),
            "latte": Drink("Latte", 3.5, Recipe({"water": 100, "milk": 150, "coffee": 24, "sugar": 10})),
            "cappuccino": Drink("Cappuccino", 3.8, Recipe({"water": 120, "milk": 120, "coffee": 20})),
        }

        CoffeeMachine.__instance = self

    def prepare_drink(self, drink_name: str):
        """
        Prepare a drink if ingredients are available.

        :param drink_name: Name of the drink
        :return: Drink object
        """
        if drink_name not in self.menu:
            raise ValueError(f"{drink_name} is not on the menu.")

        drink = self.menu[drink_name]
        for ingredient, amount in drink.recipe.get_ingredients().items():
            self.ingredients[ingredient].use(amount)

        Logger.log(f"Prepared {drink.name} for ${drink.price:.2f}.")
        return drink

    def refill(self, ingredient_name: str, amount: float):
        """Refill a specific ingredient."""
        if ingredient_name not in self.ingredients:
            raise ValueError("Unknown ingredient.")
        self.ingredients[ingredient_name].refill(amount)
        Logger.log(f"Refilled {ingredient_name} by {amount} units.")

    def display_status(self):
        """Display the current resource levels."""
        print("\n=== Machine Resources ===")
        for ing in self.ingredients.values():
            print(f" - {ing}")

