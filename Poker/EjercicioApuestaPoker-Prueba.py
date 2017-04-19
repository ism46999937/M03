# coding:utf-8
# Possibilitats: 1-10 J,Q,K
# jugador1 màquina
# jugador2 màquina
##############################################################
#						IMPORT
##############################################################

from random import randint
import os
os.system ('clear')

##############################################################
#				  VARIABLES GLOBALES
##############################################################

saldo=100
salir=False
salir_de_apuesta=False

##############################################################
#						NIVEL2
##############################################################
while (salir==False):
	apuesta=input("Introduzca el dinero ha apostar (mínimo 10€): ")
	if (saldo<10):
		print "No puedes apostar con menos de 10€"
		salir=True
	if(apuesta<10):
		print "La apuesta mínima es de 10€ crack!!!"
		salir_de_apuesta=True
	if (apuesta>saldo):
		print "No tienes dinero para una apuesta tan grande, sorry! pero o bajas la apuesta o a la calle!"
	if (apuesta==-1):
		print "Deseas irte? No me opondré! Paselo bien!"
		salir=True
		salir_de_apuesta=True
	if (apuesta<=saldo):
		saldo=saldo-apuesta
		salir_de_apuesta=False
while (salir_de_apuesta==False):
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
		print "empate"
	else:
		if (J1NUMERO>J2NUMERO):
			print "J1 gana"
			saldo=saldo-apuesta
			print "Este es tu saldo actual: ", saldo
			salir=True
		else:
			print "J2 gana"
			saldo=saldo+(apuesta*2)
			print "Este es tu saldo actual: ", saldo
			salir=True
	if (saldo<10):
		salir=True
#	else:
#		if (apuesta==-1):
#			salir=True
#			salir_apuesta=True
#		else:
#			if(apuesta<10):
#				salir_apuesta=True
	else:
		apuesta=input("Introduzca el dinero ha apostar (mínimo 10€): ")
	if apuesta==-1:
		salir=True
		salir_de_apuesta=True
##############################################################
#						NIVEL1
##############################################################

	

