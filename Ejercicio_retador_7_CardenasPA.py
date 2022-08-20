pasajeros = {'12122': ['Pedro', 21, 'GDL', True], '21765': ['Alonso', 21, 'JAL', False]}
IATA_destino = ('BJX','GDL', 'JAL')
edad_pasajeros = [0,0,0]
edad_promedio = []
destino_Final = []
contador_pasajeros = [0,0,0]

while True:
	print("(1) Añadir cliente.")
	print("(2) Listar todos los clientes.")
	print("(3) Listar clientes preferentes.")
	print("(4) Salir.")

	opcion = int(input("Ingrese una opcion: "))

	if(opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 ):
		print("Opcion No Valida")

	else:
		if(opcion == 1):
			id_ine = input("Ingresa el ID del INE: ")
			nombre = input("Ingresa el Nombre: ")
			edad = int(input("Ingresa la edad: "))
			destino = input("Ingresa el destino: ")
			destino = destino.upper()

			while destino != 'BJX' and destino != 'GDL' and destino != 'JAL':

				print("Destino invalido")
				print("Ingrese alguno de estos destinos BJX, GDL o JAL")
				destino = input("Destino: ")
				destino = destino.upper()

			cliente_preferente = input("Cliente preferente (Si/NO):")

			cliente_preferente = cliente_preferente.upper()

			while True:
				if (cliente_preferente == 'SI'):
					cliente_preferente = True
					break

				elif (cliente_preferente == 'NO'):
					cliente_preferente = False
					break

				else:
					cliente_preferente = input("Ingrese (SI/NO): ")
					cliente_preferente = cliente_preferente.upper()

			pasajeros.setdefault( id_ine, [nombre, edad, destino, cliente_preferente])

		elif(opcion == 2):
			contador = 0 
			id_pasajeros = list(pasajeros)

			print("")
			print("Lista de todos los clientes: ")

			while len(pasajeros) > contador:
				print("ID del INE: " + id_pasajeros[contador] + ", Nombre: " + pasajeros[id_pasajeros[contador]][0])
				contador += 1
			print("")

		elif(opcion == 3):
			contador = 0
			id_pasajeros = list(pasajeros)

			print("")
			print("Lista de todos los clientes preferentes: ")
			
			while len(pasajeros) > contador:
				if(pasajeros[id_pasajeros[contador]][3] == True):
					print("ID del INE: " + id_pasajeros[contador] + ", Nombre: " + pasajeros[id_pasajeros[contador]][0])
				contador = contador + 1
			print("")

		elif(opcion == 4):
			break

contador = 0
id_pasajeros = list(pasajeros)

while len(pasajeros) > contador:

	if(pasajeros[id_pasajeros[contador]][2] == IATA_destino[0]):
		edad_pasajeros[0] += pasajeros[id_pasajeros[contador]][1] 
		contador_pasajeros[0] += 1

	elif(pasajeros[id_pasajeros[contador]][2] == IATA_destino[1]):
		edad_pasajeros[1] += pasajeros[id_pasajeros[contador]][1]
		contador_pasajeros[1] += 1

	else:
		edad_pasajeros[2] += pasajeros[id_pasajeros[contador]][1]
		contador_pasajeros[2] += 1 

	contador = contador + 1

destino_Final.append(('BJX', contador_pasajeros[0]))
destino_Final.append(('GDL', contador_pasajeros[1]))
destino_Final.append(('JAL', contador_pasajeros[2]))

if(contador_pasajeros[0] != 0):
	edad_promedio.append(('BJX', edad_pasajeros[0] / contador_pasajeros[0]))

if(contador_pasajeros[1] != 0):
	edad_promedio.append(('GDL', edad_pasajeros[1] / contador_pasajeros[1]))

if (contador_pasajeros[2] != 0):
	edad_promedio.append(('JAL', edad_pasajeros[2] / contador_pasajeros[2]))

print("Detalles de vuelos: ", sorted(destino_Final, key = lambda destino_Final: destino_Final[1], reverse = True ))
print("Edad promedio por vuelo: ", sorted(edad_promedio, key = lambda edad_promedio: edad_promedio[1], reverse = True ))