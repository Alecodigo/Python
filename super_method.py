# -*- coding: utf-8 -*-




class Perro:
    def __init__(self, ladrar):
        self.ladra = ladrar 
        self.juega = "Persigue la pelota"
        

    def ladrar(self):
        print(self.ladra)


    def jugar(self):
        print(self.juega)


    def _mover_cola(self):
        vals = {'cola': 'Moviendo cola'}
        return vals



class PastorAleman(Perro):


    def __init__(self, ladrar):
        #super(PastorAleman, self).__init__(ladrar)
        result = super().__init__(ladrar)
        print("result es :", result)


    def _mover(self):
        print("Ahora a mover la cola")
        resultado = super(PastorAleman, self)._mover_cola()
        print('resultado es {}'.format(resultado))
        resultado['cola'] = 'Moviendo la cola pero con modificacion'
        print(resultado['cola'])


#perro = Perro("Guau Guau")
pastor = PastorAleman("Guau Guau")
pastor.ladrar()
pastor._mover()




