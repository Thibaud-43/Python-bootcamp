import sys

cookbook = {
            'sandwich' : [["ham", "bread", "cheese", "tomatoes"], "lunch", 10],
            'cake' : [["floor", "sugar", "egss"], "dessert", 60],
            'salad' : [["avocado", "arugula", "tomatoes", "spinach"], "lunch", 15],
            }

def print_recipe(recipe):
    print(f"\n\nRecipe for a {recipe}:\nIngredients list : {cookbook[recipe][0]}\nTo be eaten for : {cookbook[recipe][1]}.\nTakes {cookbook[recipe][2]} minutes of cooking\n")

def delete_recipe(recipe):
    del cookbook[recipe]

def add_recipe(recipe, ingredients, meal, prep_time):
    cookbook[recipe] = [ingredients, meal, prep_time]

def selection_addRecipe():
    ingredients = []
    recipe = input("Which recipe do you want to add : \n")
    nbr_ingredients = input(f"How much ingredients have {recipe}?\n")
    for i in range(int(nbr_ingredients)):
        ingredients.append(input(f"Which is the ingredient number {i + 1} of {recipe}:\n"))
    prep_time = input(f"How long is it to cook {recipe} (in minutes) :\n")
    meal = input(f"For what meal do you it {recipe} :\n")
    add_recipe(recipe, ingredients, meal, prep_time)

def selection_deleteRecipe():
    recipe = input("Which recipe do you want to delete : \n")
    delete_recipe(recipe)

def selection_printRecipe():
    recipe = input("Which recipe do you want to print : \n")
    print_recipe(recipe)

def selection_printCookbook():
    for recipe in cookbook:
        print_recipe(recipe)

def main():
    switch = {
            1 : selection_addRecipe,
            2 : selection_deleteRecipe,
            3 : selection_printRecipe,
            4 : selection_printCookbook,
            5 : sys.exit,
            }
    while 1:
        usr = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
        if int(usr) > 5:
            print("This option does not exist, please type the corresponding number.")
        else :
            switch[int(usr)]()


if __name__ == '__main__':
    main()


