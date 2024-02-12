ing=float(input("¿Cuánto es el ingreso total en su casa?"))
luz=float(input("¿Cuánto paga por luz en promedio?"))
agua=float(input("¿Cuánto paga por agua en promedio?"))
alq=float(input("¿Cuánto paga por alquiler?"))
mens=float(input("¿Cuánto paga mensualmente por sus clases en Datux?"))
gasto=luz+agua+alq+mens
ahorro=ing-gasto
msg=f"Mensualmente gasta un total de S/{gasto} y ahorra un total de S/{ahorro}"
print(msg)