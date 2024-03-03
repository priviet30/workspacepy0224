class Producto:
    nombre:None
    codigo:None
    pais:None
    lote:None
    def __init__(self, nombre, codigo):
        self.nombre=nombre
        self.codigo=codigo
        self.pais=codigo[0:4]
        self.lote=codigo[5:10]
    def __str__(self) -> str:
        return f"El producto {self.nombre} viene del pais {self.pais} y tiene un numero de lote {self.lote}"

producto1=Producto('glacitas', 'PERU-00001-2024')
print(producto1)
