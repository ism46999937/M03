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

for fil in my_range(1,6,1):
	for col in my_range(1,5,1):
		if (fil==4):
			print "A"
		else:
			if(fil==1)and(col==3):
				print "*"
			else:
				if (fil==2)and(col==3):
					print "A"
				else:
					if (fil==3)and((col>1) and(col<5)):
						print "A"
					else:
						if ((fil==5)and(col==3))or((fil==6)and(col==3)):
							print "N"
						else:
							print " "
	print ""

