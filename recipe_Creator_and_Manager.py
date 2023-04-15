class Recipe:
    def __init__(self, name, category, ingredients):
        self.name = name
        self.category = category
        self.ingredients = ingredients


class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, category, ingredients):
        recipe = Recipe(name, category, ingredients)
        self.recipes.append(recipe)

    def print_all(self):
        for recipe in self.recipes:
            print(recipe.name)

    def print_category(self, category):
        for recipe in self.recipes:
            if recipe.category == category:
                print(recipe.name)

    def print_contains_ingredient(self, ingredient):
        for recipe in self.recipes:
            if ingredient in recipe.ingredients:
                print(recipe.name)

