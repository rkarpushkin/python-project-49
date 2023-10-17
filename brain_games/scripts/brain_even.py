#!/usr/bin/env python3
# from .brain_games import main
# from cli import welcome_user
import prompt
import random
# from .brain_games import games


def welcome_user():
    print('Welcome to the Brain Games!')
    # print("May I have your name?", end='')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(name):
    number = random.randint(0, 1000)
    answer = prompt.string(f'Question: {number}\nYour answer: ')
    # print(answer.lower())    
    if (number%2==0 and answer.lower()=='yes') or (number%2==1 and answer.lower()=='no'):
        print('Correct!')
        return True
    # elif number%2==1 and answer.lower()=='no':
    #     print('Correct!')
    #     return True
    elif answer=='yes':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        exit()
    elif answer=='no':
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        exit()
    else:
        print(f"{answer} is not a valid answer.\nLet's try again, {name}!")
        exit()
        # return False
    

def main():
    # print("May I have your name?", end='')
    counter=3
    name=welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter!=0:
        question_result = ask_question(name)
        if question_result==True:
            counter-=1
            # print(counter)
        if question_result==False:
            counter=3
            # print(counter)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()