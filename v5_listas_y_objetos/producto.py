# la clase es un molde para crear objetos
# Igual a un molde para fabricar galletas
# Si yo quiero hacer un cambio a todas las galletas, entonces debo 
# cambiar el molde, y no cada galleta por separado
class Producto:
    # atributos de la clase
    # son las propiedades del objeto
    nombre = ""
    precio = 0
    cantidad = 0

    # metodos de la clase
    # son las acciones que puede realizar el objeto
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad