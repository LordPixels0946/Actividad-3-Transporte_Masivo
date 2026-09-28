# -*- coding: utf-8 -*-
"""
INTERFAZ DE USUARIO POR CONSOLA
Permite al usuario interactuar con el sistema de búsqueda de rutas
"""

from base_conocimiento import BaseConocimiento
from algoritmo_a_estrella import AlgoritmoAEstrella


class InterfazUsuario:
    """Gestiona la interacción con el usuario"""
    
    def __init__(self):
        self.base = BaseConocimiento()
        self.motor_busqueda = AlgoritmoAEstrella(self.base)
    
    def mostrar_banner(self):
        """Muestra el encabezado del sistema"""
        print("\n" + "="*60)
        print("  SISTEMA INTELIGENTE DE RUTAS - SETP NEIVA")
        print("  Algoritmo A* con Búsqueda Heurística")
        print("="*60 + "\n")
    
    def mostrar_estaciones(self):
        """Lista todas las estaciones disponibles"""
        estaciones = self.base.obtener_estaciones()
        print("ESTACIONES DISPONIBLES:")
        print("-" * 40)
        for i, estacion in enumerate(sorted(estaciones), 1):
            print(f"  {i:2}. {estacion}")
        print()
    
    def solicitar_estacion(self, tipo):
        """Solicita al usuario que ingrese una estación"""
        while True:
            estacion = input(f"Ingrese estación de {tipo}: ").strip()
            
            if not estacion:
                print("Error: Debe ingresar una estación\n")
                continue
            
            # Búsqueda flexible (ignorar mayúsculas/minúsculas)
            estaciones_disponibles = self.base.obtener_estaciones()
            for est in estaciones_disponibles:
                if est.lower() == estacion.lower():
                    return est
            
            print(f"Error: '{estacion}' no es una estación válida\n")
            print("Estaciones disponibles:", ", ".join(sorted(estaciones_disponibles)))
            print()
    
    def mostrar_resultado(self, ruta, num_paradas, costo):
        """Muestra el resultado de la búsqueda"""
        print("\n" + "="*60)
        print("  RESULTADO DE LA BÚSQUEDA")
        print("="*60 + "\n")
        
        print("RUTA ÓPTIMA ENCONTRADA:")
        print("-" * 40)
        for i, estacion in enumerate(ruta):
            if i == 0:
                print(f"  ▶ {estacion} (Origen)")
            elif i == len(ruta) - 1:
                print(f"  ▶ {estacion} (Destino)")
            else:
                print(f"  ▶ {estacion}")
        
        print("\n" + "-" * 40)
        print(f"Número de paradas: {num_paradas}")
        print(f"Distancia total: {costo:.2f} km")
        print(f"Tiempo estimado: {int(costo * 3.5)} minutos")
        print("="*60 + "\n")
    
    def ejecutar(self):
        """Bucle principal de la interfaz"""
        self.mostrar_banner()
        
        while True:
            self.mostrar_estaciones()
            
            # Solicitar origen y destino
            origen = self.solicitar_estacion("ORIGEN")
            destino = self.solicitar_estacion("DESTINO")
            
            if origen == destino:
                print("\n⚠ El origen y destino son iguales. No hay ruta que calcular.\n")
                if not self._continuar():
                    break
                continue
            
            # Buscar ruta con A*
            print("\n🔍 Buscando ruta óptima...\n")
            resultado = self.motor_busqueda.buscar_ruta(origen, destino)
            
            if resultado[0] is None:
                print(f"\n❌ Error: {resultado[1]}\n")
            else:
                ruta, num_paradas, costo = resultado
                self.mostrar_resultado(ruta, num_paradas, costo)
            
            # ¿Otra búsqueda?
            if not self._continuar():
                break
        
        print("\n¡Gracias por usar el Sistema de Rutas SETP Neiva!\n")
    
    def _continuar(self):
        """Pregunta si el usuario desea realizar otra búsqueda"""
        while True:
            respuesta = input("¿Desea buscar otra ruta? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí']:
                print()
                return True
            elif respuesta in ['n', 'no']:
                return False
            else:
                print("Por favor, responda 's' o 'n'\n")


if __name__ == "__main__":
    interfaz = InterfazUsuario()
    interfaz.ejecutar()
