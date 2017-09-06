import os

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch



def map_1():
    path = r'/home/sebastian/Dokumenty/The_worst_knight/map1.txt'
    file_name = open(path, "r")
    map_1_list = []
    for map_1_row in file_name:
        for i in map_1_row:
            map_1_list.append(i)
    return map_1_list


def map_2():
    path = r'/home/sebastian/Dokumenty/The_worst_knight/map2.txt'
    file_name = open(path, "r")
    map_1_list = []
    for map_1_row in file_name:
        for i in map_1_row:
            map_1_list.append(i)
    return map_1_list


def move(map_1_list):
    start_position = 73
    left_right = 1
    up_down = 71

    while True:
        print(''.join(map_1_list))
        i = getch()

        if i == "a" and map_1_list[start_position - left_right] == '.':
            os.system('clear')
            map_1_list[start_position - left_right] = '@'
            map_1_list[start_position] = "."
            start_position -= left_right
        elif i == "d" and map_1_list[start_position + left_right] == '.':
            os.system('clear')
            map_1_list[start_position + left_right] = '@'
            map_1_list[start_position] = "."
            start_position += left_right
        elif i == "w" and map_1_list[start_position - up_down] == '.':
            os.system('clear')
            map_1_list[start_position - up_down] = '@'
            map_1_list[start_position] = "."
            start_position -= up_down
        elif i == "s" and map_1_list[start_position + up_down] == '.':
            os.system('clear')
            map_1_list[start_position + up_down] = '@'
            map_1_list[start_position] = "."
            start_position += up_down
        elif i == "q":
            break
        else:
            os.system('clear')




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



def main():
    user_name = input ("Enter your name: ")
    welcome_story(user_name)
    map_1_list = map_1()
    print('press C to start')
    if getch() == 'c':
        os.system('clear')
        move(map_1_list)
    map_1_list = map_2()
    move(map_1_list)

main()


    
