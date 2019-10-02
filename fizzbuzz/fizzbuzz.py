""" 
 (    (       )   )               )   )   (   (       )        (              *     
 )\ ) )\ ) ( /(( /(   (        ( /(( /(   )\ ))\ ) ( /( (      )\ )   (     (  `    
(()/((()/( )\())\())( )\    (  )\())\()) (()/(()/( )\()))\ )  (()/(   )\    )\))(   
 /(_))/(_)|(_)((_)\ )((_)   )\((_)((_)\   /(_))(_)|(_)\(()/(   /(_)|(((_)( ((_)()\  
(_))_(_))  _((_)((_|(_)_ _ ((_)_((_)((_) (_))(_))   ((_)/(_))_(_))  )\ _ )\(_()((_) 
| |_ |_ _||_  /_  / | _ ) | | |_  /_  /  | _ \ _ \ / _ (_)) __| _ \ (_)_\(_)  \/  | 
| __| | |  / / / /  | _ \ |_| |/ / / /   |  _/   /| (_) || (_ |   /  / _ \ | |\/| | 
|_|  |___|/___/___| |___/\___//___/___|  |_| |_|_\ \___/  \___|_|_\ /_/ \_\|_|  |_| 
                                                                                    
"""

# LIMIT = 100

def fizzbuzz():
    LIMIT = 100
    """FizzBuzz function """
    while(LIMIT >= 0):
        if LIMIT % 3 == 0 and LIMIT % 5 == 0:
            print("FIZZBUZZ")
            LIMIT -= 1
            continue
        elif LIMIT % 3 == 0:
            print("FIZZ")
            LIMIT -= 1
            continue
        elif LIMIT % 5 == 0:
            print("BUZZ")
            LIMIT -= 1
            continue
        else:
            print(LIMIT)
            LIMIT -= 1



if __name__ == '__main__':
    fizzbuzz()

    #Las lineas de abajo son necesarias si corremos el programa como ejecutable
    print "\n\n"
    var = raw_input('Press enter to exit')