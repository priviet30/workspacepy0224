## ejemplo
""" nombre="datux"
msg0="Hola "+ nombre
msg1="Hola {}  {}".format(nombre)
msg2=f"Hola {nombre}"
print(msg0)
print(msg1)
print(msg2)
print("4.Hola",nombre) """

nombre=input("Ingrese su nombre:")
edad=input("Ingrese su edad:")
correo=input("Ingrese su correo:")

msg0="Hola "+ nombre + " " +edad + " "+ correo # str
msg1="Hola {} {} {}".format(nombre,edad,correo) # str
msg2=f"Hola {nombre} {edad} {correo}"  #str
print(msg0) # al utlimo concatena un \n que es un salto de linea
print(msg1)
print(msg2)
print("comparacion")
##### lo puedo simplificar en un solo print 
print(msg0,"\n",msg1,"\n"+msg2)
print(msg0,msg1,msg2)

