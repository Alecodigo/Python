# -*- coding: utf-8 -*-
#!/bin/python3


class  Calculator:

    def __init__(self, a):
        self.display_hello()
        self.num = a


    def display_hello(self):

        self.IMAGES = ['''
         _____________________
        |  _________________  |
        | |    HELLO!! =)   | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | + | |
        | |___|___|___| |___| |
        | | 4 | 5 | 6 | | - | |
        | |___|___|___| |___| |
        | | 1 | 2 | 3 | | x | |
        | |___|___|___| |___| |
        | | . | 0 | = | | / | |
        | |___|___|___| |___| |
        |_____________________|

        ''',
        ]   
    
    def rest(self):
        




def actions():
    calculator = Calculator()
    
    while True:
        #Menu
        command = input("""Select one actions in the menu
                
                [r]estar ----->  press r
                [s]umar  ----->  press s
                [d]ividir ---->  press d
                [m]ultiplicar -> press m
                [A]ny to exit

                """)
        if command == 'r':
            calculator.rest()
        elif command == 's':
            calculator.suma()
        elif command == 'd':
            calculator.dividir()
        elif command == 'm':
            calculator.multi()
        else:
            break




if __name__ == '__main__':


    print("Hello, Welcome to Your Calculator Software")
    calculator


