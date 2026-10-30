# DATOS ORIGINALES
registros_crudos = [
    {
        "sensor_id": " SENSOR-001 ",
        "temperatura": "24.5C",
        "ubicacion": "Planta Norte"
    },
    {
        "sensor_id": " SENSOR-002 ",
        "temperatura": "31C",
        "ubicacion": "Planta Sur"
    },
    {
        "sensor_id": " SENSOR-003 ",
        "temperatura": "27.2C",
        "ubicacion": ""
    },
    {
        "sensor_id": " SENSOR-004 ",
        "temperatura": "35.6C",
        "ubicacion": "Planta Este"
    },
    {
        "sensor_id": " SENSOR-005 ",
        "temperatura": "22.4C",
        "ubicacion": ""
    }
]
# PUNTO A: NORMALIZACION DE DATOS
def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw.get("sensor_id", "").strip()
    
    temperatura_texto = registro_raw["temperatura"].strip().replace("C", "")
    temperatura = float(temperatura_texto)
    
    ubicacion = registro_raw.get("ubicacion", "").strip()
    if ubicacion == "":
        ubicacion = "Ubicacion NO REGISTRADA"

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }         
    return registro_limpio

# PUNTO B: MONITOREO Y MAPEO

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total_sensores = len(lista_sensores_limpios)

    if total_sensores == 0:
        return [], 0.0  
       
    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        suma_temperaturas += temp
        
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
            
    promedio_temperatura = suma_temperaturas / total_sensores
    
    return lista_sensores_alerta, promedio_temperatura    

if __name__ == "__main__":
    lista_sensores_limpios = []
    for registro in registros_crudos:
        sensor_limpio = limpiar_registro_sensor(registro)
        lista_sensores_limpios.append(sensor_limpio)
        
    umbral_temperatura = 30.0

    resultado = generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura)
    lista_sensores_alerta, promedio_temperatura = resultado    
    print("\n============================================")
    print("       REPORTE ECOTECH SOLUTIONS")
    print("============================================")
    print("\nREGISTROS NORMALIZADOS:")
    for sensor in lista_sensores_limpios:
        print("--------------------------------------------")
        print("Identificador:", sensor["sensor_id"])
        print("Temperatura:", sensor["temperatura"], "°C")
        print("Ubicacion:", sensor["ubicacion"])

    
    print("\n============================================")
    print("            RESUMEN ESTADISTICO")
    print("============================================")
    print("Cantidad de sensores analizados:", len(lista_sensores_limpios))
    print("Umbral establecido:", umbral_temperatura, "°C")
    print("Sensores que superan el umbral (Alertas):")

    if len(lista_sensores_alerta) > 0:
        for sensor_id in lista_sensores_alerta:
            print("  -> Alerta en sensor:", sensor_id)
    else:
        print("  -> No se registraron alertas.")

    print(f"\nPromedio global de temperatura: {promedio_temperatura:.2f} °C")
    print("============================================")