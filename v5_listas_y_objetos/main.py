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

def calcular_ventas_por_producto(nombre_producto: str):
    total_ventas = 0
    for producto in lista_productos:
        if producto.nombre == nombre_producto:
            total_ventas += producto.calcular_total()
    return total_ventas

def calcular_ventas_totales():
    total_ventas = 0
    for producto in lista_productos:
        total_ventas += producto.calcular_total()
    return total_ventas

def mostrar_menu():
    opcion = 0
    while opcion != 4:
        print("1. Ingresar productos")
        print("2. Calcular ventas por producto")
        print("3. Calcular ventas totales")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            pedir_productos()
        elif opcion == 2:
            nombre_producto = input("Ingrese el nombre del producto que desea calcular las ventas: ")
            ventas_por_producto = calcular_ventas_por_producto(nombre_producto)
            print(f"Las ventas por producto son: {ventas_por_producto}")
        elif opcion == 3:
            ventas_totales = calcular_ventas_totales()
            print(f"Las ventas totales son: {ventas_totales}")
        elif opcion == 4:
            print("Saliendo...")
            break

def main():
    mostrar_menu()

if __name__ == "__main__":
    main()