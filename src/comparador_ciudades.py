# -*- coding: utf-8 -*-
"""
COMPARADOR DE SISTEMAS DE TRANSPORTE
Compara SETP Neiva con sistemas de otras ciudades
"""

import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime


class ComparadorCiudades:
    """Compara características de sistemas de transporte de diferentes ciudades"""
    
    def __init__(self, output_dir='outputs'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Datos de sistemas de transporte de diferentes ciudades
        # Basado en información pública de sistemas BRT y transporte masivo
        self.sistemas = {
            'Neiva (SETP)': {
                'pais': 'Colombia',
                'estaciones': 12,
                'conexiones': 16,
                'distancia_red_km': 35.2,
                'poblacion_ciudad': 350000,
                'año_inicio': 2013,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 25
            },
            'Bogotá (TransMilenio)': {
                'pais': 'Colombia',
                'estaciones': 139,
                'conexiones': 200,
                'distancia_red_km': 114.4,
                'poblacion_ciudad': 7900000,
                'año_inicio': 2000,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 26
            },
            'Medellín (Metro)': {
                'pais': 'Colombia',
                'estaciones': 31,
                'conexiones': 45,
                'distancia_red_km': 43.4,
                'poblacion_ciudad': 2500000,
                'año_inicio': 1995,
                'tipo': 'Metro',
                'velocidad_promedio_kmh': 35
            },
            'Cali (MIO)': {
                'pais': 'Colombia',
                'estaciones': 60,
                'conexiones': 85,
                'distancia_red_km': 50.2,
                'poblacion_ciudad': 2250000,
                'año_inicio': 2008,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 23
            },
            'Curitiba (RIT)': {
                'pais': 'Brasil',
                'estaciones': 340,
                'conexiones': 450,
                'distancia_red_km': 81,
                'poblacion_ciudad': 1900000,
                'año_inicio': 1974,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 28
            },
            'Ciudad de México (Metrobús)': {
                'pais': 'México',
                'estaciones': 200,
                'conexiones': 280,
                'distancia_red_km': 140,
                'poblacion_ciudad': 9200000,
                'año_inicio': 2005,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 27
            },
            'Lima (Metropolitano)': {
                'pais': 'Perú',
                'estaciones': 38,
                'conexiones': 52,
                'distancia_red_km': 26,
                'poblacion_ciudad': 10000000,
                'año_inicio': 2010,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 24
            },
            'Santiago (Transantiago)': {
                'pais': 'Chile',
                'estaciones': 136,
                'conexiones': 195,
                'distancia_red_km': 103,
                'poblacion_ciudad': 6100000,
                'año_inicio': 2007,
                'tipo': 'BRT',
                'velocidad_promedio_kmh': 29
            }
        }
    
    def generar_comparativa_grafica(self, filename='comparativa_ciudades.png'):
        """Genera gráficos comparativos entre ciudades"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))
        fig.suptitle('Comparación de Sistemas de Transporte Masivo - Latinoamérica', 
                    fontsize=18, fontweight='bold', y=0.995)
        
        ciudades = list(self.sistemas.keys())
        
        # Colores: Neiva en color destacado
        colores = ['#FF0054' if 'Neiva' in c else '#2E86AB' for c in ciudades]
        
        # 1. Número de estaciones
        ax1 = axes[0, 0]
        estaciones = [self.sistemas[c]['estaciones'] for c in ciudades]
        bars1 = ax1.barh(ciudades, estaciones, color=colores, alpha=0.8)
        ax1.set_xlabel('Número de Estaciones', fontsize=11)
        ax1.set_title('Estaciones por Sistema', fontsize=13, fontweight='bold')
        for i, (bar, val) in enumerate(zip(bars1, estaciones)):
            ax1.text(val, i, f' {val}', va='center', fontsize=9)
        
        # 2. Distancia de red
        ax2 = axes[0, 1]
        distancias = [self.sistemas[c]['distancia_red_km'] for c in ciudades]
        bars2 = ax2.barh(ciudades, distancias, color=colores, alpha=0.8)
        ax2.set_xlabel('Distancia Total (km)', fontsize=11)
        ax2.set_title('Extensión de la Red', fontsize=13, fontweight='bold')
        for i, (bar, val) in enumerate(zip(bars2, distancias)):
            ax2.text(val, i, f' {val} km', va='center', fontsize=9)
        
        # 3. Velocidad promedio
        ax3 = axes[0, 2]
        velocidades = [self.sistemas[c]['velocidad_promedio_kmh'] for c in ciudades]
        bars3 = ax3.barh(ciudades, velocidades, color=colores, alpha=0.8)
        ax3.set_xlabel('Velocidad (km/h)', fontsize=11)
        ax3.set_title('Velocidad Promedio', fontsize=13, fontweight='bold')
        for i, (bar, val) in enumerate(zip(bars3, velocidades)):
            ax3.text(val, i, f' {val} km/h', va='center', fontsize=9)
        
        # 4. Población vs Estaciones (scatter)
        ax4 = axes[1, 0]
        poblaciones = [self.sistemas[c]['poblacion_ciudad']/1000000 for c in ciudades]
        ax4.scatter(poblaciones, estaciones, s=[200 if 'Neiva' in c else 100 for c in ciudades],
                   c=colores, alpha=0.7)
        for i, ciudad in enumerate(ciudades):
            label = 'Neiva' if 'Neiva' in ciudad else ciudad.split('(')[0].strip()
            ax4.annotate(label, (poblaciones[i], estaciones[i]), 
                        fontsize=8, ha='right')
        ax4.set_xlabel('Población (millones)', fontsize=11)
        ax4.set_ylabel('Estaciones', fontsize=11)
        ax4.set_title('Relación Población - Estaciones', fontsize=13, fontweight='bold')
        ax4.grid(True, alpha=0.3)
        
        # 5. Distribución por tipo de sistema
        ax5 = axes[1, 1]
        tipos = {}
        for ciudad, datos in self.sistemas.items():
            tipo = datos['tipo']
            tipos[tipo] = tipos.get(tipo, 0) + 1
        
        wedges, texts, autotexts = ax5.pie(
            tipos.values(), 
            labels=tipos.keys(),
            autopct='%1.1f%%',
            colors=['#2E86AB', '#A23B72', '#06FFA5'],
            startangle=90
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        ax5.set_title('Distribución por Tipo de Sistema', fontsize=13, fontweight='bold')
        
        # 6. Línea de tiempo
        ax6 = axes[1, 2]
        años = [self.sistemas[c]['año_inicio'] for c in ciudades]
        ax6.barh(ciudades, años, color=colores, alpha=0.8)
        ax6.set_xlabel('Año de Inicio', fontsize=11)
        ax6.set_title('Año de Inicio de Operaciones', fontsize=13, fontweight='bold')
        ax6.set_xlim(1970, 2025)
        for i, (bar, val) in enumerate(zip(ciudades, años)):
            ax6.text(val, i, f' {val}', va='center', fontsize=9)
        
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def generar_tabla_comparativa(self, filename='tabla_comparativa.xlsx'):
        """Genera tabla Excel con comparación detallada"""
        # Convertir a DataFrame
        df = pd.DataFrame(self.sistemas).T
        df.index.name = 'Ciudad (Sistema)'
        
        # Calcular métricas adicionales
        df['estaciones_por_millon_habitantes'] = (
            df['estaciones'] / (df['poblacion_ciudad'] / 1000000)
        ).round(2)
        
        df['km_por_millon_habitantes'] = (
            df['distancia_red_km'] / (df['poblacion_ciudad'] / 1000000)
        ).round(2)
        
        df['antiguedad_años'] = datetime.now().year - df['año_inicio']
        
        # Reordenar columnas
        columnas_ordenadas = [
            'pais', 'poblacion_ciudad', 'tipo', 'año_inicio', 'antiguedad_años',
            'estaciones', 'conexiones', 'distancia_red_km', 
            'velocidad_promedio_kmh', 'estaciones_por_millon_habitantes',
            'km_por_millon_habitantes'
        ]
        
        df = df[columnas_ordenadas]
        
        # Renombrar columnas para mejor presentación
        df.columns = [
            'País', 'Población Ciudad', 'Tipo Sistema', 'Año Inicio', 'Antigüedad (años)',
            'Estaciones', 'Conexiones', 'Distancia Red (km)', 
            'Velocidad Promedio (km/h)', 'Estaciones por Millón Hab.',
            'Km Red por Millón Hab.'
        ]
        
        # Ordenar por población
        df = df.sort_values('Población Ciudad', ascending=False)
        
        # Guardar en Excel
        filepath = os.path.join(self.output_dir, filename)
        
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Comparativa General')
            
            # Hoja de rankings
            rankings = pd.DataFrame({
                'Mayor Número de Estaciones': df.nlargest(5, 'Estaciones').index.tolist(),
                'Mayor Extensión de Red': df.nlargest(5, 'Distancia Red (km)').index.tolist(),
                'Mayor Velocidad': df.nlargest(5, 'Velocidad Promedio (km/h)').index.tolist(),
                'Más Antiguo': df.nlargest(5, 'Antigüedad (años)').index.tolist()
            })
            rankings.to_excel(writer, sheet_name='Rankings', index=False)
            
            # Hoja de análisis de Neiva
            neiva_data = df.loc[df.index.str.contains('Neiva')]
            promedio_brt = df[df['Tipo Sistema'] == 'BRT'].mean(numeric_only=True)
            
            comparacion_neiva = pd.DataFrame({
                'Métrica': neiva_data.columns,
                'Neiva': neiva_data.iloc[0].values,
                'Promedio BRT Latinoamérica': ['Colombia', '-', 'BRT', '-', '-'] + 
                                               promedio_brt.tolist()
            })
            comparacion_neiva.to_excel(writer, sheet_name='Análisis Neiva', index=False)
        
        return filepath
    
    def generar_informe_posicionamiento(self, filename='informe_posicionamiento.txt'):
        """Genera informe de texto sobre posicionamiento de Neiva"""
        filepath = os.path.join(self.output_dir, filename)
        
        df = pd.DataFrame(self.sistemas).T
        neiva = df.loc['Neiva (SETP)']
        brt_sistemas = df[df['tipo'] == 'BRT']
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("  INFORME DE POSICIONAMIENTO - SETP NEIVA\n")
            f.write("  Comparación con Sistemas BRT de Latinoamérica\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("1. CARACTERÍSTICAS DEL SETP NEIVA:\n")
            f.write("-"*70 + "\n")
            f.write(f"   • Estaciones: {neiva['estaciones']}\n")
            f.write(f"   • Distancia de red: {neiva['distancia_red_km']} km\n")
            f.write(f"   • Velocidad promedio: {neiva['velocidad_promedio_kmh']} km/h\n")
            f.write(f"   • Población atendida: {neiva['poblacion_ciudad']:,} habitantes\n")
            f.write(f"   • Años de operación: {datetime.now().year - neiva['año_inicio']}\n\n")
            
            f.write("2. COMPARACIÓN CON PROMEDIO BRT LATINOAMÉRICA:\n")
            f.write("-"*70 + "\n")
            
            promedio_estaciones = brt_sistemas['estaciones'].mean()
            promedio_distancia = brt_sistemas['distancia_red_km'].mean()
            promedio_velocidad = brt_sistemas['velocidad_promedio_kmh'].mean()
            
            f.write(f"   Estaciones:\n")
            f.write(f"      Neiva: {neiva['estaciones']} | ")
            f.write(f"Promedio: {promedio_estaciones:.1f} | ")
            f.write(f"Diferencia: {((neiva['estaciones']/promedio_estaciones - 1) * 100):.1f}%\n\n")
            
            f.write(f"   Distancia de Red:\n")
            f.write(f"      Neiva: {neiva['distancia_red_km']} km | ")
            f.write(f"Promedio: {promedio_distancia:.1f} km | ")
            f.write(f"Diferencia: {((neiva['distancia_red_km']/promedio_distancia - 1) * 100):.1f}%\n\n")
            
            f.write(f"   Velocidad Promedio:\n")
            f.write(f"      Neiva: {neiva['velocidad_promedio_kmh']} km/h | ")
            f.write(f"Promedio: {promedio_velocidad:.1f} km/h | ")
            f.write(f"Diferencia: {((neiva['velocidad_promedio_kmh']/promedio_velocidad - 1) * 100):.1f}%\n\n")
            
            f.write("3. POSICIÓN EN RANKINGS:\n")
            f.write("-"*70 + "\n")
            
            rank_estaciones = (df['estaciones'] > neiva['estaciones']).sum() + 1
            rank_distancia = (df['distancia_red_km'] > neiva['distancia_red_km']).sum() + 1
            rank_velocidad = (df['velocidad_promedio_kmh'] > neiva['velocidad_promedio_kmh']).sum() + 1
            
            total_sistemas = len(df)
            
            f.write(f"   • Estaciones: Posición {rank_estaciones} de {total_sistemas}\n")
            f.write(f"   • Extensión de red: Posición {rank_distancia} de {total_sistemas}\n")
            f.write(f"   • Velocidad: Posición {rank_velocidad} de {total_sistemas}\n\n")
            
            f.write("4. CONCLUSIONES:\n")
            f.write("-"*70 + "\n")
            f.write(f"   SETP Neiva es un sistema de transporte BRT en fase de consolidación,\n")
            f.write(f"   apropiado para el tamaño de la ciudad ({neiva['poblacion_ciudad']:,} habitantes).\n")
            f.write(f"   Comparado con sistemas BRT de ciudades más grandes, cuenta con una red\n")
            f.write(f"   más compacta pero funcional para las necesidades locales.\n\n")
            
            f.write("="*70 + "\n")
        
        return filepath
