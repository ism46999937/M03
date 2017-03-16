#!/usr/bin/python
# coding: utf-8
import time
import os
os.system('clear')
print "Menu de una calculadora"
time.sleep (2)
print "======================="
print "|1.- Sumar            |"
print "|2.- Restar           |"
print "|3.- Multiplicar      |"
print "|4.- Dividir          |"
print "|5.- Salir            |"
print "======================="
time.sleep (1)
while True:
	OpcionMenu = input("Inserta un número del 1 al 5: ")
	if OpcionMenu == 1 :
		print "Has pulsado el número 1 por tanto deseas sumar"
	elif OpcionMenu == 2 :
		print "Has pulsado el número 2 por tanto deseas restar"
	elif OpcionMenu == 3 :
		print "Has pulsado el número 3 por tanto deseas multiplicar"
	elif OpcionMenu == 4 :
		print "Has pulsado el número 4 por tanto deseas dividir"
	elif OpcionMenu == 5 :
		break
	else:
		print "Es que no sabes leer o que!! Del 1 al 5!!! Esa opción no existe" 
	
