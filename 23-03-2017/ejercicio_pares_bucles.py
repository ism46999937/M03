#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
numero = 1
limite = input ("El número que pongas aquí será hasta el que se cuente:")
salir = False
while salir == False:
	if (numero%2 == 0) :
		print numero
	if (numero == limite) :
		salir = True
	numero = numero+1

