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
        
for fil in my_range(1,4,1):
	for col in my_range(1,8,1):
		if (fil==1)or(fil==4):
			print "*",
		else:
			if (fil==2)and((col==1)or(col==8)):
				print "*",
			else:
				if (fil==3)and((col==1)or (col==8):
					print "*",
				else:
					if (fil==2)and((col==4)or(col==5)):
						print "·",
					else:
						if (fil==3)and(col==4):
							print "\\",
						else: 
							if (fil==3)and(col==5):
								print "/",
							else:
								print " ",
	print ""

