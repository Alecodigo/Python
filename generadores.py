# -*- coding: utf-8 -*-



def generador(n, m, s):
    while(n <= m):
        yield n
        n += s

for n in generador(0, 5, 1):
    print(n)

