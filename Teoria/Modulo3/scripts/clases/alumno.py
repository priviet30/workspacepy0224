"""

Realizar una función que permita la carga de n alumnos. 
Por cada alumno se deberá preguntar el nombre completo y permitir el ingreso de 3 notas. 
Las notas deben estar comprendidas entre 0 y 10. 
Devolver el listado de alumnos.
"""

def ingreso_numero_decimal(msg= 'Ingrese un número decimal: '):
    """Validar el ingreso de un número decimal """
    try:
        numero = float(input(msg))
        return numero
    except:
        print('Numero invalido, vuelva a ingresar el dato ...')
        return ingreso_numero_decimal(msg)

def ingreso_numero_entero(msg= 'Ingrese un número entero: '):
    """Validar el ingreso de un número entero """
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Numero invalido, vuelva a ingresar el dato ...')
        return ingreso_numero_entero(msg)


class Alumno:
    aprobado = True
    def __init__(self, nombre_alumno) -> None:
        self.nombre = nombre_alumno
        self.listado_notas = [
            self.ingreso_nota('Ingrese la 1ra nota: '),
            self.ingreso_nota('Ingrese la 2da nota: '),
            self.ingreso_nota('Ingrese la 3ra nota: ')
        ]

        # for i in range(3):
        #     nota = self.ingreso_nota(f'Ingrese la {i+1} nota: ')
        #     self.listado_notas.append(nota)

        self.aprobado = self.bool_aprobado()
        pass

    def ingreso_nota(self, msg:str):
        try:
            nota = ingreso_numero_decimal(msg=msg)
            assert nota<=10 and nota>=0
            return nota
        except:
            print('Nota invalida, vuelva a intentar!!!')
            return self.ingreso_nota(msg)

    def bool_aprobado(self):
        return sum(self.listado_notas)/3 >=4

    def imprimir_alumno(self):
        print(f'Nombre_alumno: {self.nombre}\nNotas: {self.listado_notas}')

class Colegio:

    def __init__(self, nombre_colegio, listado_alumnos=[]):
        self.nombre = nombre_colegio

        self.alumnos = listado_alumnos
        pass

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_listado_alumnos(self):
        for alumno in self.alumnos:
            alumno.imprimir_alumno()
        

n = 2

colegio1 = Colegio('Saco Oliveros') 

for i in range(n):
    nombre_alumno = input('Ingrese nombre alumno: ')
    colegio1.agregar_alumno(Alumno(nombre_alumno))


colegio1.mostrar_listado_alumnos()
