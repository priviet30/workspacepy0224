while True:
    from lib.fx import Dividir_numeros
    try:
        a=float(input("Digita el número a dividir: "))
        b=float(input("Digite el divisor: "))
        producto=Dividir_numeros(a,b)
        print(f"Al dividir {a} entre {b}, se obtiene: {producto}")
        break
    except Exception as e:
        print(e)
       