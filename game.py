def welcome_story (user_name):
    print ("Hello", user_name)
    story=open(r"C:\Users\Marta\Documents\codecool\python\game_knight\the_worst_knight\story.txt").read()
    print(story)
    start = input ("Would you like to start the game? y or n")
    if start == "y":
        first_level()
    elif start == "n":
        print ("You will die anyway")
    else:
        welcome_story(user_name)
    

def first_level():
    width = 70
    height = 15
    board = []
    element_full = []
    for i in range(width):
        element_full.append("X")
    element_blanks = []

    element_blanks.append("X")
    for i in range(width - 2):
        element_blanks.append(" ")
    element_blanks.append("X")
    board.append(element_full)

    for i in range(height - 2):
        board.append(element_blanks)
    board.append(element_full)

    for n in board:
       print(''.join(n))
    pass

def main ():
    user_name = input ("Enter your name: ")
    welcome_story(user_name)

main ()