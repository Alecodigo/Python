# -*- coding: utf-8 -*-

def funcion_1():
    def funcion_2():
        print "Soy la funcion 2"
    
    print("finalizando la funcion 1")
    return funcion_2


funcion_1()
input("Press enter for output")