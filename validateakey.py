# -*- coding: utf-8 -*-

import sys


PASSWORD = ''


def create_password():
    global PASSWORD
    pwd = input("Enter your new password: ")
    confir_pwd = input("Confirm you password: ")
    if pwd == confir_pwd:
        print("Success")
        PASSWORD = confir_pwd
    else:
        print("Error in password try again.")


def change_password():
    global PASSWORD
    if PASSWORD:
        current_pwd = input("Enter current password: ")

        if PASSWORD == current_pwd:
            new_passwd = input("Enter a new password: ")
            PASSWORD = new_passwd
            print(PASSWORD)
        
        else:
            print("Current password is not valid.")
    else:
        print("You don't have any password set.")

def menu():
    password = input(""" Configuration Menu
                
                Press [1] to create a new password
                Press [2] to change password
                Press [Q] to exit  
            """)
    return password


if __name__ == '__main__':
    # Menu

    while True:
        password = menu()
        if password.isdecimal():
            if password == '1':
                create_password()
            elif password == '2':
                change_password()
        elif password == 'Q':
            break
        else:
            print("Enter only numbers")
            #sys.exit()
            #break
    print("\n")
    print("Thanks for use our services.")

            
