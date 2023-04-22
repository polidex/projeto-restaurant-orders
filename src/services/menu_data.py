import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_data(source_path)

    def load_data(self, source_path):
        csv = pd.read_csv(source_path)
        self.dishes = {Dish(dish, price) for dish, price in csv[
            ['dish', 'price']].values}
        for dish, ingredient, recipe_amount in csv[
            ['dish', 'ingredient', 'recipe_amount']
                ].values:
            dish = next((d for d in self.dishes if d.name == dish), None)
            if dish is not None:
                dish.add_ingredient_dependency(
                    Ingredient(ingredient), recipe_amount)
            else:
                raise ValueError(f'Dish "{dish}" not found.')
