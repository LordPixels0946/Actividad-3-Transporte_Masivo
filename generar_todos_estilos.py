# -*- coding: utf-8 -*-
"""
GENERADOR AUTOMÁTICO DE MAPAS CON TODOS LOS ESTILOS
Genera mapas con los 5 estilos disponibles para que los compares
"""

import sys
sys.path.insert(0, 'src')

from src.base_conocimiento import BaseConocimiento
from src.algoritmo_a_estrella import AlgoritmoAEstrella
from src.mapa_interactivo import MapaInteractivoSETP


def main():
    """Genera mapas con todos los estilos automáticamente"""
    print("\n" + "="*60)
    print("  GENERADOR DE MAPAS - TODOS LOS ESTILOS")
    print("="*60 + "\n")
    
    # Inicializar componentes
    base = BaseConocimiento()
    algoritmo = AlgoritmoAEstrella(base)
    
    # Ruta de ejemplo: Terminal → Estadio
    origen, destino = 'Terminal', 'Estadio'
    print(f"📍 Calculando ruta: {origen} → {destino}")
    ruta, num_paradas, costo = algoritmo.buscar_ruta(origen, destino)
    tiempo_estimado = int(costo * 3.5)
    print(f"   ✓ Ruta: {' → '.join(ruta)}")
    print(f"   ✓ {num_paradas} paradas, {costo:.2f} km, {tiempo_estimado} min\n")
    
    # Estilos disponibles
    estilos = {
        'carto_light': 'CartoDB Light (Claro minimalista)',
        'carto_dark': 'CartoDB Dark (Oscuro elegante)',
        'esri_world': 'Esri World (Calles profesionales)',
        'esri_satellite': 'Esri Satellite (Vista satélite real)',
        'osm': 'OpenStreetMap (Estándar detallado)'
    }
    
    print("🎨 Generando mapas con 5 estilos diferentes...\n")
    
    archivos_generados = []
    
    for i, (key, desc) in enumerate(estilos.items(), 1):
        print(f"   {i}/5 → {desc}")
        
        # Crear nueva instancia con el estilo específico
        mapa = MapaInteractivoSETP(base)
        mapa.tile_default = key
        
        # Generar mapa (sin abrir automáticamente)
        archivo = mapa.crear_mapa_ruta(
            origen, destino, ruta, costo, tiempo_estimado, abrir=False
        )
        
        archivos_generados.append((key, desc, archivo))
        print(f"       ✓ Guardado: {archivo}\n")
    
    print("="*60)
    print("  ✅ TODOS LOS MAPAS GENERADOS EXITOSAMENTE")
    print("="*60 + "\n")
    
    print("📂 Archivos generados en outputs/:\n")
    for key, desc, archivo in archivos_generados:
        nombre_archivo = archivo.split('\\')[-1]
        print(f"  • {nombre_archivo}")
        print(f"    Estilo: {desc}\n")
    
    print("🌐 Para ver los mapas:")
    print("   1. Abre la carpeta outputs/")
    print("   2. Haz doble clic en cualquier archivo .html")
    print("   3. Compara los diferentes estilos\n")
    
    print("💡 TIP: Para cambiar el estilo predeterminado:")
    print("   Edita src/mapa_interactivo.py, línea 54")
    print("   Cambia: self.tile_default = 'nombre_del_estilo'\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Proceso interrumpido.\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
