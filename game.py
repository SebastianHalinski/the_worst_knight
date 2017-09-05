import random
import time


def welcome_story(user_name):
    print ("Hello", user_name)
    story = open(r"C:\Users\Marta\Documents\codecool\python\game_knight\the_worst_knight\story.txt").read()
    print(story)

    start = input("Would you like to start the game? y or n")

    if start == "y":
        first_level()
    elif start == "n":
        print ("You will die anyway")
    else:
        welcome_story(user_name)

    
def display_game():

    print("Hello Knight!")
    print("Well, " + user_name + " if you want to go out alive you have to guess the number between 1-50")

    random_number = random.randint(1, 50)

    while True:
        user_number = int(input("What is your guess? "))
        if random_number == user_number:
            break
        elif random_number < user_number:
            print("{}{}".format(user_number, " is too high"))
        else:
            print("{}{}".format(user_number, " is too low!"))

    print ("Yes " + str(user_number) + " is my secret number! Congratulations.")

display_game()



def main():
    user_name = input("Enter your name: ")
    welcome_story(user_name)
    start_time = time.time()
    points = 0

main()