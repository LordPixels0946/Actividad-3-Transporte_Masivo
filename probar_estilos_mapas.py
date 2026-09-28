# -*- coding: utf-8 -*-
"""
SCRIPT PARA PROBAR DIFERENTES ESTILOS DE MAPAS
Genera mapas con todos los estilos disponibles
"""

import sys
sys.path.insert(0, 'src')

from src.base_conocimiento import BaseConocimiento
from src.algoritmo_a_estrella import AlgoritmoAEstrella
from src.mapa_interactivo import MapaInteractivoSETP


def main():
    """Genera mapas con diferentes estilos para comparar"""
    print("\n" + "="*60)
    print("  GENERADOR DE MAPAS CON DIFERENTES ESTILOS")
    print("="*60 + "\n")
    
    # Inicializar componentes
    base = BaseConocimiento()
    algoritmo = AlgoritmoAEstrella(base)
    
    # Ruta de ejemplo
    origen, destino = 'Terminal', 'Estadio'
    print(f"📍 Calculando ruta: {origen} → {destino}")
    ruta, num_paradas, costo = algoritmo.buscar_ruta(origen, destino)
    tiempo_estimado = int(costo * 3.5)
    print(f"   ✓ Ruta encontrada: {num_paradas} paradas, {costo:.2f} km\n")
    
    # Estilos disponibles
    estilos = {
        'carto_light': 'CartoDB Light (Minimalista claro)',
        'carto_dark': 'CartoDB Dark (Elegante oscuro)',
        'esri_world': 'Esri World Street (Profesional)',
        'esri_satellite': 'Esri Satellite (Vista satélite)',
        'osm': 'OpenStreetMap (Estándar)'
    }
    
    print("🎨 Estilos disponibles:\n")
    for i, (key, desc) in enumerate(estilos.items(), 1):
        print(f"  {i}. {key:15} → {desc}")
    
    print("\n" + "="*60)
    print("OPCIONES:")
    print("  1-5: Generar mapa con ese estilo específico")
    print("  all: Generar mapas con TODOS los estilos")
    print("  q: Salir")
    print("="*60)
    
    while True:
        opcion = input("\nSelecciona una opción: ").strip().lower()
        
        if opcion == 'q':
            print("\n¡Hasta luego!\n")
            break
        
        elif opcion == 'all':
            print("\n🔄 Generando mapas con todos los estilos...\n")
            for key, desc in estilos.items():
                print(f"   → Generando: {desc}")
                mapa = MapaInteractivoSETP(base)
                mapa.tile_default = key
                archivo = mapa.crear_mapa_ruta(
                    origen, destino, ruta, costo, tiempo_estimado, abrir=False
                )
                print(f"     ✓ Guardado: {archivo}\n")
            
            print("✅ Todos los mapas generados en outputs/")
            print("   Ábrelos para comparar los estilos\n")
            
            respuesta = input("¿Abrir el último mapa? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí']:
                import webbrowser, os
                webbrowser.open('file://' + os.path.abspath(archivo))
        
        elif opcion in ['1', '2', '3', '4', '5']:
            idx = int(opcion) - 1
            key = list(estilos.keys())[idx]
            desc = estilos[key]
            
            print(f"\n🗺️  Generando mapa con: {desc}")
            mapa = MapaInteractivoSETP(base)
            mapa.tile_default = key
            archivo = mapa.crear_mapa_ruta(
                origen, destino, ruta, costo, tiempo_estimado, abrir=True
            )
            print(f"✅ Mapa generado y abierto en navegador\n")
        
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Proceso interrumpido por el usuario.\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
