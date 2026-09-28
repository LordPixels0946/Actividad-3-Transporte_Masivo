# -*- coding: utf-8 -*-
"""
SCRIPT DE PRUEBAS AUTOMATIZADO
Verifica el funcionamiento correcto del sistema sin entrada manual
"""

from base_conocimiento import BaseConocimiento
from algoritmo_a_estrella import AlgoritmoAEstrella


def prueba_ruta(motor, origen, destino, descripcion):
    """Ejecuta una prueba y muestra el resultado"""
    print(f"\n{'='*60}")
    print(f"PRUEBA: {descripcion}")
    print(f"{'='*60}")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print("-" * 60)
    
    resultado = motor.buscar_ruta(origen, destino)
    
    if resultado[0] is None:
        print(f"❌ Error: {resultado[1]}")
        return False
    else:
        ruta, num_paradas, costo = resultado
        print(f"✅ Ruta encontrada:")
        print(f"   {' → '.join(ruta)}")
        print(f"   Paradas: {num_paradas}")
        print(f"   Distancia: {costo:.2f} km")
        print(f"   Tiempo estimado: {int(costo * 3.5)} min")
        return True


def main():
    """Ejecuta todas las pruebas"""
    print("\n" + "="*60)
    print("  PRUEBAS AUTOMATIZADAS - SISTEMA SETP NEIVA")
    print("="*60)
    
    base = BaseConocimiento()
    motor = AlgoritmoAEstrella(base)
    
    pruebas_exitosas = 0
    total_pruebas = 0
    
    # Prueba 1: Ruta corta directa
    total_pruebas += 1
    if prueba_ruta(motor, 'Terminal', 'Calle 7', 
                   'Ruta corta directa'):
        pruebas_exitosas += 1
    
    # Prueba 2: Ruta media
    total_pruebas += 1
    if prueba_ruta(motor, 'Terminal', 'Alcaldía', 
                   'Ruta media con múltiples paradas'):
        pruebas_exitosas += 1
    
    # Prueba 3: Ruta larga
    total_pruebas += 1
    if prueba_ruta(motor, 'Terminal', 'Estadio', 
                   'Ruta larga optimizada'):
        pruebas_exitosas += 1
    
    # Prueba 4: Ruta con alternativas
    total_pruebas += 1
    if prueba_ruta(motor, 'Centro', 'Calixto', 
                   'Ruta con caminos alternativos'):
        pruebas_exitosas += 1
    
    # Prueba 5: Estaciones extremas
    total_pruebas += 1
    if prueba_ruta(motor, 'San Mateo', 'Sevilla', 
                   'Estaciones en extremos de la red'):
        pruebas_exitosas += 1
    
    # Prueba 6: Otra combinación
    total_pruebas += 1
    if prueba_ruta(motor, 'Limonar', 'Calixto', 
                   'Ruta atravesando el centro'):
        pruebas_exitosas += 1
    
    # Prueba 7: Ruta invertida
    total_pruebas += 1
    if prueba_ruta(motor, 'Estadio', 'Terminal', 
                   'Ruta en dirección inversa'):
        pruebas_exitosas += 1
    
    # Prueba 8: Ruta corta alternativa
    total_pruebas += 1
    if prueba_ruta(motor, 'Gran Centro', 'Cándido', 
                   'Ruta corta en zona céntrica'):
        pruebas_exitosas += 1
    
    # Resumen
    print(f"\n{'='*60}")
    print("  RESUMEN DE PRUEBAS")
    print(f"{'='*60}")
    print(f"✅ Pruebas exitosas: {pruebas_exitosas}/{total_pruebas}")
    print(f"📊 Tasa de éxito: {(pruebas_exitosas/total_pruebas)*100:.1f}%")
    
    if pruebas_exitosas == total_pruebas:
        print("\n🎉 ¡Todas las pruebas pasaron correctamente!")
    else:
        print(f"\n⚠ {total_pruebas - pruebas_exitosas} prueba(s) fallaron")
    
    print("="*60 + "\n")
    
    # Verificar conectividad de la red
    print("\n" + "="*60)
    print("  VERIFICACIÓN DE CONECTIVIDAD")
    print("="*60)
    
    estaciones = base.obtener_estaciones()
    print(f"\nTotal de estaciones: {len(estaciones)}")
    print(f"Total de conexiones: {len(base.conexiones)}")
    
    # Verificar que cada estación tiene al menos una conexión
    print("\nEstaciones y sus vecinos:")
    for estacion in sorted(estaciones):
        vecinos = base.obtener_vecinos(estacion)
        print(f"  {estacion}: {len(vecinos)} conexion(es)")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
