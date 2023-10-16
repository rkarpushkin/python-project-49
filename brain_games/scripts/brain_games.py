#!/usr/bin/env python3
import prompt
from .cli import welcome_user

def main():
    # print("May I have your name?", end='')
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
