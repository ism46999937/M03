# coding:utf-8
# Possibilitats: 1-10 J,Q,K
# jugador1 màquina
# jugador2 màquina

from random import randint
import os
os.system ('clear')

salir=False

while (salir==False) :
	J1NUMERO=randint(2,14)
	J1PALO=randint(1,4)
	J2NUMERO=randint(2,14)
	J2PALO=randint(1,4)
	
	NUMERO1=J1NUMERO
	
	if (J1NUMERO==11):
		NUMERO1="J"
	if (J1NUMERO==12):
		NUMERO1="Q"
	if (J1NUMERO==13):
		NUMERO1="K"
	if (J1NUMERO==14):
		NUMERO1="A"
	
	if (J1PALO==1):
		PALO="de picas"
	if (J1PALO==2):
		PALO="de diamantes"
	if (J1PALO==3):
		PALO="de tréboles"
	if (J1PALO==4):
		PALO="de corazones"
	
	print "la jugada de J1 ha sido: " , NUMERO1 , PALO
	
	NUMERO2=J2NUMERO
	
	if (J2NUMERO==11):
		NUMERO2="J"	
	if (J2NUMERO==12):
		NUMERO2="Q"
	if (J2NUMERO==13):
		NUMERO2="K"
	if (J2NUMERO==14):
		NUMERO2="A"
	
	if (J2PALO==1):
		PALO="de picas"
	if (J2PALO==2):
		PALO="de diamantes"
	if (J2PALO==3):
		PALO="de tréboles"
	if (J2PALO==4):
		PALO="de corazones"
	
	print "la jugada de J2 ha sido: " , NUMERO2 , PALO
	
	if (J1NUMERO==J2NUMERO):
		salir=True
	else:
		if (J1NUMERO>J2NUMERO):
			print "J1 gana"
		else:
			print "J2 gana"


