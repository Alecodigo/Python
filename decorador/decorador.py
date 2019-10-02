# -*- coding: utf-8 -*-


def protected(func):

    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


@protected
def protected_func():
    print('Tu contraseña es correcta.')
    


if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))

    protected_func(password)

    # @protected equivale a:
    # wrapper = protected(protected_func)
    # wrapper(password)

    #las lineas de abajo son para que no se cierre el command line de python
    print "\n\n\n\n"
    var = raw_input("presione enter para salir")