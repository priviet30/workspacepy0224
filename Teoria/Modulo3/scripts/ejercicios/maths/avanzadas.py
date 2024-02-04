def factorial_recursivo(n):
    if n==1 or n==0:
        return 1    
    return factorial_recursivo(n-1) * n