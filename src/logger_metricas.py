# -*- coding: utf-8 -*-
"""
SISTEMA DE LOGGING Y MÉTRICAS
Registra operaciones y mide rendimiento del sistema
"""

import logging
import time
import json
import os
from datetime import datetime
from functools import wraps


class LoggerMetricas:
    """Gestiona logging y métricas de rendimiento"""
    
    def __init__(self, log_dir='outputs/logs'):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        
        # Configurar logging
        log_file = os.path.join(log_dir, f'setp_{datetime.now().strftime("%Y%m%d")}.log')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('SETP_Neiva')
        self.metricas = []
        self.metricas_file = os.path.join(log_dir, 'metricas.json')
        
        # Cargar métricas previas si existen
        self._cargar_metricas()
    
    def _cargar_metricas(self):
        """Carga métricas de sesiones anteriores"""
        if os.path.exists(self.metricas_file):
            try:
                with open(self.metricas_file, 'r', encoding='utf-8') as f:
                    self.metricas = json.load(f)
            except:
                self.metricas = []
    
    def _guardar_metricas(self):
        """Guarda métricas en archivo JSON"""
        with open(self.metricas_file, 'w', encoding='utf-8') as f:
            json.dump(self.metricas, f, indent=2, ensure_ascii=False)
    
    def registrar_busqueda(self, origen, destino, resultado, tiempo_ejecucion):
        """Registra una búsqueda de ruta"""
        metrica = {
            'tipo': 'busqueda_ruta',
            'timestamp': datetime.now().isoformat(),
            'origen': origen,
            'destino': destino,
            'exitosa': resultado[0] is not None,
            'tiempo_ejecucion_ms': round(tiempo_ejecucion * 1000, 2),
            'distancia': resultado[2] if resultado[0] else None,
            'paradas': resultado[1] if resultado[0] else None
        }
        
        self.metricas.append(metrica)
        self._guardar_metricas()
        
        self.logger.info(
            f"Búsqueda: {origen} → {destino} | "
            f"Exitosa: {metrica['exitosa']} | "
            f"Tiempo: {metrica['tiempo_ejecucion_ms']} ms"
        )
    
    def registrar_visualizacion(self, tipo, archivo, tiempo_ejecucion):
        """Registra generación de visualización"""
        metrica = {
            'tipo': 'visualizacion',
            'timestamp': datetime.now().isoformat(),
            'tipo_grafico': tipo,
            'archivo': archivo,
            'tiempo_ejecucion_ms': round(tiempo_ejecucion * 1000, 2)
        }
        
        self.metricas.append(metrica)
        self._guardar_metricas()
        
        self.logger.info(
            f"Visualización '{tipo}' generada | "
            f"Archivo: {archivo} | "
            f"Tiempo: {metrica['tiempo_ejecucion_ms']} ms"
        )
    
    def registrar_excel(self, archivo, tiempo_ejecucion, num_hojas):
        """Registra generación de reporte Excel"""
        metrica = {
            'tipo': 'reporte_excel',
            'timestamp': datetime.now().isoformat(),
            'archivo': archivo,
            'num_hojas': num_hojas,
            'tiempo_ejecucion_ms': round(tiempo_ejecucion * 1000, 2)
        }
        
        self.metricas.append(metrica)
        self._guardar_metricas()
        
        self.logger.info(
            f"Reporte Excel generado | "
            f"Archivo: {archivo} | "
            f"Hojas: {num_hojas} | "
            f"Tiempo: {metrica['tiempo_ejecucion_ms']} ms"
        )
    
    def obtener_estadisticas(self):
        """Obtiene estadísticas de uso del sistema"""
        if not self.metricas:
            return {}
        
        busquedas = [m for m in self.metricas if m['tipo'] == 'busqueda_ruta']
        visualizaciones = [m for m in self.metricas if m['tipo'] == 'visualizacion']
        reportes = [m for m in self.metricas if m['tipo'] == 'reporte_excel']
        
        stats = {
            'total_operaciones': len(self.metricas),
            'total_busquedas': len(busquedas),
            'busquedas_exitosas': sum(1 for b in busquedas if b['exitosa']),
            'total_visualizaciones': len(visualizaciones),
            'total_reportes': len(reportes),
            'tiempo_promedio_busqueda_ms': (
                sum(b['tiempo_ejecucion_ms'] for b in busquedas) / len(busquedas)
                if busquedas else 0
            ),
            'tiempo_promedio_visualizacion_ms': (
                sum(v['tiempo_ejecucion_ms'] for v in visualizaciones) / len(visualizaciones)
                if visualizaciones else 0
            )
        }
        
        return stats
    
    def generar_reporte_metricas(self, filename='reporte_metricas.txt'):
        """Genera reporte de texto con métricas"""
        stats = self.obtener_estadisticas()
        filepath = os.path.join(self.log_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("  REPORTE DE MÉTRICAS - SISTEMA SETP NEIVA\n")
            f.write("="*60 + "\n\n")
            
            f.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("ESTADÍSTICAS GENERALES:\n")
            f.write("-"*60 + "\n")
            f.write(f"Total de operaciones: {stats.get('total_operaciones', 0)}\n")
            f.write(f"Total de búsquedas: {stats.get('total_busquedas', 0)}\n")
            f.write(f"Búsquedas exitosas: {stats.get('busquedas_exitosas', 0)}\n")
            f.write(f"Total de visualizaciones: {stats.get('total_visualizaciones', 0)}\n")
            f.write(f"Total de reportes Excel: {stats.get('total_reportes', 0)}\n\n")
            
            f.write("RENDIMIENTO:\n")
            f.write("-"*60 + "\n")
            f.write(f"Tiempo promedio de búsqueda: {stats.get('tiempo_promedio_busqueda_ms', 0):.2f} ms\n")
            f.write(f"Tiempo promedio de visualización: {stats.get('tiempo_promedio_visualizacion_ms', 0):.2f} ms\n\n")
            
            # Últimas 10 operaciones
            f.write("ÚLTIMAS 10 OPERACIONES:\n")
            f.write("-"*60 + "\n")
            for metrica in self.metricas[-10:]:
                f.write(f"{metrica['timestamp']} - {metrica['tipo']}\n")
            
            f.write("\n" + "="*60 + "\n")
        
        return filepath


def medir_tiempo(logger_metricas=None, tipo_operacion='operacion'):
    """Decorador para medir tiempo de ejecución"""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            tiempo_ejecucion = time.time() - inicio
            
            if logger_metricas:
                logger_metricas.logger.info(
                    f"{tipo_operacion} '{func.__name__}' completada en {tiempo_ejecucion*1000:.2f} ms"
                )
            
            return resultado
        return wrapper
    return decorador
