#!/usr/bin/python
# coding: utf-8
import time 
import os

os.system ('clear')
time.sleep (2)
J1 = raw_input("J1 Introduce: piedra, papel o tijera: ")
J2 = raw_input("J2 Introduce: piedra, papel o tijera: ")
print
print
if (J1 == "piedra" and J2 == "papel"):
	print "J2 gana"
if (J1 == "piedra" and J2 == "tijera"):
	print "J1 gana"
if (J1 == "tijera" and J2 == "papel"):
	print "J1 gana"
if (J1 == "tijera" and J2 == "piedra"):
	print "J2 gana"
if (J1 == "papel" and J2 == "tijera"):
	print "J2 gana"
if (J1 == "papel" and J2 == "piedra"):
	print "J1 gana"
if J1 == J2 :
	print "Esto es empate!!!"
