def sumar(a,b):
    return a + b

def dividir(a,b):
    
    assert b!=0, 'División entre 0'
    return a/b


# Validarcion
if __name__ == '__main__':
    assert sumar(1,5)==6
    print(sumar(1,2),3)