import os
import random
import time

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
    story = open(r'story.txt').read()
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
        elif i == 'c':
            break
        else:
            os.system('clear')

    if choose_class_list[29] == '*':
        charracter_status_list.append('Stupid Warrior')
    elif choose_class_list[57] == '*':
        charracter_status_list.append('Sparta!!!!')
    elif choose_class_list[85] == '*':
        charracter_status_list.append('Mage (not recomend)')
    print(''.join(charracter_status_list[0]) + ' Your class is: ' + ''.join(charracter_status_list[1]))

    return charracter_status_list


def charracter_status_dict(charracter_status_list):
    if charracter_status_list[1] == 'Stupid Warrior':
        stats_dict = {'str': 8, 'dex': 2, 'int': 0}
    if charracter_status_list[1] == 'Sparta!!!!':
        stats_dict = {'str': 9, 'dex': 9, 'int': 5}
    if charracter_status_list[1] == 'Mage (not recomend)':
        stats_dict = {'str': 1, 'dex': 4, 'int': 9}

    return stats_dict


def stats_disp(stats_dict):
    for i in stats_dict:
        stats = (str(stats_dict[i]) + ': ' + str(i))
        print(stats)
    return stats


def how_to_play_screen():
    os.system('clear')
    path = 'howtoplay.txt'
    file_name = open(path, "r")
    howto = []
    for howto_row in file_name:
        for i in howto_row:
            howto.append(i)
    return howto


def dragon():
    os.system('clear')
    path = 'dragon.txt'
    file_name = open(path, "r")
    drag = []
    for drag_row in file_name:
        for i in drag_row:
            drag.append(i)
    return drag


def win_screen():
    path = 'win.txt'
    file_name = open(path, "r")
    map_1_list = []
    for map_1_row in file_name:
        for i in map_1_row:
            map_1_list.append(i)
    return map_1_list


def lose_screen():
    path = 'Lose.txt'
    file_name = open(path, "r")
    lose = []
    for lose_row in file_name:
        for i in lose_row:
            lose.append(i)
    return lose


def map_1():
    path = 'map1.txt'
    file_name = open(path, "r")
    map_1_list = []
    for map_1_row in file_name:
        for i in map_1_row:
            map_1_list.append(i)
    return map_1_list


def map_2():
    os.system('clear')
    path = 'map2.txt'
    file_name = open(path, "r")
    map_1_list = []
    for map_1_row in file_name:
        for i in map_1_row:
            map_1_list.append(i)
    return map_1_list


def monster(stats_dict, monster_helth):

    attack_power = stats_dict['str']
    print("monster HP: " + str(monster_helth))
    while monster_helth >= 0:
        i = getch()
        if i == 'e':
            monster_helth -= attack_power
            print("monster HP: " + str(monster_helth))
    print("die")




def move(map_1_list, stats_dict, charracter_status_list, points, drag, lose):

    start_position = 73
    left_right = 1
    up_down = 71
    monster_helth = 20
    while True:
        print(''.join(map_1_list))
        stats_disp(stats_dict)
        print(''.join(charracter_status_list[0]) + ' Your class is: ' + ''.join(charracter_status_list[1]))
#first map
        if map_1_list[649] == '@' and map_1_list[720] == '2':
            print('Monster!!! Press "e" to attack')
            monster(stats_dict, monster_helth)
            points_add(points)
            map_1_list[720] = '.'
        elif map_1_list[269] == '@' and map_1_list[198] == '4':
            print('Monster!!! Press "e" to attack')
            monster(stats_dict, monster_helth)
            points_add(points)
            map_1_list[198] = '.'
        elif map_1_list[96] == '@' and map_1_list[95] == '1':
            print('Monster!!! Press "e" to attack')
            monster(stats_dict,  monster_helth)
            points_add(points)
            map_1_list[95] = '.'
        elif map_1_list[685] == '@' and map_1_list[684] == '3':
            print('Mini Boss')
            display_game()
            points_add(points)
            input("well done! Press any key to continue")
            map_1_list[684] = '.'
            if map_1_list[684] == '.':
                break
#second map
        if map_1_list[713] == '@' and map_1_list[712] == '5':
            print('Monster!!! Press "e" to attack')
            monster(stats_dict, monster_helth)
            points_add(points)
            map_1_list[712] = '.'
        if map_1_list[108] == '@' and map_1_list[109] == '6':
            print('Monster!!! Press "e" to attack')
            monster(stats_dict, monster_helth)
            points_add(points)
            map_1_list[109] = '.'
        if map_1_list[694] == '@' and map_1_list[765] == '7':
            print('Monster!!! Press "e" to attack')
            monster(stats_dict,  monster_helth)
            points_add(points)
            print('WTF??? o_O')
            map_1_list[765] = '.'
            input("Good Job. I have something for You if You want kill BOSS\n Just answer correctly!!\n PRESS ENTER TO START")
            check_answer(lose, points)
            os.system('clear')
            input('Now You have to play in cold, hot, warm game\n PRESS ENTER TO START')
            final_quest(drag, lose, points)
            break


#move
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




# Level_1 - Guess the number


def display_game():

    user_name = input('What is your name ?')
    print('Hello ' + user_name)
    print('Well, ' + user_name + ' if you want to go out alive you have to guess the number between 1-50')

    random_number = random.randint(1, 50)

    while True:
        user_number = int(input('What is your guess? '))

        if random_number == user_number:
            break

        elif random_number < user_number:
            print('{}{}'.format(user_number, ' is too high'))

        else:
            print('{}{}'.format(user_number, ' is too low!'))

    print ('Yes ' + str(user_number) + ' is my secret number! Congratulations.')

#display_game()

# Level_2 - Answer the questions

file_name = r'/home/sebastian/Dokumenty/The_worst_knight/question_answer.txt'


def display_question(file_name):
    question_file = open(file_name, 'r')
    question_list = []

    for line in question_file:
        question_list.append(line)
    # print(''.join(question_list))
    return question_list


def questions(points):
    answer_list = []
    question_list = display_question(file_name)

    for element in range(len(question_list)):
        os.system('clear')
        print(question_list[element])
        answer = input('My answer is: ')

        if answer == 'yes' or answer == 'Yes' or answer == 'YES':
            print('That is wrong answer')

        elif answer == 'no' or answer == 'No' or answer == 'NO':
            points_add(points)
            print('Yes, you right !')

        elif answer != 'yes' or answer != 'Yes' or answer != 'YES':
            print('That is wrong answer')

        elif answer != 'no' or answer != 'No' or answer != 'NO':
            print('That is wrong answer')

        answer_list.append(answer)

    return answer_list


def check_answer(lose, points):
    point = 0
    answer_list = questions(points)

    for element in answer_list:

        if element == 'no' or element == 'No' or element == 'NO':
            point += 1
        else:
            os.system('clear')
            print(''.join(lose))
            input('Press Enter to exit')
            exit()
            break

    print('You have: ' + str(point) + ' point(s)')

#check_answer()


# Level_3

def get_random_number():
    number_list = []
    while len(number_list) < 3:
        digit = random.randint(0, 9)
        if digit not in number_list:
            number_list.append(digit)

    return number_list


def get_user_input():
    while True:

        user_guess = input("Enter the number: ")

        if user_guess.isalpha():
            print("Enter only digits")

        elif len(user_guess) != 3:
            print("Input hasnt 3 digits")

        else:
            return list(user_guess)


def compare_user_input_witth_answer(user_guess, correct_answer, drag):
    index = 0
    hint_list = []

    for a in correct_answer:
        if str(a) == user_guess[index]:
            hint_list.insert(0, "HOT")

        elif str(a) in user_guess:
            hint_list.append("WORM")
        index += 1
        os.system('clear')
        print(''.join(drag))
    if not hint_list:
        hint_list.append("cold")
        os.system('clear')
        print(''.join(drag))
    return hint_list


def check_result(hint_list, points):
    if hint_list == ["HOT"] * 3:
        points_add(points)
        return True


def points_add(points):
    points.append(1)
    return points

# Level_3
def final_quest(drag, lose, points):
    correct_answer = get_random_number()
    print(''.join(drag))
    tries_left = 10
    while tries_left > 0:
        user_guess = get_user_input()
        result = compare_user_input_witth_answer(user_guess, correct_answer, drag)
        print(result)
        if check_result(result, points):
            print("WIN")
            break
        tries_left -= 1
    if tries_left == 0:
        os.system('clear')
        print(''.join(lose))
        print('Pres Enter to exit')
        exit()

# start_time = time.time() wstawimy na początek
# game_time = int(time.time() - start_time) wstawimy na koniec


def main():
    start_time = time.time()
    lose = lose_screen()
    drag = dragon()
    points = []
    user_name = input("Enter your name: ")
    howto = how_to_play_screen()
    print(''.join(howto))
    input("Enter to continue")
    welcome_story(user_name)
    charracter_status_list = character_creation(user_name)
    stats_dict = charracter_status_dict(charracter_status_list)
    stats_disp(stats_dict)
    map_1_list = map_1()
    print('press "C" to start')
    i = getch()
    if i == 'c':
        os.system('clear')
        move(map_1_list, stats_dict, charracter_status_list, points, drag, lose)

    map_1_list = map_2()
    move(map_1_list, stats_dict, charracter_status_list, points, drag, lose)
    game_time = int(time.time() - start_time)
    input('Enter to continue')
    print('Your points = ' + str(len(points)))
    print('Your time = ' + str(game_time))
    score = (int(len(points)) * 100) / int(game_time)
    print('Your score = ' + str(score))
    input()


main()
