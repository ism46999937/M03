# coding:utf-8


import random
import os
os.system ('clear')

salir=False
num=['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', '1T', '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT', '1P', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']

while (salir == False):
	#Para coger carta y sacarla de la baraja
	if (len(num) <> 0 ):
		tirada=(random.choice(num))
		num.remove(tirada)
		
		print tirada
	else:
		#Es decir cuando no queden numeros disponibles en la baraja
		salir=True	
