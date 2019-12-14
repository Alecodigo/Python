# -*- coding: utf-8 -*-
#!/bin/python3


class  Calculator:


    def __init__(self):
        self.display_hello()
        #self.num = a


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

        print(self.IMAGES[0])


    def rest(self):
        number = 0
        result = 0
        while True:
            number = int(input(":"))
            if result == 0:
                result = number
            else:
                result -= number
                return result


    def suma(self):
        number = 0
        result = 0
        while True:
            number = int(input(":"))
            if result == 0:
                result = number
            else:
                result += number
                return result

    def dividir(self):
        number = 0
        result = 0
        while True:
            number = int(input(":"))
            if result == 0:
                result = number
            else:
                result /= number
                return result
     
   
    def multi(self):
        number = 0
        result = 0
        while True:
            number = int(input(":"))
            if result == 0:
                result = number
            else:
                result *= number
                return result




def display_result(result):
    print("\n")
    print(result)


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
            resta = calculator.rest()
            display_result(resta)
        elif command == 's':
            suma = calculator.suma()
            display_result(suma)
        elif command == 'd':
            division = calculator.dividir()
            display_result(division)
        elif command == 'm':
            multi = calculator.multi()
            display_result(multi)
        else:
            break




if __name__ == '__main__':


    print("Hello, Welcome to Your Calculator Software")
    actions()


