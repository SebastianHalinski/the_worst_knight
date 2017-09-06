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

def welcome_story(user_name):
    os.system("clear")
    print("Hello", user_name)
    story = open(r'/home/sebastian/Dokumenty/The_worst_knight/story.txt').read()
    print(story)
    start = input("Would you like to start the game? y or n")
    if start == "y":
        pass
    elif start == "n":
        print("You will die anyway")
    else:
        welcome_story(user_name)

def character_creation(user_name):
    charracter_status_list = []
    print(user_name + 'Now choose Your profession')
    charracter_status_list.append(user_name)
    os.system('clear')
    path = r'/home/sebastian/Dokumenty/The_worst_knight/choose_class.txt'
    file_name = open(path, "r")
    choose_class_list = []
    for row in file_name:
        for i in row:
            choose_class_list.append(i)

    start_position = 29
    up_down = 28
    while True:
        print("".join(choose_class_list))
        i = getch()
        if i == 'w' and choose_class_list[start_position - up_down] == '_':
            os.system('clear')
            choose_class_list[start_position - up_down] = '*'
            choose_class_list[start_position] = '_'
            start_position -= up_down
        elif i == 's' and choose_class_list[start_position + up_down] == '_':
            os.system('clear')
            choose_class_list[start_position + up_down] = '*'
            choose_class_list[start_position] = '_'
            start_position += up_down
        elif i == 'q':
            break
        else:
            os.system('clear')

    if choose_class_list[29] == '*':
        charracter_status_list.append('Stupid Warrior')
    elif choose_class_list[57] == '*':
        charracter_status_list.append('Sparta!!!!')
    elif choose_class_list[85] == '*':
        charracter_status_list.append('Mage (not recomend)')
    print(' '.join(charracter_status_list))


    if charracter_status_list[1] == 'Stupid Warrior':
        stats_dict = {'str': 8, 'dex': 2, 'int': 0}
    if charracter_status_list[1] == 'Sparta!!!!':
        stats_dict = {'str': 9, 'dex': 9, 'int': 5}
    if charracter_status_list[1] == 'Mage (not recomend)':
        stats_dict = {'str': 1, 'dex': 4, 'int': 9}
    print(stats_dict)

    return stats_dict, charracter_status_list


def hud_display(status_dict, charracter_status_list):
    
    pass


def map_1():
    path = r'/home/sebastian/Dokumenty/The_worst_knight/map1.txt'
    file_name = open(path, "r")
    map_1_list = []
    for map_1_row in file_name:
        for i in map_1_row:
            map_1_list.append(i)
    return map_1_list


def map_2():
    os.system('clear')
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


def main():
    user_name = input("Enter your name: ")
    welcome_story(user_name)
    character_creation(user_name)
    map_1_list = map_1()
    print('press C to start')
    if getch() == 'c':
        os.system('clear')
        move(map_1_list)
    map_1_list = map_2()
    move(map_1_list)


main()
