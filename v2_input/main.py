#Variables
#inputs
nombre_producto1 = input("Ingrese el nombre del producto 1: ")
precio_producto1 = float(input("Ingrese el precio del producto 1: "))
cantidad_producto1 = input("Ingrese el cantidad del producto 1: ")
cantidad_producto1 = int(cantidad_producto1)
#operadores (en este caso multiplicacion)
total_producto1 = precio_producto1 * cantidad_producto1


#Variables
nombre_producto2 = input("Ingrese el nombre del producto 2: ")
precio_producto2 = float(input("Ingrese el precio del producto 2: "))
cantidad_producto2 = int(input("Ingrese el cantidad del producto 2: "))
#operadores (en este caso multiplicacion)
total_producto2 = precio_producto2 * cantidad_producto2

#Hay muchas formas de hacer las mismas operaciones
#total_compra = (precio_producto1 * cantidad_producto1) + (precio_producto2 * cantidad_producto2)
#total_compra = total_producto1 + (precio_producto2 * cantidad_producto2)
total_compra = total_producto1 + total_producto2

#output
#print(...): esto es una instruccion que le estamos indicando al programa
print(f"El total de la compra es: {total_compra}")







