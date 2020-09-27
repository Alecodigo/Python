# -*- coding:utf-8 -*-

PASSWORD = '123456*'


def proof_id(passwd):
    if passwd:
        if PASSWORD == passwd:
            return True
    else:
        return False
    




if __name__ == '__main__':
    print("Welcome Enter Your Secret Password")
    passwd = input("password: ")
    print(passwd)
    if passwd:
        result = proof_id(passwd)
        if result:
            print("Access granted")
        else:
            print("Access Denied")
        
