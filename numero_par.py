# -*- coding: utf-8 -*-


def if_part(num):
    """This function say if we have a 
    part number."""
    
    if num % 2 == 0:
        return True
    else:
        return False



def check_number(number):
    """This function check a number."""

    try:
        num = int(number)
        result = if_part(num)
        return result
    except ValueError:
        return False




if __name__=='__main__':
    print("Do you want to know if a number is part?\n")
    number = input(("Enter a number: "))
    result = check_number(number)
    
    if result is True:
        print("Congratulations this number" + " " + number + " " + "is part")
    else:
        print("Sorry this is not a even number.")
    


