from random import seed
from random import randint


def main():
    number = randint(1, 99)
    play = 1
    attempts = 0
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
    while play:
        player_number = input("What's your guess between 1 and 99?\n\n")
        try:
            int(player_number)
            if int(player_number) == number:
                print(f"\nCongratulations, you've got it!\nYou won in {attempts} attempts !\n")
                play = 0
            elif int(player_number) > number:
                print("\nToo high!")
                attempts += 1
            elif int(player_number) < number:
                print("\nToo low!")
                attempts += 1
        except ValueError:
            if str(player_number) == "exit":
                print("\nGoodbye!")
                play = 0
            else :
                print("\nThat's not a number.")
        
if __name__ == '__main__':
    main()
