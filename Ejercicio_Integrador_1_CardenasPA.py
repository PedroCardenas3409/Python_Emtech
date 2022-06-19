Descuento = False
Num_Cajas_Venta = 0
Id_Producto = 0
Tipo_de_Producto = ""
Costo_por_caja = 0
Costo_Total = 0
Cajas_Vendidas = 0
Descuento_Precio = 0

venta_productos = [[2, 122],[1, 89],[1, 22],[3, 48],[1, 75],[3, 322],[2, 95],[1, 148],[1, 83],[3, 100]]

for venta in venta_productos:
    Cajas_Vendidas  += venta[1]


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

if (Cajas_Vendidas + Num_Cajas_Venta) > 1500:
	Descuento = True
	Descuento_Precio = Costo_Total * .20
	Costo_Total = Costo_Total - Descuento_Precio


Costo_Total = round(Costo_Total, 2)


print("Salida:")
print("El producto es:",Tipo_de_Producto)
print("El precio por caja es:",Costo_por_caja)
print("Aplica descuento del 20%:",Descuento)
print("El costo total a pagar:",Costo_Total)

venta_productos.append([Id_Producto,Num_Cajas_Venta])