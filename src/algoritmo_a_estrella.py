# -*- coding: utf-8 -*-
"""
ALGORITMO A* - MOTOR DE BÚSQUEDA HEURÍSTICA
Implementa búsqueda informada para encontrar la ruta óptima
"""

import math
from queue import PriorityQueue

class NodoAStar:
    """Representa un nodo en el espacio de búsqueda"""
    
    def __init__(self, estacion, g, h, padre=None):
        self.estacion = estacion  # Nombre de la estación
        self.g = g  # Costo real desde el origen
        self.h = h  # Heurística (estimación al destino)
        self.f = g + h  # Función de evaluación
        self.padre = padre  # Nodo padre para reconstruir ruta
    
    def __lt__(self, otro):
        return self.f < otro.f


class AlgoritmoAEstrella:
    """Motor de búsqueda A* para encontrar rutas óptimas"""
    
    def __init__(self, base_conocimiento):
        self.base = base_conocimiento
    
    def calcular_heuristica(self, estacion_actual, estacion_destino):
        """
        HEURÍSTICA: Distancia euclidiana en coordenadas geográficas.
        Es admisible porque nunca sobreestima el costo real.
        """
        lat1, lon1 = self.base.obtener_coordenadas(estacion_actual)
        lat2, lon2 = self.base.obtener_coordenadas(estacion_destino)
        
        # Factor de conversión aproximado (1 grado ≈ 111 km)
        dx = (lon2 - lon1) * 111 * math.cos(math.radians(lat1))
        dy = (lat2 - lat1) * 111
        
        return math.sqrt(dx**2 + dy**2)
    
    def buscar_ruta(self, origen, destino):
        """
        ALGORITMO A*:
        1. Mantiene frontera (cola de prioridad) ordenada por f(n) = g(n) + h(n)
        2. Explora nodo con menor f(n)
        3. Expande vecinos y actualiza costos
        4. Termina al encontrar destino
        """
        
        if not self.base.validar_estacion(origen):
            return None, "Estación origen no existe"
        if not self.base.validar_estacion(destino):
            return None, "Estación destino no existe"
        
        if origen == destino:
            return [origen], 0, 0
        
        # Frontera: cola de prioridad ordenada por f
        frontera = PriorityQueue()
        h_inicial = self.calcular_heuristica(origen, destino)
        nodo_inicial = NodoAStar(origen, 0, h_inicial)
        frontera.put((nodo_inicial.f, id(nodo_inicial), nodo_inicial))
        
        # Conjuntos de exploración
        visitados = set()
        mejor_g = {origen: 0}
        
        while not frontera.empty():
            _, _, nodo_actual = frontera.get()
            
            if nodo_actual.estacion in visitados:
                continue
            
            # Marcar como visitado
            visitados.add(nodo_actual.estacion)
            
            # ¿Llegamos al destino?
            if nodo_actual.estacion == destino:
                return self._reconstruir_ruta(nodo_actual)
            
            # Expandir vecinos
            vecinos = self.base.obtener_vecinos(nodo_actual.estacion)
            
            for estacion_vecina, distancia, tiempo in vecinos:
                if estacion_vecina in visitados:
                    continue
                
                # Calcular nuevo costo g
                nuevo_g = nodo_actual.g + distancia
                
                # Si encontramos un camino mejor
                if estacion_vecina not in mejor_g or nuevo_g < mejor_g[estacion_vecina]:
                    mejor_g[estacion_vecina] = nuevo_g
                    h = self.calcular_heuristica(estacion_vecina, destino)
                    nodo_vecino = NodoAStar(estacion_vecina, nuevo_g, h, nodo_actual)
                    frontera.put((nodo_vecino.f, id(nodo_vecino), nodo_vecino))
        
        return None, "No se encontró ruta entre las estaciones"
    
    def _reconstruir_ruta(self, nodo_final):
        """Reconstruye la ruta desde el nodo final hacia el origen"""
        ruta = []
        costo_total = nodo_final.g
        nodo = nodo_final
        
        while nodo is not None:
            ruta.append(nodo.estacion)
            nodo = nodo.padre
        
        ruta.reverse()
        num_paradas = len(ruta) - 1
        
        return ruta, num_paradas, costo_total
