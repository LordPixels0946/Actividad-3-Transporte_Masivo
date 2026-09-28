# -*- coding: utf-8 -*-
"""
VISUALIZADOR DE REDES Y RUTAS
Genera gráficos profesionales del sistema de transporte
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np
from datetime import datetime


class VisualizadorRed:
    """Genera visualizaciones de la red de transporte"""
    
    def __init__(self, base_conocimiento, output_dir='outputs'):
        self.base = base_conocimiento
        self.output_dir = output_dir
        self.grafo = self._crear_grafo()
        
        # Crear directorio de salida
        os.makedirs(output_dir, exist_ok=True)
        
        # Configurar estilo
        plt.style.use('seaborn-v0_8-darkgrid')
    
    def _crear_grafo(self):
        """Crea un grafo NetworkX desde la base de conocimiento"""
        G = nx.Graph()
        
        # Agregar nodos con atributos
        for estacion, coords in self.base.estaciones.items():
            G.add_node(estacion, 
                      lat=coords['lat'], 
                      lon=coords['lon'])
        
        # Agregar aristas con pesos
        for origen, destino, distancia, tiempo in self.base.conexiones:
            G.add_edge(origen, destino, 
                      weight=distancia, 
                      tiempo=tiempo)
        
        return G
    
    def visualizar_red_completa(self, filename='red_completa.png'):
        """Genera visualización de la red completa tipo mapa de tráfico"""
        plt.figure(figsize=(16, 12))
        
        # Usar coordenadas geográficas para posicionamiento
        pos = {nodo: (self.grafo.nodes[nodo]['lon'], 
                     self.grafo.nodes[nodo]['lat']) 
              for nodo in self.grafo.nodes()}
        
        # Dibujar aristas con grosor proporcional a importancia
        edge_weights = [self.grafo[u][v]['weight'] for u, v in self.grafo.edges()]
        max_weight = max(edge_weights)
        
        # Aristas
        nx.draw_networkx_edges(
            self.grafo, pos,
            width=[5 * (1 - w/max_weight) + 1 for w in edge_weights],
            alpha=0.6,
            edge_color='#2E86AB'
        )
        
        # Nodos
        nx.draw_networkx_nodes(
            self.grafo, pos,
            node_color='#A23B72',
            node_size=1500,
            alpha=0.9
        )
        
        # Etiquetas de nodos
        nx.draw_networkx_labels(
            self.grafo, pos,
            font_size=10,
            font_weight='bold',
            font_color='white'
        )
        
        # Etiquetas de distancias
        edge_labels = {(u, v): f"{self.grafo[u][v]['weight']} km"
                      for u, v in self.grafo.edges()}
        nx.draw_networkx_edge_labels(
            self.grafo, pos,
            edge_labels,
            font_size=8,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7)
        )
        
        plt.title('Red de Transporte SETP Neiva - Vista General', 
                 fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Longitud', fontsize=12)
        plt.ylabel('Latitud', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def visualizar_ruta(self, ruta, filename=None):
        """Resalta una ruta específica en el grafo"""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'ruta_{timestamp}.png'
        
        plt.figure(figsize=(16, 12))
        
        pos = {nodo: (self.grafo.nodes[nodo]['lon'], 
                     self.grafo.nodes[nodo]['lat']) 
              for nodo in self.grafo.nodes()}
        
        # Dibujar todas las aristas en gris claro
        nx.draw_networkx_edges(
            self.grafo, pos,
            width=2,
            alpha=0.3,
            edge_color='gray'
        )
        
        # Dibujar aristas de la ruta en rojo
        ruta_edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
        nx.draw_networkx_edges(
            self.grafo, pos,
            edgelist=ruta_edges,
            width=5,
            alpha=0.9,
            edge_color='#FF0054',
            arrows=True,
            arrowsize=20
        )
        
        # Todos los nodos en azul
        nx.draw_networkx_nodes(
            self.grafo, pos,
            node_color='#2E86AB',
            node_size=1000,
            alpha=0.7
        )
        
        # Nodos de la ruta en verde brillante
        nx.draw_networkx_nodes(
            self.grafo, pos,
            nodelist=ruta,
            node_color='#06FFA5',
            node_size=1500,
            alpha=1.0
        )
        
        # Nodo origen en amarillo
        nx.draw_networkx_nodes(
            self.grafo, pos,
            nodelist=[ruta[0]],
            node_color='#FFD700',
            node_size=2000,
            alpha=1.0
        )
        
        # Nodo destino en rojo
        nx.draw_networkx_nodes(
            self.grafo, pos,
            nodelist=[ruta[-1]],
            node_color='#FF0054',
            node_size=2000,
            alpha=1.0
        )
        
        # Etiquetas
        nx.draw_networkx_labels(
            self.grafo, pos,
            font_size=9,
            font_weight='bold',
            font_color='black'
        )
        
        # Leyenda
        origen_patch = mpatches.Patch(color='#FFD700', label='Origen')
        destino_patch = mpatches.Patch(color='#FF0054', label='Destino')
        ruta_patch = mpatches.Patch(color='#06FFA5', label='Ruta')
        plt.legend(handles=[origen_patch, ruta_patch, destino_patch], 
                  loc='upper right', fontsize=12)
        
        plt.title(f'Ruta Óptima: {ruta[0]} → {ruta[-1]}', 
                 fontsize=18, fontweight='bold', pad=20)
        plt.xlabel('Longitud', fontsize=12)
        plt.ylabel('Latitud', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def analisis_centralidad(self, filename='analisis_centralidad.png'):
        """Analiza y visualiza la centralidad de las estaciones"""
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        
        pos = {nodo: (self.grafo.nodes[nodo]['lon'], 
                     self.grafo.nodes[nodo]['lat']) 
              for nodo in self.grafo.nodes()}
        
        # 1. Centralidad de grado
        degree_centrality = nx.degree_centrality(self.grafo)
        node_colors_degree = [degree_centrality[node] for node in self.grafo.nodes()]
        
        ax1 = axes[0, 0]
        plt.sca(ax1)
        nx.draw_networkx_edges(self.grafo, pos, alpha=0.3, ax=ax1)
        nodes = nx.draw_networkx_nodes(
            self.grafo, pos,
            node_color=node_colors_degree,
            node_size=1500,
            cmap=plt.cm.Reds,
            ax=ax1
        )
        nx.draw_networkx_labels(self.grafo, pos, font_size=8, ax=ax1)
        ax1.set_title('Centralidad de Grado', fontsize=14, fontweight='bold')
        plt.colorbar(nodes, ax=ax1)
        
        # 2. Centralidad de intermediación
        betweenness_centrality = nx.betweenness_centrality(self.grafo, weight='weight')
        node_colors_between = [betweenness_centrality[node] for node in self.grafo.nodes()]
        
        ax2 = axes[0, 1]
        plt.sca(ax2)
        nx.draw_networkx_edges(self.grafo, pos, alpha=0.3, ax=ax2)
        nodes = nx.draw_networkx_nodes(
            self.grafo, pos,
            node_color=node_colors_between,
            node_size=1500,
            cmap=plt.cm.Greens,
            ax=ax2
        )
        nx.draw_networkx_labels(self.grafo, pos, font_size=8, ax=ax2)
        ax2.set_title('Centralidad de Intermediación', fontsize=14, fontweight='bold')
        plt.colorbar(nodes, ax=ax2)
        
        # 3. Centralidad de cercanía
        closeness_centrality = nx.closeness_centrality(self.grafo, distance='weight')
        node_colors_close = [closeness_centrality[node] for node in self.grafo.nodes()]
        
        ax3 = axes[1, 0]
        plt.sca(ax3)
        nx.draw_networkx_edges(self.grafo, pos, alpha=0.3, ax=ax3)
        nodes = nx.draw_networkx_nodes(
            self.grafo, pos,
            node_color=node_colors_close,
            node_size=1500,
            cmap=plt.cm.Blues,
            ax=ax3
        )
        nx.draw_networkx_labels(self.grafo, pos, font_size=8, ax=ax3)
        ax3.set_title('Centralidad de Cercanía', fontsize=14, fontweight='bold')
        plt.colorbar(nodes, ax=ax3)
        
        # 4. Ranking de estaciones más importantes
        ax4 = axes[1, 1]
        
        # Combinar métricas
        importancia = {}
        for node in self.grafo.nodes():
            importancia[node] = (
                degree_centrality[node] * 0.4 +
                betweenness_centrality[node] * 0.4 +
                closeness_centrality[node] * 0.2
            )
        
        sorted_nodes = sorted(importancia.items(), key=lambda x: x[1], reverse=True)
        nodes_names = [n[0] for n in sorted_nodes]
        nodes_scores = [n[1] for n in sorted_nodes]
        
        colors = plt.cm.viridis(np.linspace(0, 1, len(nodes_names)))
        ax4.barh(nodes_names, nodes_scores, color=colors)
        ax4.set_xlabel('Puntuación de Importancia', fontsize=12)
        ax4.set_title('Ranking de Estaciones por Importancia', fontsize=14, fontweight='bold')
        ax4.invert_yaxis()
        
        plt.suptitle('Análisis de Centralidad - Red SETP Neiva', 
                    fontsize=18, fontweight='bold', y=0.995)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath, sorted_nodes
    
    def grafico_comparativo_rutas(self, resultados, filename='comparativa_rutas.png'):
        """Genera gráfico comparativo de múltiples rutas"""
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        
        origenes = [r['origen'] for r in resultados]
        destinos = [r['destino'] for r in resultados]
        labels = [f"{o[:3]}-{d[:3]}" for o, d in zip(origenes, destinos)]
        distancias = [r['distancia'] for r in resultados]
        paradas = [r['paradas'] for r in resultados]
        tiempos = [r['tiempo_estimado'] for r in resultados]
        
        # Gráfico 1: Distancias
        ax1 = axes[0]
        bars1 = ax1.bar(labels, distancias, color='#2E86AB', alpha=0.8)
        ax1.set_ylabel('Distancia (km)', fontsize=12)
        ax1.set_title('Distancia por Ruta', fontsize=14, fontweight='bold')
        ax1.tick_params(axis='x', rotation=45)
        
        for bar, dist in zip(bars1, distancias):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{dist:.1f} km', ha='center', va='bottom', fontsize=9)
        
        # Gráfico 2: Número de paradas
        ax2 = axes[1]
        bars2 = ax2.bar(labels, paradas, color='#A23B72', alpha=0.8)
        ax2.set_ylabel('Número de Paradas', fontsize=12)
        ax2.set_title('Paradas por Ruta', fontsize=14, fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        
        for bar, par in zip(bars2, paradas):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{par}', ha='center', va='bottom', fontsize=9)
        
        # Gráfico 3: Tiempo estimado
        ax3 = axes[2]
        bars3 = ax3.bar(labels, tiempos, color='#06FFA5', alpha=0.8)
        ax3.set_ylabel('Tiempo (minutos)', fontsize=12)
        ax3.set_title('Tiempo Estimado por Ruta', fontsize=14, fontweight='bold')
        ax3.tick_params(axis='x', rotation=45)
        
        for bar, tiempo in zip(bars3, tiempos):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{tiempo} min', ha='center', va='bottom', fontsize=9)
        
        plt.suptitle('Análisis Comparativo de Rutas', fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def mapa_calor_conectividad(self, filename='mapa_calor_conectividad.png'):
        """Genera mapa de calor de conectividad entre estaciones"""
        estaciones = sorted(self.grafo.nodes())
        n = len(estaciones)
        matriz = np.zeros((n, n))
        
        # Calcular distancias más cortas entre todas las estaciones
        for i, origen in enumerate(estaciones):
            for j, destino in enumerate(estaciones):
                if i != j:
                    try:
                        distancia = nx.shortest_path_length(
                            self.grafo, origen, destino, weight='weight')
                        matriz[i][j] = distancia
                    except nx.NetworkXNoPath:
                        matriz[i][j] = np.inf
        
        # Crear mapa de calor
        plt.figure(figsize=(14, 12))
        
        # Reemplazar infinitos por valor máximo
        matriz[matriz == np.inf] = matriz[matriz != np.inf].max() * 1.5
        
        im = plt.imshow(matriz, cmap='YlOrRd', aspect='auto')
        plt.colorbar(im, label='Distancia (km)')
        
        # Configurar ejes
        plt.xticks(range(n), estaciones, rotation=45, ha='right')
        plt.yticks(range(n), estaciones)
        
        # Agregar valores en las celdas
        for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != matriz.max():
                    text = plt.text(j, i, f'{matriz[i][j]:.1f}',
                                  ha="center", va="center", 
                                  color="black", fontsize=8)
        
        plt.title('Mapa de Conectividad - Distancias entre Estaciones (km)', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Destino', fontsize=12)
        plt.ylabel('Origen', fontsize=12)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
