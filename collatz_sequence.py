#-*- coding:utf-8 -*-
# collatz sequence

import sys


def collatz(number):
    result = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
             number = 3 * number + 1
        print(number)


if __name__ == '__main__':
    print("Welcome to the program.")
    numb = 0
    try:
        numb = int(input("Enter a number: "))
    except ValueError:
        print("You can only enter a numbers.")
    
    collatz(numb)

