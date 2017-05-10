# coding: utf-8

import calendar
import os

os.system('clear')

# definim my_Range
def my_range (inici, fi, augment):

    while inici <= fi:

        # Retornem la variable
        yield inici

        # Augmentem la variable
        inici = inici + augment

for fil in my_range(1,8,1):
	for col in my_range(1,8,1):
		if ((fil%2==1)and(col%2==0))or((fil%2==0)and(col%2==1)):
			print "Pintado",
		else: 
			print "Blanco",
	print ""
			
