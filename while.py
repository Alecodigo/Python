# -*- coding: utf-8 -*-


def cuenta_regresiva():
    x = 10
    despegue = False
    while despegue == False:
        print(x)
        x -= 1
        if x == 0:
            despegue = True
            print("Despegue!!")


if __name__ == '__main__':
    print("Cuenta regresiva")
    cuenta_regresiva()
