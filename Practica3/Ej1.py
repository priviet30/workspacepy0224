class Catalogo:
    productos=[]
    def __init__(self, productos=[]):
        self.productos=productos
    def Agregar(self,p):
        self.productos.append(p)
    def __str__(self) -> str:
        return f"Se registro el producto {self.productos}"
    def mostrar(self):
        for p in self.productos:
            print(p)
           
class Productos:
    pass

print("Bienvenido a nuestro catálogo, nuestros productos son los siguientes:")
catalogo1=Catalogo()
catalogo1.Agregar('glacitas')
catalogo1.Agregar('oreo')
catalogo1.Agregar('chomp')
catalogo1.mostrar() 