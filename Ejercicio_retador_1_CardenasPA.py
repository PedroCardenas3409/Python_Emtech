Estado_Sinaloa = True
Superficie_km2 = 57365
Localizacion = "noroeste"
Clima = "Calido, Subhumedo, Seco y Semiseco"
Temp_Media_Anual = "25.45 grados centigrados"
Precipitacion_Anual_Prom_mm = 790.1
Poblacion_Mujeres = 1532128
Poblacion_Hombre = 1494815
Porcentaje_Hab_Culiacan = 33.15
Porcentaje_Hab_Mazatlan = 16.57

Poblacion_Total = Poblacion_Hombre + Poblacion_Mujeres
Porcentaje_Hab_Total_Cul_Maz = Porcentaje_Hab_Culiacan + Porcentaje_Hab_Mazatlan
Temp_Media_Anual_y_clima = Temp_Media_Anual + " y clima " + Clima

print("1. La población total entre hombres y mujeres es:", Poblacion_Total, "habitantes")
print("2. El porcentaje total de la población entre Culiacán y Mazatlán es:", str(Porcentaje_Hab_Total_Cul_Maz) + "%")
print("3. La temperatura media anual y los tipos de clima es:", Temp_Media_Anual_y_clima)


