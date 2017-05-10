# coding:utf-8
def mensaje_bienvenida(nom, apellido):
	print "*****************************"
	print "          BIENVENIDO         "
	print "       	", nom , "," , apellido
	print "*****************************"
	
	nom="CAMBIO"
	apellido="CAMBIAZO"
	
	print "*****************************"
	print "          BIENVENIDO         "
	print "       	", nom , "," , apellido
	print "*****************************"	
	
#############################################################################	

nom_invitado="PEPE"
apellido_invitado="SANCHEZ"

print nom_invitado , apellido_invitado

mensaje_bienvenida(nom_invitado,apellido_invitado)


# Los parámetros no son modificables
# Aunque se cambie su valor dentro de la acción
print nom_invitado , apellido_invitado
