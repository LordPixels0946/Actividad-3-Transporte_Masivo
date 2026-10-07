# -*- coding: utf-8 -*-
"""
GENERADOR DE DATASET PARA APRENDIZAJE SUPERVISADO
Sistema de Transporte SETP Neiva
Predicción de demanda de pasajeros y clasificación de rutas
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuración de semilla para reproducibilidad
np.random.seed(42)
random.seed(42)


def generar_dataset_demanda():
    """
    Genera dataset de demanda de pasajeros en estaciones del SETP
    Variables:
    - Hora del día
    - Día de la semana
    - Estación
    - Condiciones climáticas
    - Evento especial
    - Demanda (target): Bajo, Medio, Alto
    """
    
    # Estaciones del SETP Neiva
    estaciones = [
        'Terminal', 'Estadio', 'San Mateo', 'Sevilla', 'La Toma',
        'Centro', 'Cándido', 'Calixto', 'Alcalá', 'Miraflores'
    ]
    
    # Generar datos para 6 meses (180 días)
    n_registros = 10000
    
    datos = []
    
    for i in range(n_registros):
        # Características
        hora = random.randint(5, 22)  # 5am - 10pm
        dia_semana = random.randint(0, 6)  # 0=Lunes, 6=Domingo
        estacion = random.choice(estaciones)
        clima = random.choice(['Soleado', 'Lluvioso', 'Nublado'])
        evento_especial = random.choice([0, 0, 0, 1])  # 25% eventos especiales
        temperatura = round(random.uniform(22, 35), 1)
        
        # Lógica para determinar demanda (clasificación)
        demanda_score = 0
        
        # Horas pico (6-8am, 12-2pm, 5-7pm)
        if hora in [6, 7, 8, 12, 13, 17, 18]:
            demanda_score += 3
        elif hora in [9, 10, 11, 14, 15, 16, 19]:
            demanda_score += 2
        else:
            demanda_score += 1
            
        # Días laborales tienen más demanda
        if dia_semana < 5:  # Lunes a Viernes
            demanda_score += 2
        else:
            demanda_score += 1
            
        # Estaciones clave
        if estacion in ['Terminal', 'Centro', 'Estadio']:
            demanda_score += 2
        else:
            demanda_score += 1
            
        # Clima afecta demanda
        if clima == 'Lluvioso':
            demanda_score += 2
        elif clima == 'Soleado':
            demanda_score += 1
            
        # Eventos especiales
        if evento_especial == 1:
            demanda_score += 3
            
        # Clasificación final
        if demanda_score <= 6:
            demanda = 'Baja'
            num_pasajeros = random.randint(10, 50)
        elif demanda_score <= 10:
            demanda = 'Media'
            num_pasajeros = random.randint(51, 150)
        else:
            demanda = 'Alta'
            num_pasajeros = random.randint(151, 300)
            
        # Agregar variabilidad realista
        num_pasajeros = int(num_pasajeros * random.uniform(0.8, 1.2))
        
        datos.append({
            'hora': hora,
            'dia_semana': dia_semana,
            'estacion': estacion,
            'clima': clima,
            'temperatura': temperatura,
            'evento_especial': evento_especial,
            'num_pasajeros': num_pasajeros,
            'demanda': demanda
        })
    
    df = pd.DataFrame(datos)
    return df


def generar_dataset_tiempos_viaje():
    """
    Genera dataset de tiempos de viaje entre estaciones
    Para regresión: predecir tiempo de viaje
    """
    
    rutas = [
        ('Terminal', 'Estadio', 15, 25),
        ('Terminal', 'Centro', 20, 30),
        ('Estadio', 'San Mateo', 10, 18),
        ('Centro', 'Sevilla', 12, 20),
        ('San Mateo', 'Sevilla', 8, 15),
        ('Sevilla', 'La Toma', 10, 16),
        ('Centro', 'Cándido', 15, 25),
        ('Cándido', 'Calixto', 12, 20),
        ('Calixto', 'Alcalá', 10, 18),
        ('Alcalá', 'Miraflores', 8, 14)
    ]
    
    n_registros = 5000
    datos = []
    
    for i in range(n_registros):
        origen, destino, tiempo_min, tiempo_max = random.choice(rutas)
        
        # Características
        hora = random.randint(5, 22)
        dia_semana = random.randint(0, 6)
        clima = random.choice(['Soleado', 'Lluvioso', 'Nublado'])
        trafico = random.choice(['Bajo', 'Medio', 'Alto'])
        num_paradas = random.randint(3, 10)
        
        # Calcular tiempo base
        tiempo_base = random.uniform(tiempo_min, tiempo_max)
        
        # Factores que afectan el tiempo
        if hora in [6, 7, 8, 12, 13, 17, 18]:  # Horas pico
            tiempo_base *= 1.4
        
        if dia_semana < 5:  # Días laborales
            tiempo_base *= 1.2
            
        if clima == 'Lluvioso':
            tiempo_base *= 1.3
            
        if trafico == 'Alto':
            tiempo_base *= 1.5
        elif trafico == 'Medio':
            tiempo_base *= 1.2
            
        # Agregar tiempo por paradas
        tiempo_base += num_paradas * random.uniform(0.5, 1.5)
        
        # Agregar variabilidad
        tiempo_final = round(tiempo_base * random.uniform(0.9, 1.1), 2)
        
        datos.append({
            'origen': origen,
            'destino': destino,
            'hora': hora,
            'dia_semana': dia_semana,
            'clima': clima,
            'trafico': trafico,
            'num_paradas': num_paradas,
            'tiempo_viaje_minutos': tiempo_final
        })
    
    df = pd.DataFrame(datos)
    return df


def main():
    """Genera los datasets y los guarda"""
    
    print("=" * 60)
    print("GENERADOR DE DATASETS - APRENDIZAJE SUPERVISADO")
    print("Sistema SETP Neiva")
    print("=" * 60)
    
    # Dataset 1: Clasificación de demanda
    print("\n1. Generando dataset de demanda de pasajeros...")
    df_demanda = generar_dataset_demanda()
    df_demanda.to_csv('data/dataset_demanda_pasajeros.csv', index=False, encoding='utf-8')
    print(f"   ✓ Generados {len(df_demanda)} registros")
    print(f"   ✓ Guardado en: data/dataset_demanda_pasajeros.csv")
    
    # Estadísticas
    print("\n   Distribución de demanda:")
    print(df_demanda['demanda'].value_counts())
    print(f"\n   Rango pasajeros: {df_demanda['num_pasajeros'].min()} - {df_demanda['num_pasajeros'].max()}")
    
    # Dataset 2: Regresión de tiempos de viaje
    print("\n2. Generando dataset de tiempos de viaje...")
    df_tiempos = generar_dataset_tiempos_viaje()
    df_tiempos.to_csv('data/dataset_tiempos_viaje.csv', index=False, encoding='utf-8')
    print(f"   ✓ Generados {len(df_tiempos)} registros")
    print(f"   ✓ Guardado en: data/dataset_tiempos_viaje.csv")
    
    # Estadísticas
    print("\n   Estadísticas de tiempos (minutos):")
    print(f"   - Promedio: {df_tiempos['tiempo_viaje_minutos'].mean():.2f}")
    print(f"   - Min: {df_tiempos['tiempo_viaje_minutos'].min():.2f}")
    print(f"   - Max: {df_tiempos['tiempo_viaje_minutos'].max():.2f}")
    
    print("\n" + "=" * 60)
    print("✓ DATASETS GENERADOS EXITOSAMENTE")
    print("=" * 60)
    

if __name__ == "__main__":
    main()
