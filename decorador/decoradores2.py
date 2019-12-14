# -*- coding: utf-8 -*-

# se pude resumir A(B) ---> C


def hello_language(func):
    def wrapper():
        print('In english I say you:')
        func()
    return wrapper


@hello_language
def hello():
    print('Hello world')


if __name__ == '__main__':
    print('Decorators')
    hello()






