#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
numero = 1
salir = False
while salir == False:
	print numero
	if numero == 50 :
		salir = True
	numero = numero+1

