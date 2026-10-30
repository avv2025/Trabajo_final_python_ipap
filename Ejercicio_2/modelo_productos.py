import json
import os


# PUNTO A: CATALOGO Y REGLAS DE INVENTARIO
class StockInvalidoError(Exception):
    pass

class DispositivoEcologico:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio 
        self.stock = stock 

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(f"Error: el stock NO puede ser negativo ({valor}).")
        self.__stock = valor

    def mostrar_ficha_tecnica(self):
        return f"Dispositivo: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"

class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre, precio, stock, potencia_w, eficiencia):
        super().__init__(nombre, precio, stock)
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    def mostrar_ficha_tecnica(self):
        return (f"[Panel Solar] {self.nombre} | Potencia: {self.potencia_w}W | "
                f"Eficiencia: {self.eficiencia}% | Precio: ${self.precio} | Stock: {self.stock}")


# PUNTO B: PERSISTENCIA Y GESTION CATALOGO
class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos_serializados = []

        for disp in lista_dispositivos:
            item = {
                "tipo": type(disp).__name__,
                "nombre": disp.nombre,
                "precio": disp.precio,
                "stock": disp.stock 
            }
            if isinstance(disp, PanelSolar):
                item["potencia_w"] = disp.potencia_w
                item["eficiencia"] = disp.eficiencia
            datos_serializados.append(item)

        with open(ruta_archivo, 'w', encoding='utf8') as archivo:
            json.dump(datos_serializados, archivo, indent=4, ensure_ascii=False)

        print(f"\n¡Catálogo guardado con éxito en {ruta_archivo}!")

if __name__ == "__main__":
    print("==========================================")
    print(" PRUEBAS DE VALIDACIÓN Y EXCEPCIONES")
    print("==========================================")

    try:
        panel_erroneo = PanelSolar("Panel Test", 150.0, -5, 300, 20)
    except StockInvalidoError as e:
        print(f"-> ¡Excepción atrapada exitosamente! -> {e}")

    print("------------------------------------------")
    
    panel1 = PanelSolar("SunPower Pro 400W", 250.0, 15, 400, 21.5)
    panel2 = PanelSolar("EcoGrid Mini 200W", 120.0, 30, 200, 18.0)
    dispositivo_base = DispositivoEcologico("Termotanque Solar", 450.0, 8)

    print("\n--- FICHA TÉCNICA ---")
    print(panel1.mostrar_ficha_tecnica())
    print(panel2.mostrar_ficha_tecnica())
    print(dispositivo_base.mostrar_ficha_tecnica())

    lista_inventario = [panel1, panel2, dispositivo_base]
    ruta_json = "catalogo_ecotech.json"

    GestorInventario.guardar_catalogo_json(lista_inventario, ruta_json)