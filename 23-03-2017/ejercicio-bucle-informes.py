#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
anyo = 2010
salir = False
while salir == False:
	print ("")
	anyo = input ("Teclee un año 2010 o 2016: ")
	if anyo <= 2016 :
		print "Informe", anyo
	else:
		if anyo > 2016 :
			print "No hay informe para el año especificado"
			salir = True
		
		anyo = anyo+1

