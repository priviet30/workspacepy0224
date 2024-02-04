### crear una calcudora de taxes en base a tu salario
# reglas => se cobra solo a los mayores de edad 
#  tasa para sueldos menores a 10k anual es 0
#  menor a 18k es 5%  , menor 25k es 10% y luego todos los siguientes es 15%

print("Ingrese sus datos")
nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad: "))
salario=input("ingrese su salario anual:")


if edad >=18:
    impuesto=0.0
    salario_parseado=float(salario)
    if salario_parseado<10000:
        tasa=0.0
    elif salario_parseado<18000:
        tasa=5     
    elif salario_parseado<25000:
         tasa=10       
    else:
         tasa=10
    impuesto=salario_parseado*(tasa/100)
    correo=input("ingrese su correo: ")
    msg=f"su impuesta sera {impuesto} le enviaremos los datos a su correo. Gracias"
    print(msg   )
else:
    msgError=f"""Hola {nombre} , 
            usted aun no califica para aportar impuestos.
            ya que tiene {edad} años y se cobra apartir de los 18 años"""
    print(msgError)