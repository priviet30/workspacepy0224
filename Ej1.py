alumnos=[
        {'nombre':"Brando", 'edad': 15, 'correo': "brando11@gmail.com", 'cursos': ['comunicación', 'matemática', 'historia', 'lenguaje']},
        {'nombre':"Cristofer", 'edad': 15, 'correo': "cris13@gmail.com", 'cursos': ['arte', 'matemática', 'religión', 'deporte']},
        {'nombre':"Luciano", 'edad': 14, 'correo': "gallo03@gmail.com", 'cursos': ['comunicación', 'química', 'historia', 'física']},
        {'nombre':"Clari", 'edad': 15, 'correo': "clari26@gmail.com", 'cursos': ['comunicación', 'matemática', 'física', 'química']},
        {'nombre':"Milagro", 'edad': 14, 'correo': "valicha06@gmail.com", 'cursos': ['religión', 'arte', 'deporte', 'historia']}
        ]
cursos=[
        {'cursos': ['comunicación', 'matemática', 'historia', 'lenguaje'], 'notas': [15, 10, 11, 13]},
        {'cursos': ['arte', 'matemática', 'religión', 'deporte'], 'notas': [11, 5, 10, 9]},
        {'cursos': ['comunicación', 'química', 'historia', 'física'], 'notas': [12, 7, 10, 8]},
        {'cursos': ['comunicación', 'matemática', 'física', 'química'], 'notas': [13, 11, 12, 12]},
        {'cursos': ['religión', 'arte', 'deporte', 'historia'], 'notas': [14, 16, 13, 17]}
        ]

def mayormenor(a,b):
    if a>b:
        print(f"{a} es mayor que {b}.")
    elif b>a:
        print(f"{b} es mayor que {a}.")
    else:
        print("Los números son iguales.")

while True:
    print("Bienvenido :)")
    print("Ingrese una opcion")
    opciones="""
        1. Saludar
        2. Operación matemética
        3. Agregar información
        4. Calculo del promedio de las notas
        5. Listado de alumnos aprobados
        6. Listado de alumnos desaprobados
        7. Números multiplos del 2, 5 y 7
        8. Comparación de numeros mayor y menor
        9. Salir
    """
    print(opciones)
    opc=int(input("Digite su opción: "))
    if opc==1:
        name=input("Ingrese su nombre: ")
        print(f"Bienvenido {name}.")
    elif opc==2:
        num1=float(input("Digite un numero: "))
        num2=float(input("Digite otro numero: "))
        sum=num1+num2
        print(f"La suma de los números digitados es {sum}.")
    elif opc==3:
        name=input("Ingrese su nombre: ")
        edad=input("Ingrese su edad: ")
        correo=input("Ingrese su correo: ")
        curso1=input("Ingrese el curso 1: ")
        curso2=input("Ingrese el curso 2: ")
        curso3=input("Ingrese el curso 3: ")
        curso4=input("Ingrese el curso 4: ")
        datos1={
            'nombre':name,
            'edad':edad,
            'correo':correo,
            'cursos': [curso1, curso2, curso3, curso4]
        }
        alumnos.append(datos1)
        nota1=int(input("Ingrese la nota del curso 1: "))
        nota2=int(input("Ingrese la nota del curso 2: "))
        nota3=int(input("Ingrese la nota del curso 3: "))
        nota4=int(input("Ingrese la nota del curso 4: "))
        datos2={
            'cursos': [curso1, curso2, curso3, curso4],
            'notas': [nota1, nota2, nota3, nota4]
        }
        cursos.append(datos2)

    #elif opc==4:
    elif opc==5:
        
        for i in range(0,5):
            notaf=0
            for j in range(0,4):
                notaf+=cursos[i]['notas'][j]
            promnot=notaf/4    
            if promnot >= 12:
                print(i, alumnos[i]['nombre'], f"con promedio final {promnot}")

    elif opc==6:
        for i in range(0,5):
            notaf=0
            for j in range(0,4):
                notaf+=cursos[i]['notas'][j]
            promnot=notaf/4    
            if promnot < 12:
                print(i, alumnos[i]['nombre'], f"con promedio final {promnot}")
    #elif opc==7:
    elif opc==8:
        x=float(input("Digite el primer número: "))
        y=float(input("Digite el segundo número:"))
        mayormenor(x,y)
    elif opc==9:
        print("Hasta luego")
        break
    else:
        print("Ingrese un valor correcto")
