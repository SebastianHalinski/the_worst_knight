file_name = r'/home/katarzyna/the_worst_knight/question_answer.txt'


def display_question(file_name):  
    question_file = open(file_name, 'r')
    question_list = []

    for line in question_file:
        question_list.append(line)
    # print(''.join(question_list))
    return question_list


def questions():
    answer_list = []
    question_list = display_question(file_name)

    for element in range(len(question_list)):
        print(question_list[element])
        answer = input('My answer is: ')
        #print(answer)   
        if answer == 'yes' or answer == 'Yes' or answer == 'YES':
            print('That is wrong answer')

        elif answer == 'no' or answer == 'No' or answer == 'NO':
            print('Yes, you right !')

        elif answer != 'yes' or answer != 'Yes' or answer != 'YES':
            print('That is wrong answer')

        elif answer != 'no' or answer != 'No' or answer != 'NO':
            print('That is wrong answer')
        
        answer_list.append(answer)
    # print(answer_list)
    return answer_list


def check_answer():
    points = 0
    answer_list = questions()

    for element in answer_list:

        if element == 'no' or element == 'No' or element == 'NO':
            points += 1
        else:
            print('You lose !')
            break

    print('You have: ' + str(points) + ' point(s)')

check_answer()    
    

def main():



main()    