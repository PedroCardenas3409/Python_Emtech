# Ejercicio Retador 6
pasajeros = []
destino_Final = []
IATA_destino = ('BJX','GDL', 'JAL')
edad_pasajeros = [0,0,0]
edad_promedio = []
contador = [0,0,0]

while True:

	nombre = input("Nombre: ")

	if(nombre != 'X' and nombre != 'x'):

		edad = int(input("Edad: "))
		destino = input("Destino: ")
		destino = destino.upper()

		while destino != 'BJX' and destino != 'GDL' and destino != 'JAL':

			print("Destino invalido")
			print("Ingrese alguno de estos destinos BJX, GDL o JAL")
			destino = input("Destino: ")
			destino = destino.upper()

		pasajeros.append((nombre, edad, destino))

	else:
		print('salio del programa')
		break

for lugar in pasajeros:
	
	if(lugar[2] == IATA_destino[0]):
		edad_pasajeros[0] += lugar[1] 
		contador[0] += 1

	elif(lugar[2] == IATA_destino[1]):
		edad_pasajeros[1] += lugar[1]
		contador[1] += 1

	else:
		edad_pasajeros[2] += lugar[1]
		contador[2] += 1 

destino_Final.append(('BJX', contador[0]))
destino_Final.append(('GDL', contador[1]))
destino_Final.append(('JAL', contador[2]))

if(contador[0] != 0):
	edad_promedio.append(('BJX', edad_pasajeros[0] / contador[0]))

if(contador[1] != 0):
	edad_promedio.append(('GDL', edad_pasajeros[1] / contador[1]))

if (contador[2] != 0):
	edad_promedio.append(('JAL', edad_pasajeros[2] / contador[2]))

print("Detalles de vuelos: ", sorted(destino_Final, key = lambda destino_Final: destino_Final[1], reverse = True ))
print("Edad promedio por vuelo: ", sorted(edad_promedio, key = lambda edad_promedio: edad_promedio[1], reverse = True ))
