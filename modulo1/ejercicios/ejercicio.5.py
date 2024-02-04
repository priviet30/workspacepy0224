#operaciones => siempre devuelven false o true
a=5
b=10

c1=a==b
c2=a<b
d1=c1 and c2 # falso por tabla de verdad
d2=c1 or c2 # verdadero
print(c1,"=>",c2,"=>",d1,"=>",d2)
