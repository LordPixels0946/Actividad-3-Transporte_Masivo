# -*- coding: utf-8 -*-
"""
GENERADOR DE MAPAS INTERACTIVOS
Script para generar mapas interactivos de la red SETP Neiva
"""

import sys
sys.path.insert(0, 'src')

from src.base_conocimiento import BaseConocimiento
from src.algoritmo_a_estrella import AlgoritmoAEstrella
from src.mapa_interactivo import MapaInteractivoSETP


def main():
    """Genera mapas interactivos del sistema SETP"""
    print("\n" + "="*60)
    print("  GENERADOR DE MAPAS INTERACTIVOS - SETP NEIVA")
    print("="*60 + "\n")
    
    # Inicializar componentes
    base = BaseConocimiento()
    algoritmo = AlgoritmoAEstrella(base)
    mapa = MapaInteractivoSETP(base)
    
    # 1. Generar mapa de la red completa
    print("📍 1. Generando mapa de la red completa...")
    mapa.crear_mapa_red_completa(abrir=False)
    
    # 2. Generar mapas de rutas de ejemplo
    rutas_ejemplo = [
        ('Terminal', 'Estadio'),
        ('San Mateo', 'Sevilla'),
        ('Calle 7', 'Limonar'),
        ('Centro', 'Calixto')
    ]
    
    print(f"\n📍 2. Generando {len(rutas_ejemplo)} mapas de rutas de ejemplo...")
    
    for origen, destino in rutas_ejemplo:
        print(f"\n   → Calculando ruta: {origen} → {destino}")
        resultado = algoritmo.buscar_ruta(origen, destino)
        
        if resultado[0] is not None:
            ruta, num_paradas, costo = resultado
            tiempo_estimado = int(costo * 3.5)
            
            mapa.crear_mapa_ruta(
                origen,
                destino,
                ruta,
                costo,
                tiempo_estimado,
                abrir=False
            )
            
            print(f"     ✓ Ruta: {' → '.join(ruta)}")
            print(f"     ✓ Distancia: {costo:.2f} km | Tiempo: {tiempo_estimado} min")
        else:
            print(f"     ✗ No se encontró ruta entre {origen} y {destino}")
    
    print("\n" + "="*60)
    print("  ✅ MAPAS GENERADOS EXITOSAMENTE")
    print("="*60)
    print("\nLos mapas HTML se han guardado en la carpeta 'outputs/'")
    print("Puede abrirlos con cualquier navegador web.\n")
    
    # Preguntar si desea abrir el último mapa
    print("¿Desea abrir el último mapa generado en el navegador? (s/n): ", end="")
    respuesta = input().strip().lower()
    if respuesta in ['s', 'si', 'sí']:
        # Generar y abrir el último mapa
        origen, destino = rutas_ejemplo[-1]
        resultado = algoritmo.buscar_ruta(origen, destino)
        if resultado[0] is not None:
            ruta, num_paradas, costo = resultado
            tiempo_estimado = int(costo * 3.5)
            mapa.crear_mapa_ruta(
                origen,
                destino,
                ruta,
                costo,
                tiempo_estimado,
                abrir=True
            )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Proceso interrumpido por el usuario.\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
