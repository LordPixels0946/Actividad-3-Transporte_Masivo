# -*- coding: utf-8 -*-
"""
GENERADOR DE ANÁLISIS COMPLETO
Ejecuta análisis exhaustivo con gráficos, Excel profesional y comparativas
"""

import sys
sys.path.insert(0, 'src')

from src.base_conocimiento import BaseConocimiento
from src.algoritmo_a_estrella import AlgoritmoAEstrella
from src.visualizador import VisualizadorRed
from src.analizador_excel import AnalizadorExcel
from src.logger_metricas import LoggerMetricas
from src.comparador_ciudades import ComparadorCiudades
from datetime import datetime
import time


def generar_resultados_ejemplo(logger):
    """Genera conjunto de búsquedas de ejemplo para análisis"""
    base = BaseConocimiento()
    motor = AlgoritmoAEstrella(base)
    
    # Casos de prueba representativos
    casos = [
        ('Terminal', 'Estadio'),
        ('San Mateo', 'Sevilla'),
        ('Centro', 'Calixto'),
        ('Terminal', 'Calle 7'),
        ('Limonar', 'Calixto'),
        ('Gran Centro', 'Cándido'),
        ('Quirinal', 'San Mateo'),
        ('Alcaldía', 'Limonar'),
    ]
    
    resultados = []
    
    print("\n" + "="*60)
    print("  GENERANDO ANÁLISIS COMPLETO - SETP NEIVA")
    print("="*60 + "\n")
    
    print("📊 Fase 1: Calculando rutas óptimas...")
    for i, (origen, destino) in enumerate(casos, 1):
        print(f"   [{i}/{len(casos)}] Calculando: {origen} → {destino}")
        
        inicio = time.time()
        resultado = motor.buscar_ruta(origen, destino)
        tiempo_ejecucion = time.time() - inicio
        
        # Registrar en logger
        logger.registrar_busqueda(origen, destino, resultado, tiempo_ejecucion)
        
        ruta, paradas, distancia = resultado
        
        if ruta:
            resultados.append({
                'origen': origen,
                'destino': destino,
                'ruta': ruta,
                'paradas': paradas,
                'distancia': round(distancia, 2),
                'tiempo_estimado': int(distancia * 3.5),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
    
    return base, motor, resultados


def main():
    """Función principal que genera todos los análisis"""
    inicio = time.time()
    
    # Inicializar logger
    logger = LoggerMetricas()
    logger.logger.info("="*60)
    logger.logger.info("Iniciando análisis completo del sistema SETP Neiva")
    logger.logger.info("="*60)
    
    # Generar datos
    base, motor, resultados = generar_resultados_ejemplo(logger)
    
    print(f"\n✅ {len(resultados)} rutas calculadas exitosamente")
    
    # Inicializar visualizador
    print("\n📈 Fase 2: Generando visualizaciones...")
    visualizador = VisualizadorRed(base)
    
    # 1. Red completa
    print("   [1/6] Red completa...")
    inicio_viz = time.time()
    archivo1 = visualizador.visualizar_red_completa()
    tiempo_viz = time.time() - inicio_viz
    logger.registrar_visualizacion('red_completa', archivo1, tiempo_viz)
    print(f"      ✓ Guardado: {archivo1}")
    
    # 2. Análisis de centralidad
    print("   [2/6] Análisis de centralidad...")
    inicio_viz = time.time()
    archivo2, ranking = visualizador.analisis_centralidad()
    tiempo_viz = time.time() - inicio_viz
    logger.registrar_visualizacion('analisis_centralidad', archivo2, tiempo_viz)
    print(f"      ✓ Guardado: {archivo2}")
    
    # 3. Mapa de calor
    print("   [3/6] Mapa de conectividad...")
    inicio_viz = time.time()
    archivo3 = visualizador.mapa_calor_conectividad()
    tiempo_viz = time.time() - inicio_viz
    logger.registrar_visualizacion('mapa_calor', archivo3, tiempo_viz)
    print(f"      ✓ Guardado: {archivo3}")
    
    # 4. Gráfico comparativo
    print("   [4/6] Gráfico comparativo de rutas...")
    inicio_viz = time.time()
    archivo4 = visualizador.grafico_comparativo_rutas(resultados)
    tiempo_viz = time.time() - inicio_viz
    logger.registrar_visualizacion('comparativa_rutas', archivo4, tiempo_viz)
    print(f"      ✓ Guardado: {archivo4}")
    
    # 5-6. Visualizar algunas rutas específicas
    print("   [5/6] Visualizando ruta: Terminal → Estadio...")
    ruta1 = next(r for r in resultados if r['origen'] == 'Terminal' and r['destino'] == 'Estadio')
    inicio_viz = time.time()
    archivo5 = visualizador.visualizar_ruta(ruta1['ruta'], 'ruta_terminal_estadio.png')
    tiempo_viz = time.time() - inicio_viz
    logger.registrar_visualizacion('ruta_especifica', archivo5, tiempo_viz)
    print(f"      ✓ Guardado: {archivo5}")
    
    print("   [6/6] Visualizando ruta: San Mateo → Sevilla...")
    ruta2 = next(r for r in resultados if r['origen'] == 'San Mateo' and r['destino'] == 'Sevilla')
    inicio_viz = time.time()
    archivo6 = visualizador.visualizar_ruta(ruta2['ruta'], 'ruta_sanmateo_sevilla.png')
    tiempo_viz = time.time() - inicio_viz
    logger.registrar_visualizacion('ruta_especifica', archivo6, tiempo_viz)
    print(f"      ✓ Guardado: {archivo6}")
    
    # Generar Excel profesional
    print("\n📊 Fase 3: Generando reporte Excel profesional...")
    analizador = AnalizadorExcel(base)
    inicio_excel = time.time()
    archivo_excel = analizador.generar_reporte_completo(resultados)
    tiempo_excel = time.time() - inicio_excel
    logger.registrar_excel(archivo_excel, tiempo_excel, 7)
    print(f"   ✓ Guardado: {archivo_excel}")
    
    # Comparación con otras ciudades
    print("\n🌎 Fase 4: Generando análisis comparativo internacional...")
    comparador = ComparadorCiudades()
    
    print("   [1/3] Gráficos comparativos...")
    archivo_comp1 = comparador.generar_comparativa_grafica()
    print(f"      ✓ Guardado: {archivo_comp1}")
    
    print("   [2/3] Tabla comparativa Excel...")
    archivo_comp2 = comparador.generar_tabla_comparativa()
    print(f"      ✓ Guardado: {archivo_comp2}")
    
    print("   [3/3] Informe de posicionamiento...")
    archivo_comp3 = comparador.generar_informe_posicionamiento()
    print(f"      ✓ Guardado: {archivo_comp3}")
    
    # Generar reporte de métricas
    print("\n📋 Fase 5: Generando reporte de métricas...")
    archivo_metricas = logger.generar_reporte_metricas()
    print(f"   ✓ Guardado: {archivo_metricas}")
    
    # Resumen final
    fin = time.time()
    tiempo_total = fin - inicio
    
    print("\n" + "="*60)
    print("  ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("="*60)
    print(f"\n📁 Todos los archivos guardados en: outputs/")
    print(f"\n📊 Archivos generados:")
    print(f"   • 6 gráficos de red y rutas (PNG 300 DPI)")
    print(f"   • 1 reporte Excel completo (7 hojas)")
    print(f"   • 3 gráficos de comparación internacional (PNG)")
    print(f"   • 1 tabla comparativa Excel con rankings")
    print(f"   • 1 informe de posicionamiento (TXT)")
    print(f"   • 1 reporte de métricas de rendimiento (TXT)")
    print(f"   • {len(resultados)} rutas óptimas analizadas")
    print(f"\n⏱️  Tiempo total de procesamiento: {tiempo_total:.2f} segundos")
    
    # Mostrar estadísticas de métricas
    stats = logger.obtener_estadisticas()
    print(f"\n📈 Métricas de Rendimiento:")
    print(f"   • Total de operaciones: {stats['total_operaciones']}")
    print(f"   • Búsquedas realizadas: {stats['total_busquedas']}")
    print(f"   • Tiempo promedio por búsqueda: {stats['tiempo_promedio_busqueda_ms']:.2f} ms")
    print(f"   • Visualizaciones generadas: {stats['total_visualizaciones']}")
    
    print(f"\n🔝 Top 5 Estaciones Más Importantes:")
    for i, (estacion, score) in enumerate(ranking[:5], 1):
        print(f"   {i}. {estacion}: {score:.4f}")
    
    print(f"\n📈 Estadísticas de Rutas Analizadas:")
    distancia_promedio = sum(r['distancia'] for r in resultados) / len(resultados)
    paradas_promedio = sum(r['paradas'] for r in resultados) / len(resultados)
    print(f"   • Distancia promedio: {distancia_promedio:.2f} km")
    print(f"   • Paradas promedio: {paradas_promedio:.1f}")
    print(f"   • Ruta más corta: {min(resultados, key=lambda x: x['distancia'])['distancia']:.2f} km")
    print(f"   • Ruta más larga: {max(resultados, key=lambda x: x['distancia'])['distancia']:.2f} km")
    
    print("\n" + "="*60 + "\n")
    
    logger.logger.info(f"Análisis completo finalizado en {tiempo_total:.2f} segundos")
    logger.logger.info("="*60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error durante el análisis: {e}")
        import traceback
        traceback.print_exc()
