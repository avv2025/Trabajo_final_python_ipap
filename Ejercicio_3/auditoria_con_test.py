import unittest

# FUNCIÓN BASE
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo de kWh no puede ser negativo.")
    return consumo_kwh * factor_emision


# PUNTO A: AUDITORÍA DE ALGORITMO DE EMISIONES (UNITTEST)

class TestCalculoEmisiones(unittest.TestCase):
    
    def test_calculo_nominal(self):
        self.assertEqual(calcular_emisiones_carbono(100), 40.0)
        self.assertEqual(calcular_emisiones_carbono(200, 0.5), 100.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)

# PUNTO B: PROCESAMIENTO DE MÉTRICAS Y RENDERIZADO WEB
def obtener_metricas_consumo(registros):
    total_emisiones = 0.0
    max_consumo = -1
    planta_mayor_consumo = None

    for reg in registros:
        consumo = reg.get("consumo", 0)
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones

        if consumo > max_consumo:
            max_consumo = consumo
            planta_mayor_consumo = reg.get("planta")

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "max_consumo": max_consumo
    }

try:
    from django.shortcuts import render
    DJANGO_DISPONIBLE = True
except ImportError:
    DJANGO_DISPONIBLE = False

def vista_panel_sustentabilidad(request):
    
    registros_plantas = [
        {"planta": "Planta Norte (San Rafael)", "consumo": 1500},
        {"planta": "Planta Sur (General Alvear)", "consumo": 2800},
        {"planta": "Planta Oeste (Malargüe)", "consumo": 950}
    ]

    metricas = obtener_metricas_consumo(registros_plantas)

    contexto = {
        "metricas": metricas,
        "registros": registros_plantas
    }

    if DJANGO_DISPONIBLE:
        return render(request, "sustentabilidad/panel.html", contexto)
    else:
        return contexto 


if __name__ == "__main__":
    print("Ejecutando pruebas unitarias de emisiones...")
    unittest.main(verbosity=2)