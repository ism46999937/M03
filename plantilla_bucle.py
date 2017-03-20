#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
salir = False
while salir == False:
	print ("Hola")
	salir = raw_input ("Pulsar una s minúscula o mayúscula para salir: ")
	if salir == "S" or salir == "s":
		print "Adios"
	else:
		salir = True
