class Recipe(object):
    ' Classe recette '
    def __init__(self):
        print("Creation de la recette ...\n")
        self.name = input("What is the name of the recipee ?\n>>")
        self.cooking_time = input(f"How long is it to cook {self.name} ?\n>>")
        self.cooking_lvl = input(f"How hard is it to cook {self.name} (difficulty from 1 to 5) ?\n>>")
        self.nbr_ingredients = input(f"How many ingredients does {self.name} have ?\n>>")
        self.ingredients = []
        for i in range(int(self.nbr_ingredients)):
            self.ingredients.append(input(f"What is the ingredient number {i + 1} of {self.name} ?\n>>"))
        self.description = input(f"Geave a short descrption of the recipee\n>>")
        self.recipe_type = input(f"What is the type of the recipee\n>>")

    def __str__(self):
        txt = "\n\n-Name : " + self.name + "\n-Cooking time (minutes) : " + self.cooking_time + "\n-Cooking lvl : " + self.cooking_lvl + " /5\n-List of ingredients : "
        for i in range(int(self.nbr_ingredients)):
            txt = txt + str(self.ingredients[i])
            if i != int(self.nbr_ingredients):
                txt = txt + ", "
        txt = txt + "\n-Description : " + self.description + "\n-Recipe type : " + self.recipe_type + "\n\n"
        return txt
