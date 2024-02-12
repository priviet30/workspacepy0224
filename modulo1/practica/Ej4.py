print("Bienvenido! Responder a las preguntas con Si o No, dependiendo el caso.")
edad=input("¿Usted es mayor de edad?")
if edad=="Si" or edad=="si":
    ruc=input("¿Usted cuenta con RUC?")
    if ruc=="Si" or ruc=="si":
        name=input("¿Cuenta con un nombre comercial?")
        if name=="Si" or name=="si":
            print("Usted es apto para abrir un comercio.")
        else:
            print("Usted no es apto para abrir un comercio")
    else:
        print("Usted no es apto para abrir un comercio") 
else:
    print("Usted no es apto para abrir un comercio")  