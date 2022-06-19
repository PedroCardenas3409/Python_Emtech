Num_Cajas_Venta = 0
Id_Producto = 0
Tipo_de_Producto = ""
Costo_por_caja = 0
Costo_Total = 0

print("Entrada:")
Num_Cajas_Venta = int(input("Número de cajas a vender:"))
Id_Producto = int(input("ID del producto:"))

if Id_Producto == 1:
	Tipo_de_Producto = "Maiz Grano"
	Costo_por_caja = 285.55

elif Id_Producto == 2:
	Tipo_de_Producto = "Pepino"
	Costo_por_caja = 334.72
else:
	Tipo_de_Producto = "Tomate Verde"
	Costo_por_caja = 129.00

Costo_Total = Costo_por_caja * Num_Cajas_Venta

if Num_Cajas_Venta <= 100:
	Costo_Total += 1500

Costo_Total = round(Costo_Total, 2)


print("Salida:")
print("El producto es:",Tipo_de_Producto)
print("El precio por caja es:",Costo_por_caja)
print("El costo total a pagar:",Costo_Total)