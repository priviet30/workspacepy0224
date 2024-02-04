# Importamos Librerias
from saludo.saludar import saludar
# from maths.operaciones_basicas import sumar, dividir
from maths import operaciones_basicas as opb
from maths import avanzadas
from validacion_datos import ingreso_numero_decimal, ingreso_numero_entero

# Definimos constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"

MENU_OPCIONES = """
¿Qué quieres hacer?
    1) Saludar
    2) Sumar dos números
    3) Funcion factorial
    4) Salir
Escribe tu respuesta: 
"""

# Definimos funciones y/o clases
def opcion2():
    n1 = ingreso_numero_decimal("Introduce el primer número: ")
    n2 = ingreso_numero_decimal("Introduce el segundo número: ")
    
    suma = opb.sumar(n1, n2)
    print(f"El resultado de la suma es: {suma}")

def opcion3():
    n = ingreso_numero_entero()
    
    assert n>=0, 'No se permite factorial negativo'
    
    factorial = avanzadas.factorial_recursivo(n)
    
    print(f'{n}!={factorial}')
    
# mi programa
def main():
    print(MENSAJE_BIENVENIDA)
    
    while True:
        respuesta = input(MENU_OPCIONES)
        if respuesta == '1':
            saludar()
        elif respuesta == '2':
            opcion2()
        elif respuesta == '3':
            opcion3()
        elif respuesta =='4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
    pass

# llamando a funcion main
if __name__ == '__main__':
    main()

