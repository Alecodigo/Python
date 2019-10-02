


class  Calculator:
    
    def __init__(self):
        self.welcome_message = False
        self.num = 0
        self.operator = ''
        self.result = 0
        self.div_mult = 1
        
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
        # Result           
        '''
         _____________________
        |  _________________  |
        | |        {}       | |
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


    def aritmetic(self, value, operator):
        if operator == '-':
            self.result -= value
            return
        if operator == '+':
            self.result += value
            return
        if operator == '*':
            self.div_mult *= value
            self.result = self.div_mult
            return
        if operator == '/':
            self.div_mult /= value
            self.result = self.div_mult
            return

    def display(self):
        if self.welcome_message == False:
            print self.IMAGES[0]
            self.welcome_message = True

        while True:
            print("\n\n")
            self.num = raw_input("Please enter a numeric value")
            self.operator = raw_input("Select +,-,/,* ")

            if self.num.isdigit():
                self.aritmetic(int(self.num), self.operator)
                print self.IMAGES[1].format(self.result)
            else:
                print("Please enter just a numeric value")
        
        
            


if __name__ == '__main__':

    cal = Calculator()

    print("Hello, Welcome to Your Calculator Software")

    cal.display()
    

    #Las lineas de abajo son necesarias si corremos el programa como ejecutable
    print "\n\n"
    var = raw_input('Press enter to exit')




    # def aritmetic(self, value, operator):
    #     if operator == '-':
    #         self.result -= value
    #         return
    #     if operator == '+':
    #         self.result += value
    #         return
    #     if operator == '*':
    #         self.multi(value)
    #         return
    #     if operator == '/':
    #         self.div(value)
    #         return

    # def display(self):
    #     if self.welcome_message == False:
    #         print self.IMAGES[0]
    #         self.welcome_message = True

    #     while True:
    #         print("\n\n")
    #         self.num = raw_input("Please enter a numeric value")
    #         self.operator = raw_input("Select +,-,/,* ")

    #         if self.num.isdigit():
    #             self.aritmetic(int(self.num), self.operator)
    #             print self.IMAGES[1].format(self.result)
    #         else:
    #             print("Please enter just a numeric value")
