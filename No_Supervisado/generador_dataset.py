# -*- coding: utf-8 -*-
"""
GENERADOR DE DATASET PARA APRENDIZAJE NO SUPERVISADO
Sistema de Transporte SETP Neiva
Clustering y análisis de patrones
"""

import pandas as pd
import numpy as np
import random

# Configuración de semilla para reproducibilidad
np.random.seed(42)
random.seed(42)


def generar_dataset_patrones_uso():
    """
    Genera dataset de patrones de uso de pasajeros
    Para clustering: identificar grupos de usuarios
    """
    
    n_usuarios = 2000
    
    datos = []
    
    for usuario_id in range(1, n_usuarios + 1):
        # Generar perfil de usuario
        tipo_usuario = random.choice(['Estudiante', 'Trabajador', 'Ocasional', 'Turista'])
        
        if tipo_usuario == 'Estudiante':
            # Estudiantes: uso frecuente en horarios escolares
            viajes_semana = random.randint(8, 12)
            hora_promedio = random.choice([7, 8, 13, 14, 17, 18])
            gasto_mensual = random.uniform(40000, 80000)
            rutas_favoritas = random.randint(2, 3)
            usa_fines_semana = random.choice([0, 0, 0, 1])
            
        elif tipo_usuario == 'Trabajador':
            # Trabajadores: uso regular y predecible
            viajes_semana = random.randint(10, 14)
            hora_promedio = random.choice([6, 7, 17, 18, 19])
            gasto_mensual = random.uniform(60000, 120000)
            rutas_favoritas = random.randint(1, 2)
            usa_fines_semana = random.choice([0, 0, 1])
            
        elif tipo_usuario == 'Ocasional':
            # Ocasionales: uso esporádico
            viajes_semana = random.randint(2, 5)
            hora_promedio = random.randint(9, 20)
            gasto_mensual = random.uniform(15000, 40000)
            rutas_favoritas = random.randint(3, 6)
            usa_fines_semana = random.choice([0, 1, 1])
            
        else:  # Turista
            # Turistas: uso variable y diverso
            viajes_semana = random.randint(3, 7)
            hora_promedio = random.randint(10, 18)
            gasto_mensual = random.uniform(20000, 60000)
            rutas_favoritas = random.randint(4, 8)
            usa_fines_semana = random.choice([1, 1, 1])
            
        # Agregar variabilidad
        viajes_semana = int(viajes_semana * random.uniform(0.8, 1.2))
        gasto_mensual = round(gasto_mensual * random.uniform(0.9, 1.1), 2)
        
        # Métricas adicionales
        tiempo_promedio_viaje = random.uniform(15, 45)
        distancia_promedio = random.uniform(3, 15)
        
        datos.append({
            'usuario_id': usuario_id,
            'viajes_por_semana': viajes_semana,
            'hora_promedio_uso': hora_promedio,
            'gasto_mensual': gasto_mensual,
            'numero_rutas_diferentes': rutas_favoritas,
            'usa_fines_semana': usa_fines_semana,
            'tiempo_promedio_viaje_min': round(tiempo_promedio_viaje, 2),
            'distancia_promedio_km': round(distancia_promedio, 2),
            'tipo_real': tipo_usuario  # Para validación (no se usa en clustering)
        })
    
    df = pd.DataFrame(datos)
    return df


def generar_dataset_estaciones():
    """
    Genera dataset de características de estaciones
    Para clustering: agrupar estaciones por similitud
    """
    
    estaciones = [
        'Terminal', 'Estadio', 'San Mateo', 'Sevilla', 'La Toma',
        'Centro', 'Cándido', 'Calixto', 'Alcalá', 'Miraflores',
        'Limonar', 'Cali', 'Granjas', 'Quirinal', 'Candelaria'
    ]
    
    datos = []
    
    for estacion in estaciones:
        # Generar características basadas en tipo de zona
        if estacion in ['Terminal', 'Centro', 'Estadio']:
            # Estaciones principales
            flujo_diario = random.randint(3000, 5000)
            conexiones = random.randint(8, 12)
            comercios_cercanos = random.randint(50, 100)
            zona_tipo = 'Principal'
            tarifa_promedio = random.uniform(2000, 2500)
            
        elif estacion in ['San Mateo', 'Sevilla', 'Cándido', 'Calixto']:
            # Estaciones intermedias
            flujo_diario = random.randint(1500, 3000)
            conexiones = random.randint(5, 8)
            comercios_cercanos = random.randint(20, 50)
            zona_tipo = 'Intermedia'
            tarifa_promedio = random.uniform(1800, 2300)
            
        else:
            # Estaciones secundarias
            flujo_diario = random.randint(500, 1500)
            conexiones = random.randint(3, 6)
            comercios_cercanos = random.randint(5, 20)
            zona_tipo = 'Secundaria'
            tarifa_promedio = random.uniform(1500, 2000)
            
        # Variabilidad
        flujo_diario = int(flujo_diario * random.uniform(0.9, 1.1))
        
        # Métricas adicionales
        tiempo_espera_promedio = random.uniform(3, 15)
        area_cobertura_km2 = random.uniform(0.5, 3.0)
        
        datos.append({
            'estacion': estacion,
            'flujo_pasajeros_diario': flujo_diario,
            'numero_conexiones': conexiones,
            'comercios_proximos': comercios_cercanos,
            'tiempo_espera_promedio_min': round(tiempo_espera_promedio, 2),
            'area_cobertura_km2': round(area_cobertura_km2, 2),
            'tarifa_promedio': round(tarifa_promedio, 2),
            'zona_tipo_real': zona_tipo  # Para validación
        })
    
    df = pd.DataFrame(datos)
    return df


def generar_dataset_rutas_frecuencias():
    """
    Genera dataset de rutas y sus frecuencias de uso
    Para análisis de componentes principales y clustering
    """
    
    rutas = [
        ('Terminal', 'Estadio'),
        ('Terminal', 'Centro'),
        ('Estadio', 'San Mateo'),
        ('Centro', 'Sevilla'),
        ('San Mateo', 'Sevilla'),
        ('Sevilla', 'La Toma'),
        ('Centro', 'Cándido'),
        ('Cándido', 'Calixto'),
        ('Calixto', 'Alcalá'),
        ('Alcalá', 'Miraflores'),
        ('Centro', 'Limonar'),
        ('Terminal', 'Granjas'),
        ('Estadio', 'Quirinal'),
        ('Centro', 'Candelaria'),
        ('Sevilla', 'Estadio')
    ]
    
    datos = []
    
    for origen, destino in rutas:
        # Generar datos para cada hora del día
        for hora in range(5, 23):  # 5am - 10pm
            # Uso basado en horarios pico
            if hora in [7, 8, 12, 13, 17, 18]:
                uso_base = random.randint(150, 300)
            elif hora in [6, 9, 11, 14, 16, 19]:
                uso_base = random.randint(80, 150)
            else:
                uso_base = random.randint(20, 80)
                
            # Factores adicionales
            ocupacion_promedio = random.uniform(0.4, 0.95)
            velocidad_promedio = random.uniform(25, 45)
            
            datos.append({
                'ruta_origen': origen,
                'ruta_destino': destino,
                'hora': hora,
                'pasajeros_hora': int(uso_base * random.uniform(0.9, 1.1)),
                'ocupacion_promedio': round(ocupacion_promedio, 3),
                'velocidad_promedio_kmh': round(velocidad_promedio, 2)
            })
    
    df = pd.DataFrame(datos)
    return df


def main():
    """Genera los datasets y los guarda"""
    
    print("=" * 60)
    print("GENERADOR DE DATASETS - APRENDIZAJE NO SUPERVISADO")
    print("Sistema SETP Neiva")
    print("=" * 60)
    
    # Dataset 1: Patrones de uso de usuarios
    print("\n1. Generando dataset de patrones de usuarios...")
    df_usuarios = generar_dataset_patrones_uso()
    df_usuarios.to_csv('data/dataset_patrones_usuarios.csv', index=False, encoding='utf-8')
    print(f"   ✓ Generados {len(df_usuarios)} usuarios")
    print(f"   ✓ Guardado en: data/dataset_patrones_usuarios.csv")
    
    print("\n   Distribución real de tipos (para validación):")
    print(df_usuarios['tipo_real'].value_counts())
    
    # Dataset 2: Características de estaciones
    print("\n2. Generando dataset de estaciones...")
    df_estaciones = generar_dataset_estaciones()
    df_estaciones.to_csv('data/dataset_estaciones.csv', index=False, encoding='utf-8')
    print(f"   ✓ Generadas {len(df_estaciones)} estaciones")
    print(f"   ✓ Guardado en: data/dataset_estaciones.csv")
    
    print("\n   Distribución por zona:")
    print(df_estaciones['zona_tipo_real'].value_counts())
    
    # Dataset 3: Rutas y frecuencias
    print("\n3. Generando dataset de rutas y frecuencias...")
    df_rutas = generar_dataset_rutas_frecuencias()
    df_rutas.to_csv('data/dataset_rutas_frecuencias.csv', index=False, encoding='utf-8')
    print(f"   ✓ Generados {len(df_rutas)} registros")
    print(f"   ✓ Guardado en: data/dataset_rutas_frecuencias.csv")
    
    print(f"\n   Total de rutas únicas: {df_rutas[['ruta_origen', 'ruta_destino']].drop_duplicates().shape[0]}")
    
    print("\n" + "=" * 60)
    print("✓ DATASETS GENERADOS EXITOSAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    main()
