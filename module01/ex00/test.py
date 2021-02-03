from recipe import Recipe
from book import Book 

def main():
    book = Book()
    book.add_recipe("cake")
    book.get_recipes_by_types("dessert")
    book.get_recipe_by_name("cake")

if __name__ == '__main__':
    main()
