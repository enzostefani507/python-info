#Se tiene una lista que contiene mensajes encriptados de varios usuarios.
#Cada mensaje se encierra entre {}, y para indicar que se terminó el área de mensajes de un usuario se 
#usa un signo &. Indique cuántos usuarios y cuántos mensajes hay en la lista, teniendo en cuenta que
#todos los mensajes están correctamente formados,es decir comienzan con { y terminan con }.
#Y que es seguro que al menos exista un usuario en la lista.

mensaje = """{hola}{este es un mensaje}{encriptado}&{este}{es de otro usuario}&"""

cant_mensajes = mensaje.count("}")
cant_usuarios = mensaje.count("&")

print ("Cantidad de mensajes {} cantidad de usuarios {} ".format(cant_mensajes, cant_usuarios))

