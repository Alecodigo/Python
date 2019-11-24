# -*- coding: utf-8 -*-

import math


def prime_number(num):
    
    if num == 2:
        print("2 is a prime number and part number too.")

    elif num > 2:
        x = [i for i in range(1,num + 1) if num % i == 0]
        if x[0] == 1 and x[1] == num:
            print("Congratulations this is a prime number")
        else:
            print("Sorry! this is not a prime number")
    else:
        print("Sorry! this is not a prime number")



def test(num):
        
    try:
        number = int(num)
        prime_number(number)
    except ValueError:
        print("Oops! please type a valid value =( \n")





if __name__ == "__main__":
    print("Welcome...\n")
    num = input("Type a number: ")
    test(num)
    print("Bye =)\n")


