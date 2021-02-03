from recipe import Recipe
from datetime import date

class Book(object):
    "Classe de cookbook"
    def __init__(self):
        self.name = str(input("What is the name of the cookbook ?\n"))
        self.last_update = date.today()
        self.creation_date = date.today()
        self.recipes_list = {
                "starter" : [],
                "lunch" : [],
                "dessert" : [],
                }
    def get_recipe_by_name(self, name):
        print(str(self.name))
        return name
    def get_recipes_by_types(self, name):
        print(self.recipes_list[self.name])
        pass
    def add_recipe(self, name):
        self.name = Recipe()
        self.recipes_list[self.name.recipe_type].append(self.name)
        self.last_update = date.today()
        pass

