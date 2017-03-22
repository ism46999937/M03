#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
numero = 0
contar = input ("El número que pongas aquí será hasta el que se cuente (solo pares):")
salir = False
while salir == False:
	print numero
	if contar == numero :
		salir = True
	numero = numero+2						
	
	
