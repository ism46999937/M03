# coding:utf-8

# PARAMETROS
# ---------------------------------------------------------------
# nombre          : entrada          valor       no modificable
# apellido1       : entrada/salida   referencia  modificable
# apellido2       : entrada/salida   referencia  modificable
# nombre_completo : salida           referencia  modificable
# ---------------------------------------------------------------
def mensaje_bienvenida(nom, apellido1, apellido2):
	print "*****************************"
	print "          BIENVENIDO         "
	print " ", nom , "," , apellido1, "," , apellido2
	print "*****************************"
	
	nom_complet=nom+","+apellido1+" "+apellido2
	
	nom="CAMBIO"
	apellido1="CAMBIAZO"
	apellido2="CAMBIAZON"
	
	
	
	return apellido1,apellido2,nom_complet
	
#############################################################################	

nom_invitado="PEPE"
apellido1_invitat="SANCHEZ"
apellido2_invitat="LOPEZ"
nom_complet_invitat=""

print nom_invitat , apellido1_invitat, apellido2_invitat,nom_complet_invitat


# ----------------------------------------------------------------------
# nombre_invitado          : entrada          valor       no modificable
# apellido1_invitado       : entrada/salida   referencia  modificable
# apellido2_invitado       : entrada/salida   referencia  modificable
# nombre_completo_invitado : salida           referencia  modificable
# ----------------------------------------------------------------------
apellido1_invitat,apellido2_invitat,nom_complet_invitat=mensaje_bienvenida(nom_invitat,apellido1_invitat,apellido2_invitat)


# Sólo cambia el valor de los parámetro modificables
print nom_invitat , apellido1_invitat, apellido2_invitat,nom_complet_invitat
