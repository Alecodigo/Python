# -*- coding:utf-8 -*-



def validate_input():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            print('Thanks')
            break
        print('Please enter a number for your age.')







if __name__ == '__main__':
    validate_input()
