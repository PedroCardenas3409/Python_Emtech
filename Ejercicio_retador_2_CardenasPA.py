
municipios = []
habitantes = []
contador = 0
sumatoria = 0
promedio = 0 

print("Entrada:")
while contador < 3:
	municipio = input("Ingresa el municipio:")
	municipios.append(municipio)
	habitante = int(input("Ingresa el número de habitantes:"))
	habitantes.append(habitante)
	contador += 1

"""
Otra forma de sumar la lista:

for hab in habitantes:
    sumatoria  += hab
"""

sumatoria = sum(habitantes)
promedio = sumatoria/len(habitantes)
promedio = round(promedio, 2)

print("Salida:")
print("El total de habitantes es:",sumatoria)
print("El promedio de habitantes es:",promedio)
