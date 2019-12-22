# -*- coding: utf-8  -*-

class Lobo:
	def __init__(self):
		self.correr = 'Corriendo'
		self.grunir = 'GR GR GR'
		self.aullar = 'Auuu!!'

	def correr(self):
		print(self.correr)


	def grunir(self):
		print(self.grunir)


	def aullar(self):
		print(self.aullar)


class Perro:
	def __init__(self):
		self.correr = 'Corriendo'
		self.ladrar = 'Guau Guau!'
		self.grunir = 'GR GR GR GR'
		self.jugar = 'El perro persigue la pelota'

	#def correr(self):
	#	print(self.correr)

	def ladrar(self):
		print(self.ladrar)

	def grunir(self):
		print(self.grunir)




class PastorAleman(Perro, Lobo):


	def __init__(self):
		super().correr()


pastor = PastorAleman()
pastor.correr()
