from producto import Producto


lista_productos: list[Producto] = []

def pedir_productos():
    agregar_otro_producto = True
    contador_productos = 0
    while (agregar_otro_producto == True):
        while (True):
            try:
                nombre = input(f"Ingrese el nombre del producto {contador_productos + 1}: ")
                if (nombre.strip() == ""):# strip elimina espacios en blanco al inicio y al final
                    raise ValueError(f"El nombre {contador_productos + 1} del producto no puede ser vacío") 
                else: 
                    break
            except ValueError as error:
                print(error)

        while (True):
            try:
                try:
                    precio = float(input(f"Ingrese el precio del producto {contador_productos + 1}: "))
                except ValueError:
                    raise ValueError(f"El precio {contador_productos + 1} del producto no es un número")
                if (precio < 0):
                    raise ValueError(f"El precio {contador_productos + 1} del producto no puede ser menor o igual a 0")
                else:
                    break
            except ValueError as error:
                print(error)
        
        while (True):
            try:
                try:
                    cantidad = int(input(f"Ingrese la cantidad del producto {contador_productos + 1}: "))
                except ValueError:
                    raise ValueError(f"La cantidad {contador_productos + 1} del producto no es un número")
                if (cantidad < 0):
                    raise ValueError(f"La cantidad {contador_productos + 1} del producto no puede ser menor o igual a 0")
                else:
                    break
            except ValueError as error:
                print(error)

        contador_productos += 1
        producto = Producto(nombre, precio, cantidad)
        lista_productos.append(producto)

        ingresar_otro_producto = input("¿Desea ingresar otro producto? (s/n): ")
        if (ingresar_otro_producto == "n"):
            agregar_otro_producto = False

def main():
    pedir_productos()
    print(lista_productos)

if __name__ == "__main__":
    main()