import math
b=float(input("Ingrese el lado del triangulo equilatero:"))
area1=math.pow(b,2) *math.sqrt(3)/2
p1=3*b
msg1=f"El area del triangulo es {area1} y su perímetro es {p1}"
print(msg1)


l=float(input("Ingrese el lado del cuadrado:"))
area2=l*l
p2=4*l
msg2=f"El area del cuadrado es {area2} y su perímetro es {p2}"
print(msg2)

r=float(input("Ingrese el radio de la circunferencia:"))
area3=math.pow(r,2)*math.pi
p3=2*math.pi*r
msg3=f"El area del circulo es {area3} y su perímetro es {p3}"
print(msg3)