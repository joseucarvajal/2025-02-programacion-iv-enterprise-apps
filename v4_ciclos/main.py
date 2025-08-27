#Variables
#inputs

#ciclo while
nombre_producto = ""
while (nombre_producto == ""):
    print("Ingrese el nombre del producto: ")
    nombre_producto = input()
    if (nombre_producto == ""):
        print("ERROR:El nombre del producto no puede ser vacío")

precio_producto = ""
while(precio_producto.replace(".", "").isnumeric() == False):
    print("Ingrese el precio del producto: ")
    precio_producto = input()
    if(precio_producto.replace(".", "").isnumeric() == False):
        print("ERROR:El precio del debe ser un número")
    else:
        precio_producto = float(precio_producto)
        break



