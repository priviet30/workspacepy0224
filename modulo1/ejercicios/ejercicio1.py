# realizar un programa que me muestre si un numero ingresado por teclado es par o impar

numero_por_revisar= input("ingresar numero: ")
print(numero_por_revisar)
type_numero=type(numero_por_revisar)
print("numero por revisar",type_numero)
### como convertir una variable de un tipo a otro tipo  
### como cambiar el tipo de variable
### se llama parseo o parsear
numero_parseado=int(numero_por_revisar)
### variable_nueva = tipo por cambiar( variable por cambiar)
type_numero_parseado=type(numero_parseado)
print("numero parseado",type_numero_parseado)

### operaciones 
resultado1=numero_por_revisar*3
resultado2=numero_parseado*3
print("resultados",resultado1,"=>",resultado2)

##### el operador modulo es el residuo de la operacion de division

is_par=numero_parseado%2

print(is_par) ### si es 1 es impar y si es 0 es par
