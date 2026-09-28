# -*- coding: utf-8 -*-
"""
BASE DE CONOCIMIENTO - SETP NEIVA
Contiene las estaciones y conexiones del Sistema Estratégico de Transporte Público
"""

class BaseConocimiento:
    """
    Representa la red de transporte con estaciones y conexiones.
    Implementa hechos lógicos como estructura de datos.
    """
    
    def __init__(self):
        # Coordenadas aproximadas (lat, lon) de estaciones reales de Neiva
        self.estaciones = {
            'Terminal': {'lat': 2.9273, 'lon': -75.2819},
            'Calle 7': {'lat': 2.9298, 'lon': -75.2850},
            'Centro': {'lat': 2.9342, 'lon': -75.2809},
            'Alcaldía': {'lat': 2.9356, 'lon': -75.2795},
            'Quirinal': {'lat': 2.9410, 'lon': -75.2880},
            'Limonar': {'lat': 2.9450, 'lon': -75.2920},
            'Gran Centro': {'lat': 2.9320, 'lon': -75.2770},
            'Calixto': {'lat': 2.9280, 'lon': -75.2740},
            'Estadio': {'lat': 2.9500, 'lon': -75.2850},
            'Cándido': {'lat': 2.9380, 'lon': -75.2730},
            'San Mateo': {'lat': 2.9240, 'lon': -75.2900},
            'Sevilla': {'lat': 2.9550, 'lon': -75.2800}
        }
        
        # Conexiones: (origen, destino, distancia_km, tiempo_min)
        self.conexiones = [
            ('Terminal', 'Calle 7', 1.2, 4),
            ('Terminal', 'San Mateo', 1.5, 5),
            ('Calle 7', 'Centro', 1.0, 3),
            ('Calle 7', 'Calixto', 1.8, 6),
            ('Centro', 'Alcaldía', 0.8, 2),
            ('Centro', 'Gran Centro', 0.9, 3),
            ('Alcaldía', 'Quirinal', 1.5, 5),
            ('Alcaldía', 'Cándido', 1.3, 4),
            ('Quirinal', 'Limonar', 1.1, 4),
            ('Quirinal', 'Estadio', 1.4, 5),
            ('Gran Centro', 'Calixto', 1.2, 4),
            ('Gran Centro', 'Cándido', 1.0, 3),
            ('Limonar', 'Estadio', 1.6, 5),
            ('Estadio', 'Sevilla', 1.3, 4),
            ('Cándido', 'Sevilla', 2.0, 7),
            ('Calixto', 'San Mateo', 1.4, 5),
        ]
    
    def obtener_estaciones(self):
        """Retorna lista de nombres de estaciones"""
        return list(self.estaciones.keys())
    
    def obtener_coordenadas(self, estacion):
        """Obtiene coordenadas de una estación"""
        if estacion in self.estaciones:
            return self.estaciones[estacion]['lat'], self.estaciones[estacion]['lon']
        return None, None
    
    def obtener_vecinos(self, estacion):
        """
        Retorna vecinos de una estación con sus costos.
        Las conexiones son bidireccionales.
        """
        vecinos = []
        for origen, destino, distancia, tiempo in self.conexiones:
            if origen == estacion:
                vecinos.append((destino, distancia, tiempo))
            elif destino == estacion:
                vecinos.append((origen, distancia, tiempo))
        return vecinos
    
    def validar_estacion(self, estacion):
        """Verifica si una estación existe en la red"""
        return estacion in self.estaciones
