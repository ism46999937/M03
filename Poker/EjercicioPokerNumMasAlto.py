# coding:utf-8
# Possibilitats: PE, PA, TI, LA
# Total 9: 3 empat, 6 guanyador
# jugador1 humà
# jugador2 machine

from random import randint
import os
os.system ('clear')
#Jugador 2 màquina

#Jugador machine Tipo Carta
aleatori2=randint(1,4)
if (aleatori2==1):
	maquina2="de Picas"
if (aleatori2==2):
	maquina2="de Diamantes"
if (aleatori2==3):
	maquina2="de Tréboles"
if (aleatori2==4):
	maquina2="de Corazones"

#Jugador machine num carta
aleatori=randint(1,13)
if (aleatori==1):
    jugador2="A"
if (aleatori==2):
    jugador2="2"
if (aleatori==3):
    jugador2="3"
if (aleatori==4):
    jugador2="4"
if (aleatori==5):
    jugador2="5"
if (aleatori==6):
	jugador2="6"
if (aleatori==7):
	jugador2="7"
if (aleatori==8):
	jugador2="8"
if (aleatori==9):
	jugador2="9"
if (aleatori==10):
	jugador2="10"
if (aleatori==11):
	jugador2="J"
if (aleatori==12):
	jugador2="Q"
if (aleatori==13):
	jugador2="K"
#JUgador1 màquina
#Jugador machine 1 Tipo Carta
aleatorio2=randint(1,4)
if (aleatorio2==1):
	maquina1="de Picas"
if (aleatorio2==2):
	maquina1="de Diamantes"
if (aleatorio2==3):
	maquina1="de Tréboles"
if (aleatorio2==4):
	maquina1="de Corazones"

#Jugador machine 1 num carta
aleatorio=randint(1,13)
if (aleatorio==1):
    jugador1="A"
if (aleatorio==2):
    jugador1="2"
if (aleatorio==3):
    jugador1="3"
if (aleatorio==4):
    jugador1="4"
if (aleatorio==5):
    jugador1="5"
if (aleatorio==6):
	jugador1="6"
if (aleatorio==7):
	jugador1="7"
if (aleatorio==8):
	jugador1="8"
if (aleatorio==9):
	jugador1="9"
if (aleatorio==10):
	jugador1="10"
if (aleatorio==11):
	jugador1="J"
if (aleatorio==12):
	jugador1="Q"
if (aleatorio==13):
	jugador1="K"


# Empat (3 combinacions)
if (jugador1==jugador2):
    print "Empat"
    print "La jugada de jugador 1 ha estat: " , jugador1 
    print "La jugada de jugador 2 ha estat: " , jugador2
else: # 6 combinacions
    # Guanya jugador1 (3 combinacions)
    if (aleatorio>aleatori):
		print "Jugador 1 guanya!!"
		print "La jugada J1 ha estat: " , jugador1 , maquina1
		print "La jugada J2 ha estat: " , jugador2 , maquina2
    else: # Guanya jugador2 (3 combinacions)
        print "Jugador 2 guanya!!"
        print "La jugada J1 ha estat: " , jugador1 , maquina1
        print "La jugada J2 ha estat: " , jugador2 , maquina2

