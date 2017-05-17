# coding:utf-8
# Possibilitats: PE, PA, TI, LA
# Total 9: 3 empat, 6 guanyador
# jugador1 maquina
# jugador2 maquina

from random import randint
import os
os.system ('clear')
#Definim el my_range
def my_range (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment

#Jugador 
palos=["D","C","T","P"]
numeros=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
randint=palos
randint=numeros
#Jugadors maquines tirades:

for num in my_range(0,13,1):	
	
	if (numeros==11):
		print numeros[10]
	if (numeros==12):
		print numeros[11]
	if (numeros==13):
		print numeros[12]
	if (numeros==1):
		print numeros[0]
	if (numeros==10):
		print numeros[9]
	if (numeros==9):
		print numeros[8]
	if (numeros==8):
		print numeros[7]
	if (numeros==7):
		print numeros[6]
	if (numeros==6):
		print numeros[5]
	if (numeros==5):
		print numeros[4]
	if (numeros==4):
		print numeros[3]
	if (numeros==3):
		print numeros[2]
	if (numeros==2):
		print numeros[1]

for pal in my_range(0,3,1):
		
	if (palos==1):
		print palos[0],
	if (palos==2):
		print palos[1],
	if (palos==3):
		print palos[2],
	if (palos==4):
		print palos[3],
	
	print "la jugada de J1 ha sido: " , num , pal
	

	
for num2 in my_range(0,12,1):	
	
	if (numeros==11):
		print numeros[10]
	if (numeros==12):
		print numeros[11]
	if (numeros==13):
		print numeros[12]
	if (numeros==1):
		print numeros[0]
	if (numeros==10):
		print numeros[9]
	if (numeros==9):
		print numeros[8]
	if (numeros==8):
		print numeros[7]
	if (numeros==7):
		print numeros[6]
	if (numeros==6):
		print numeros[5]
	if (numeros==5):
		print numeros[4]
	if (numeros==4):
		print numeros[3]
	if (numeros==3):
		print numeros[2]
	if (numeros==2):
		print numeros[1]
		
for pal2 in my_range(0,3,1):
		
	if (palos==1):
		print palos[0],
	if (palos==2):
		print palos[1],
	if (palos==3):
		print palos[2],
	if (palos==4):
		print palos[3],
	
	print "la jugada de J2 ha sido: " , num2 , pal2
	
	if (num==num2):
		print "empate"
	else:
		if (num>num2):
			print "J1 gana"
		else:
			print "J2 gana"
			


