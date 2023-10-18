from brain_games.scripts.brain_games import welcome
import random
import prompt


def check_answer(number1, number2, answer):
    min = int()
    gcd = 0
    if number1-number2 > 0:
        min = number2
        max = number1
    else:
        min = number1
        max = number2

    denominators = list()

    for i in range(1,min+1):
        if min%i == 0:
            denominators.append(i)

    for i in denominators:
        if max%i==0:
            gcd = i
    
    if gcd == answer:
        # print('wrong!')
        return 0
    else:
        print(gcd)
        return gcd



def ask_question(name):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    # function_list = {{sqrt: '*'}, {sum: '+'}, {dis: '-'}}
    # functions_list = ['-', '+', '*']
    # function = random.choice(functions_list)
    answer = prompt.string(f'Question: {number1} {number2}\nYour answer: ')

    try:
        int(answer)
        pass
    except:
        print(f"{answer} is not integer. Let's try again")
        answer = prompt.string(f'Question: {number1} {number2}\nYour answer: ')

    results=check_answer(number1, number2, int(answer))
    # print(f'Result is {results}')
    # print(f'Name is {name}')
    if results != 0:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{results}'.\nLet's try again, {name}!")
        exit()
    else:
        print('Correct!')
        return True


def main():
    counter=3
    name=welcome()
    print('Find the greatest common divisor of given numbers.')
    while counter!=0:
        # print(name)
        question_result = ask_question(name)
        if question_result:
            counter-=1
            # print(counter)ß
        if not question_result:
            counter=3
            # print(counter)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
