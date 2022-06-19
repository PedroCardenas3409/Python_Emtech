Envio_Realizado = False
Peso_Maximo_Kg = 3254
Peso_Minimo_Kg = Peso_Maximo_Kg/2
Num_Cemento = 0;
Num_Yeso = 0;
Peso_Cemento = 40;
Peso_Yeso = 30;
Peso_Total = 0;

Num_Cemento = int(input("Número de costales de cemento (kg):"))
Num_Yeso = int(input("Número de costales de yeso (kg):"))

Peso_Total = (Num_Cemento * Peso_Cemento) + (Num_Yeso * Peso_Yeso)

if Peso_Total > Peso_Minimo_Kg and Peso_Total < Peso_Maximo_Kg:
	Envio_Realizado = True

print("El peso total en kg es:", Peso_Total)
print("¿Se puede realizar el envío?:", Envio_Realizado)
