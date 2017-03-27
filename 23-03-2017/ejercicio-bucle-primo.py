#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
ceros = 0
num = input ("Pon el numero que quieras: ") 
contar = num
salir = False
while salir == False:
	if num%contar == 0 :
		ceros = ceros+1
	if contar == 1 :
		salir = True
	contar = contar-1
if ceros == 2 :
	print "Su número es primo!!"
else :
	print "no es primo"


