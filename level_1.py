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
