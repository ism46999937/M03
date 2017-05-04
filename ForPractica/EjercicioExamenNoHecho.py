# coding:utf-8
import os
os.system ('clear')
# Des de 0 fins a 3-1(2)
for fil in xrange(1,6,1):
	for col in xrange(1,5,1):
		if (fil==1):
			if (col==2):
				print "A"
			else:
				if (col==3):
					print "B"
				else:
					if (col==4):
						print "C"
					else:
						print "-"
		else:
			if (col==1):
				if (fil==2):
					print 1
				else:
					if (fil==3):
						print 2
					else:
						if (fil==4):
							print 3
						else:
							print 4
			else:
				print ""
