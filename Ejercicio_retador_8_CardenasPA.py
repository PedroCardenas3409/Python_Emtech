clientes={45471:['Luis Perez',45,'BJX', True], 8944411:['Fernanda Garcia',25,'JAL', True], 15223:['Alejandra Ortiz',33,'JAL', True]}
IATA_destino = ('BJX','GDL', 'JAL')
edad_clientes = [0,0,0]
contador_clientes = [0,0,0]
destino_Final = []
edad_promedio = []

def agregarClientes():
	id_ine = int(input("Ingresa el ID del INE: "))
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

	clientes.setdefault( id_ine, [nombre, edad, destino, cliente_preferente])

def mostrarTodosLosClientes():
	contador = 0 
	id_clientes = list(clientes)

	print("")
	print("Lista de todos los clientes: ")

	while len(clientes) > contador:
		print("ID del INE: " + str(id_clientes[contador]) + ", Nombre: " + clientes[id_clientes[contador]][0])
		contador += 1
	print("")

def mostrarClientesPreferentes():
	contador = 0
	id_clientes = list(clientes)

	print("")
	print("Lista de todos los clientes preferentes: ")
	
	while len(clientes) > contador:
		if(clientes[id_clientes[contador]][3] == True):
			print("ID del INE: " + str(id_clientes[contador]) + ", Nombre: " + clientes[id_clientes[contador]][0])
		contador = contador + 1
	print("")

def eliminarClientes():
	id_eliminar = int(input("Ingrese el ID del INE a eliminar: "))

	return id_eliminar

def edadPromedioTodosLosClientes():
	contador = 0
	id_clientes = list(clientes)
	edad_todos_clientes = 0

	while len(clientes) > contador:
		edad_todos_clientes += clientes[id_clientes[contador]][1] 
		contador += 1

	edad_prom_todo_clientes = edad_todos_clientes / len(clientes)

	print("La edad promedio de todos los clientes es de: ", edad_prom_todo_clientes)

def edadPromedioClientesPreferentes():
	contador = 0
	contador_cliente_preferente = 0
	id_clientes = list(clientes)
	edad_todos_clientes = 0

	while len(clientes) > contador:
		if(clientes[id_clientes[contador]][3] == True):
			edad_todos_clientes += clientes[id_clientes[contador]][1] 
			contador_cliente_preferente += 1
		contador += 1

	if(contador_cliente_preferente > 0):
		edad_prom_todo_clientes = edad_todos_clientes / contador_cliente_preferente
		print("La edad promedio de todos los clientes preferentes es de: ", edad_prom_todo_clientes)
	else:
		print("la edad promedio no puede sacarse porque no hay clientes preferentes")
	

while True:
	print("(1) Añadir nuevos clientes.")
	print("(2) Listar todos los clientes.")
	print("(3) Listar clientes preferentes.")
	print("(4) Eliminar un cliente mediante ID del INE.")
	print("(5) Edad promedio de todos los clientes.")
	print("(6) Edad promedio de clientes preferentes.")
	print("(7) Salir.")

	opcion = int(input("Ingrese una opcion: "))

	if(opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5  and opcion != 6  and opcion != 7):
		print("Opcion No Valida")

	else:
		if(opcion == 1):
			agregarClientes()

		if(opcion == 2):
			mostrarTodosLosClientes()

		if(opcion == 3):
			mostrarClientesPreferentes()

		if(opcion == 4):
			id_eliminar = eliminarClientes()
			del clientes[id_eliminar]

		if(opcion == 5):
			edadPromedioTodosLosClientes()

		if(opcion == 6):
			edadPromedioClientesPreferentes()

		if(opcion == 7):
			break


contador = 0
id_clientes = list(clientes)

while len(clientes) > contador:

	if(clientes[id_clientes[contador]][2] == IATA_destino[0]):
		edad_clientes[0] += clientes[id_clientes[contador]][1] 
		contador_clientes[0] += 1

	elif(clientes[id_clientes[contador]][2] == IATA_destino[1]):
		edad_clientes[1] += clientes[id_clientes[contador]][1]
		contador_clientes[1] += 1

	else:
		edad_clientes[2] += clientes[id_clientes[contador]][1]
		contador_clientes[2] += 1 

	contador = contador + 1

destino_Final.append(('BJX', contador_clientes[0]))
destino_Final.append(('GDL', contador_clientes[1]))
destino_Final.append(('JAL', contador_clientes[2]))

if(contador_clientes[0] != 0):
	edad_promedio.append(('BJX', edad_clientes[0] / contador_clientes[0]))

if(contador_clientes[1] != 0):
	edad_promedio.append(('GDL', edad_clientes[1] / contador_clientes[1]))

if (contador_clientes[2] != 0):
	edad_promedio.append(('JAL', edad_clientes[2] / contador_clientes[2]))

print("Detalles de vuelos: ", sorted(destino_Final, key = lambda destino_Final: destino_Final[1], reverse = True ))
print("Edad promedio por vuelo: ", sorted(edad_promedio, key = lambda edad_promedio: edad_promedio[1], reverse = True ))