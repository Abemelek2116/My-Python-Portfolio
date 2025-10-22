"""
Module: recipe.py
-----------------
Defines the Recipe class that outlines ingredient requirements for a specific drink.
"""

class Recipe:
    """
    Represents a drink recipe composed of ingredient requirements.
    """

    def __init__(self, ingredients: dict):
        """
        Initialize a recipe with a mapping of ingredient names to quantities.

        :param ingredients: Dictionary of {ingredient_name: amount_required}
        """
        self.ingredients = ingredients

    def get_ingredients(self):
        """Return the ingredient requirements."""
        return self.ingredients

