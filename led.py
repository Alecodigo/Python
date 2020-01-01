# -*- coding: utf-8 -*-


""" Turn off and Turn on a led when you put a binary code in the prompt """



class Led:
    """Led Class."""

    LED = [

        """   
          

              \      |      /
               .    .     .
                \        /
                   ____
           - . -  |    | - . - 
                 _|    |_ 
                |________|
                   |  |
                   | 


        """,

        """           
 

          ____
         |    |
        _|    |_
       |________|
          |  |
          | 
        

 

        """,

        ]


    def __init__(self):
        self.led_initial()


    def led_initial(self):
        print("Turn on / off a LED\n")

    def on(self):
        """Turn on the led."""
        print(self.LED[0])


    def off(self):
        """Turn off the led."""
        print(self.LED[1])




def main():
    """Run the program."""

    led = Led()

    while True:

        menu = input("""
            Please select 1 or 0
                [1] Turn on
                [0] Turn off
                [q] to exit\n\n
            """)

        if menu == '1':
            print("\n")
            led.on()
        if menu == '0':
            print("\n")
            led.off()
        if menu == 'q':
            print("\n Bye Bye ;)\n")   
            break
        else:
            print("\n Please enter a correct value")


if __name__ == '__main__':
    main()







