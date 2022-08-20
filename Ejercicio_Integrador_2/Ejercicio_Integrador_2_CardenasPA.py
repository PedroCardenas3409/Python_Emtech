# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:14:12 2022

@author: CARDENAS MEDINA
"""

import csv
aeropuertos_mayor_pasajeros = []
aeropuertos_menores_vuelos = []
total_pasajeros = 0
promedio_todos_pasajeros = 0


with open("aeropuertos_pasajeros.csv","r") as archivo:
    lector = csv.reader(archivo)
    
    lector = sorted(lector, key = lambda linea: linea[3], reverse = True )
    
    contador = 0
    
    for linea in lector:
        
        if(contador == 5):
            break
        else:
            if(linea[0] != 'Estado'):
                aeropuertos_mayor_pasajeros +=  [linea]
                contador += 1
    
    contador = 0
with open("aeropuertos_pasajeros.csv","r") as archivo:
    lector = csv.reader(archivo)
    
    for linea in lector:
        if(linea[0] != 'Estado'):
            total_pasajeros += int(linea[3])
            contador += 1
    
    promedio_todos_pasajeros = total_pasajeros / contador

    contador = 0
with open("aeropuertos_pasajeros.csv","r") as archivo:
    lector = csv.reader(archivo)
    
    lector = sorted(lector, key = lambda linea: linea[4])
    
    for linea in lector:
        if(contador == 5):
            break
        else:
            if(linea[0] != 'Estado' and linea[0] != 'Sinaloa'):
                aeropuertos_menores_vuelos +=  [linea]
                contador += 1
     
archivo_resultado = open("archivo_resultado.txt", "w")

def mensaje_de_archivo(mensaje):

    archivo_resultado.write(mensaje)
        
     
        
     
    
mensaje_de_archivo("1. Conocer los 5 aeropuertos que tienen mayor cantidad de pasajeros que desean viajar a Sinaloa: \n \n")
    
contador = 0
suma_pasajeros_mayor_cantidad = 0
    
for aeropuerto in aeropuertos_mayor_pasajeros:
    mensaje_de_archivo("    " + str(contador + 1) + ".- Aeropuerto en la Ciudad de " + aeropuerto[0] + " del estado de " + aeropuerto[1] + ". \n")
    suma_pasajeros_mayor_cantidad += int(aeropuerto[3]) 
    contador += 1
        
promedio_pasajeros_mayor_cantidad = suma_pasajeros_mayor_cantidad / contador
    
mensaje_de_archivo("     Promedio de los pasajeros de los 5 aeropuertos: " + str(promedio_pasajeros_mayor_cantidad) + " \n")
mensaje_de_archivo("\n2. El promedio de pasajeros considerando todos los aeropuertos. \n")
mensaje_de_archivo("\n    El promedio de todos los pasajeros de los aeropuertos es de: " + str(promedio_todos_pasajeros) + "\n")
mensaje_de_archivo("\n3. Los 5 aeropuertos con menos vuelos hacia Sinaloa. (Quitando a los de Sinaloa) \n\n")

    
contador = 0
suma_pasajeros_menores_vuelos = 0
    
for aeropuerto in aeropuertos_menores_vuelos:
    mensaje_de_archivo("    " + str(contador + 1) + ".- Aeropuerto en la Ciudad de " + aeropuerto[0] + " del estado de " + aeropuerto[1] + ". \n")
    suma_pasajeros_menores_vuelos += int(aeropuerto[3])
    contador += 1
        
promedio_pasajeros_menores_vuelos = suma_pasajeros_menores_vuelos / contador
    
mensaje_de_archivo("     Promedio de los pasajeros de los 5 aeropuertos: " + str(promedio_pasajeros_menores_vuelos) + " \n")
    
    
archivo_resultado.close()
    
    
    
    
    
        