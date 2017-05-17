# coding:utf-8


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

mesos_del_any=[]
mesos_del_any.append(1)
mesos_del_any.append(2)
mesos_del_any.append(3)
mesos_del_any.append(4)
mesos_del_any.append(5)
mesos_del_any.append(6)
mesos_del_any.append(777)
print "----------------------------------------"
print mesos_del_any
print "----------------------------------------"
mesos_del_any.remove(777)
print "----------------------------------------"
print mesos_del_any
print "----------------------------------------"
mesos_del_any.append(7)
mesos_del_any.append(8)
mesos_del_any.append(9)
mesos_del_any.append(10)
mesos_del_any.append(11)
mesos_del_any.append(12)
print "----------------------------------------"
print mesos_del_any
print "----------------------------------------"
