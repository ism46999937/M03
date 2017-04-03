#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
J1 = 31
J2 = 31
salir = False
while (salir == False) :
	if J1%7 == 0 or J1%7 == 1 :
		print "tijera"
	if J1%7 == 2 or J1%7 == 3 :
		print "piedra"
	if J1%7 == 4 or J1%7 == 5 :
		print "papel"
	if J1%7 == 6 :
		print "piedra"
	if J2%5 == 0 or J2%5 == 1 or J2%5 == 2 :
		print "papel"
	if J2%5 == 3 :
		print "tijera"
	if J2%5 == 4 :
		print "piedra"
	
		
	
	if J1 == J2 :
		print "Esto es empate!!!"
		
	if J1 == 57 and J2 == 57 :
		salir = True
	
	J1 = J1+1
	J2 = J2+1


