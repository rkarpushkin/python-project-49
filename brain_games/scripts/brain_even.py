#!/usr/bin/env python3
# from .brain_games import main
from .cli import welcome_user
import prompt
import random


def ask_question(name):
    number = random.randint(0, 100)
    answer = prompt.string(f'Question: {number}\nYour answer: ')
    # print(answer.lower())    
    if number%2==0 and answer.lower()=='yes':
        print('Correct!')
        return True
    elif number%2==1 and answer.lower()=='no':
        print('Correct!')
        return True
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        return False
    

def main():
    # print("May I have your name?", end='')
    counter=3
    print('Welcome to the Brain Games!')
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