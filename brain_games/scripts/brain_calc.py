from brain_games.scripts.brain_games import welcome
import random
import prompt


def check_answer(number1, number2, function, answer):
    if function == '+' and number1 + number2 == answer:
        return True
    elif function == '+':
        result = number1 + number2
        return result

    if function == '-' and number1 - number2 == answer:
        return True
    elif function == '-':
        result = number1 - number2

    if function == '*' and number1 * number2 == answer:
        return True
    elif function == '*':
        result = number1 * number2
    return result


def ask_question(name):
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    # function_list = {{sqrt: '*'}, {sum: '+'}, {dis: '-'}}
    functions_list = ['-', '+', '*']
    function = random.choice(functions_list)
    answer = prompt.string(f'Question: {number1} {function} {number2}\
                           \nYour answer: ')

    try:
        int(answer)
        pass
    except:
        print(f"{answer} is not integer. Let's try again")
        answer = prompt.string(f'Question: {number1} {function} {number2}\
                               \nYour answer: ')

    results = check_answer(number1, number2, function, int(answer))
    # print(f'Result is {results}')
    # print(f'Name is {name}')
    if not results:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{results}'.\
              \nLet's try again, {name}!")
        exit()
    else:
        print('Correct!')
        return True


def main():
    counter = 3
    name = welcome()
    print('What is the result of the expression?')
    while counter != 0:
        # print(name)
        question_result = ask_question(name)
        if question_result:
            counter -= 1
            # print(counter)ß
        if not question_result:
            counter = 3
            # print(counter)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
