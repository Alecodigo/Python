# -*- coding: utf-8 -*-
#! python3

import sys
import os
import random
import pprint

STUDENTS = [
            'Alejandro',
            'Jose',
            'Yajaira',
            'Enrique',
            'Joel',
            'Joselin',
            'Esteban',
            'Angel']

stateCapitals = {
            'Amazonas':'Puerto Ayacucho',
            'Anzoategui':'Barcelona',
            'Apure': 'San Fernando de Apure',
            'Aragua': 'Maracay',
            'Barinas': 'Barinas',
            'Bolivar': 'Ciudad Bolivar',
            'Carabobo': 'Valencia',
            'Cojedes': 'San Carlos',
            'Delta Amacuro':'Tucupita',
            'Distrito Capital':'Caracas',
            'Falcon':'Coro',
            'Guarico':'San Juan de los Morros',
            'Lara':'Barquisimeto',
            'Merida':'Merida',
            'Miranda':'Los Teques',
            'Monagas':'Maturin',
            'Nueva Esparta':'La Asuncion',
            'Portuguesa':'Guanare',
            'Sucre':'Cumana',
            'Tachira':'San Cristobal',
            'Trujillo':'Trujillo',
            'La Guaira':'La Guaira',
            'Yaracuy':'San Felipe',
            'Zulia':'Maracaibo',}


def makeTest():

    for student in STUDENTS:
        pathFile = os.path.join(os.getcwd(), 'exam', student + '.txt')
        #print('LLego al for')
        print(pathFile)
        stud = open(pathFile, 'w')
        # Creo el Encabezado
        stud.write(('Unidad Educativa de Python\nFecha:\nAlumno: ' + student + '\n\n') + (' ' * 40) + 'Test\n\n\n\n\n\n\n')
        stud.close()


def makeQuestions():
    path = os.path.join(os.path.join(os.getcwd(), 'exam'))
    print(path)
    archivos = os.listdir(path)
    if archivos:
        # Tomo las claves del diccionario y creo una lista
        keys = list(stateCapitals.keys()) 
    
        for item in archivos:
            ruta = os.path.join(path, item)
            print(ruta)
            exam = open(ruta, 'a')
            # print(exam)
            i = random.randrange(len(keys))
            exam.write('¿Indique cual es la capital de estado ' + keys[i] + '?\n\n\n')
            i = random.randrange(len(keys))
            exam.write('¿Indique cual es la capital de estado ' + keys[i] + '?\n\n\n')
            i = random.randrange(len(keys))
            exam.write('¿Indique cual es la capital de estado ' + keys[i] + '?\n\n\n')
            i = random.randrange(len(keys))
            exam.write('¿Indique cual es la capital de estado ' + keys[i] + '?\n\n\n')
            i = random.randrange(len(keys))
            exam.write('¿Indique cual es la capital de estado ' + keys[i] + '?\n\n\n')
            exam.close()





if __name__ == '__main__':

    print('llego al if')
    # Necesito crear una carpeta para guardar los examenes
    if os.path.isdir('exam'):
        print("Ya existe el directorio exam")
    else:
        os.makedirs(os.path.join(os.getcwd(), 'exam'))

    stateCapitals = {
            'Amazonas':'Puerto Ayacucho', 
            'Anzoategui':'Barcelona', 
            'Apure': 'San Fernando de Apure',
            'Aragua': 'Maracay',
            'Barinas': 'Barinas',
            'Bolivar': 'Ciudad Bolivar',
            'Carabobo': 'Valencia',
            'Cojedes': 'San Carlos',
            'Delta Amacuro':'Tucupita',
            'Distrito Capital':'Caracas',
            'Falcon':'Coro',
            'Guarico':'San Juan de los Morros',
            'Lara':'Barquisimeto',
            'Merida':'Merida',
            'Miranda':'Los Teques',
            'Monagas':'Maturin',
            'Nueva Esparta':'La Asuncion',
            'Portuguesa':'Guanare',
            'Sucre':'Cumana',
            'Tachira':'San Cristobal',
            'Trujillo':'Trujillo',
            'La Guaira':'La Guaira',
            'Yaracuy':'San Felipe',
            'Zulia':'Maracaibo',}
    #pprint.pprint(stateCapitals)
    #print(stateCapitals)

    # Empezamos a contruir los archivos
    makeTest()
    makeQuestions()
