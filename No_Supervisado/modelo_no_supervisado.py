# -*- coding: utf-8 -*-
"""
MODELOS DE APRENDIZAJE NO SUPERVISADO - SETP NEIVA
Implementa:
1. K-Means Clustering: Segmentación de usuarios y estaciones
2. DBSCAN: Detección de patrones anómalos
3. PCA: Reducción de dimensionalidad y visualización
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score
from scipy.cluster.hierarchy import dendrogram, linkage
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)


class ClusteringUsuarios:
    """Clustering de usuarios del sistema SETP"""
    
    def __init__(self, ruta_dataset='data/dataset_patrones_usuarios.csv'):
        self.ruta_dataset = ruta_dataset
        self.df = None
        self.X_scaled = None
        self.scaler = None
        self.modelo_kmeans = None
        self.modelo_dbscan = None
        self.pca = None
        
    def cargar_datos(self):
        """Carga los datos"""
        print("\n📊 Cargando dataset de usuarios...")
        self.df = pd.read_csv(self.ruta_dataset)
        print(f"   ✓ Dataset cargado: {len(self.df)} usuarios")
        
    def preprocesar_datos(self):
        """Normaliza los datos para clustering"""
        print("\n🔧 Preprocesando y normalizando datos...")
        
        # Seleccionar features (sin la etiqueta real)
        features = ['viajes_por_semana', 'hora_promedio_uso', 'gasto_mensual',
                   'numero_rutas_diferentes', 'usa_fines_semana', 
                   'tiempo_promedio_viaje_min', 'distancia_promedio_km']
        
        X = self.df[features]
        
        # Normalizar
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(X)
        
        print(f"   ✓ Features normalizadas: {len(features)}")
        
    def encontrar_k_optimo(self):
        """Encuentra el número óptimo de clusters con método del codo"""
        print("\n📊 Determinando número óptimo de clusters...")
        
        inertias = []
        silhouette_scores = []
        K_range = range(2, 11)
        
        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(self.X_scaled)
            inertias.append(kmeans.inertia_)
            silhouette_scores.append(silhouette_score(self.X_scaled, kmeans.labels_))
        
        # Visualizar método del codo
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        axes[0].plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
        axes[0].set_xlabel('Número de Clusters (k)')
        axes[0].set_ylabel('Inercia')
        axes[0].set_title('Método del Codo', fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(K_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
        axes[1].set_xlabel('Número de Clusters (k)')
        axes[1].set_ylabel('Silhouette Score')
        axes[1].set_title('Análisis de Silhouette', fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle('Determinación de k Óptimo - Clustering de Usuarios SETP', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/optimizacion_k_usuarios.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/optimizacion_k_usuarios.png")
        plt.close()
        
        # Retornar k óptimo (basado en silhouette)
        k_optimo = K_range[np.argmax(silhouette_scores)]
        print(f"   ✓ K óptimo sugerido: {k_optimo}")
        return k_optimo
        
    def aplicar_kmeans(self, n_clusters=4):
        """Aplica K-Means clustering"""
        print(f"\n🎯 Aplicando K-Means con {n_clusters} clusters...")
        
        self.modelo_kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.df['cluster_kmeans'] = self.modelo_kmeans.fit_predict(self.X_scaled)
        
        # Métricas
        silhouette = silhouette_score(self.X_scaled, self.df['cluster_kmeans'])
        davies_bouldin = davies_bouldin_score(self.X_scaled, self.df['cluster_kmeans'])
        
        print(f"   ✓ Silhouette Score: {silhouette:.4f}")
        print(f"   ✓ Davies-Bouldin Index: {davies_bouldin:.4f}")
        
        print("\n   Distribución de usuarios por cluster:")
        print(self.df['cluster_kmeans'].value_counts().sort_index())
        
        return silhouette
        
    def aplicar_dbscan(self, eps=0.5, min_samples=10):
        """Aplica DBSCAN clustering"""
        print(f"\n🔍 Aplicando DBSCAN (eps={eps}, min_samples={min_samples})...")
        
        self.modelo_dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        self.df['cluster_dbscan'] = self.modelo_dbscan.fit_predict(self.X_scaled)
        
        n_clusters = len(set(self.df['cluster_dbscan'])) - (1 if -1 in self.df['cluster_dbscan'] else 0)
        n_noise = list(self.df['cluster_dbscan']).count(-1)
        
        print(f"   ✓ Clusters encontrados: {n_clusters}")
        print(f"   ✓ Puntos de ruido: {n_noise}")
        
        if n_clusters > 1:
            # Solo calcular si hay más de 1 cluster
            mask = self.df['cluster_dbscan'] != -1
            if mask.sum() > 0:
                silhouette = silhouette_score(self.X_scaled[mask], self.df.loc[mask, 'cluster_dbscan'])
                print(f"   ✓ Silhouette Score: {silhouette:.4f}")
        
    def aplicar_pca(self):
        """Aplica PCA para visualización"""
        print("\n📉 Aplicando PCA para visualización 2D...")
        
        self.pca = PCA(n_components=2)
        X_pca = self.pca.fit_transform(self.X_scaled)
        
        self.df['pca_1'] = X_pca[:, 0]
        self.df['pca_2'] = X_pca[:, 1]
        
        varianza_explicada = self.pca.explained_variance_ratio_
        print(f"   ✓ Varianza explicada PC1: {varianza_explicada[0]:.2%}")
        print(f"   ✓ Varianza explicada PC2: {varianza_explicada[1]:.2%}")
        print(f"   ✓ Varianza total: {sum(varianza_explicada):.2%}")
        
    def visualizar_clusters_pca(self):
        """Visualiza clusters en espacio PCA"""
        print("\n📊 Generando visualización de clusters...")
        
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # K-Means
        scatter1 = axes[0].scatter(self.df['pca_1'], self.df['pca_2'], 
                                   c=self.df['cluster_kmeans'], 
                                   cmap='viridis', alpha=0.6, s=50)
        axes[0].set_xlabel(f'PC1 ({self.pca.explained_variance_ratio_[0]:.1%})')
        axes[0].set_ylabel(f'PC2 ({self.pca.explained_variance_ratio_[1]:.1%})')
        axes[0].set_title('K-Means Clustering', fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        plt.colorbar(scatter1, ax=axes[0], label='Cluster')
        
        # DBSCAN
        scatter2 = axes[1].scatter(self.df['pca_1'], self.df['pca_2'], 
                                   c=self.df['cluster_dbscan'], 
                                   cmap='plasma', alpha=0.6, s=50)
        axes[1].set_xlabel(f'PC1 ({self.pca.explained_variance_ratio_[0]:.1%})')
        axes[1].set_ylabel(f'PC2 ({self.pca.explained_variance_ratio_[1]:.1%})')
        axes[1].set_title('DBSCAN Clustering', fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        plt.colorbar(scatter2, ax=axes[1], label='Cluster')
        
        plt.suptitle('Clustering de Usuarios SETP - Proyección PCA', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/clusters_usuarios_pca.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/clusters_usuarios_pca.png")
        plt.close()
        
    def analizar_perfiles_clusters(self):
        """Analiza características de cada cluster"""
        print("\n📊 Analizando perfiles de clusters...")
        
        # Características promedio por cluster
        features = ['viajes_por_semana', 'hora_promedio_uso', 'gasto_mensual',
                   'numero_rutas_diferentes', 'tiempo_promedio_viaje_min']
        
        perfiles = self.df.groupby('cluster_kmeans')[features].mean()
        
        # Visualizar perfiles
        fig, axes = plt.subplots(2, 3, figsize=(16, 10))
        axes = axes.flatten()
        
        for idx, feature in enumerate(features):
            perfiles[feature].plot(kind='bar', ax=axes[idx], color='steelblue')
            axes[idx].set_title(feature.replace('_', ' ').title(), fontweight='bold')
            axes[idx].set_xlabel('Cluster')
            axes[idx].set_ylabel('Valor Promedio')
            axes[idx].grid(axis='y', alpha=0.3)
            
        # Eliminar el subplot extra
        fig.delaxes(axes[5])
        
        plt.suptitle('Perfiles de Clusters - Usuarios SETP', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/perfiles_clusters_usuarios.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/perfiles_clusters_usuarios.png")
        plt.close()
        
        # Comparar con tipos reales
        print("\n   Comparación con tipos reales:")
        comparacion = pd.crosstab(self.df['tipo_real'], self.df['cluster_kmeans'])
        print(comparacion)
        

class ClusteringEstaciones:
    """Clustering de estaciones del sistema SETP"""
    
    def __init__(self, ruta_dataset='data/dataset_estaciones.csv'):
        self.ruta_dataset = ruta_dataset
        self.df = None
        self.X_scaled = None
        self.scaler = None
        
    def cargar_datos(self):
        """Carga los datos"""
        print("\n📊 Cargando dataset de estaciones...")
        self.df = pd.read_csv(self.ruta_dataset)
        print(f"   ✓ Dataset cargado: {len(self.df)} estaciones")
        
    def preprocesar_datos(self):
        """Normaliza los datos"""
        print("\n🔧 Preprocesando datos...")
        
        features = ['flujo_pasajeros_diario', 'numero_conexiones', 
                   'comercios_proximos', 'tiempo_espera_promedio_min',
                   'area_cobertura_km2', 'tarifa_promedio']
        
        X = self.df[features]
        
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(X)
        
        print(f"   ✓ Features normalizadas: {len(features)}")
        
    def aplicar_clustering_jerarquico(self):
        """Aplica clustering jerárquico"""
        print("\n🌳 Aplicando Clustering Jerárquico...")
        
        # Calcular linkage
        linkage_matrix = linkage(self.X_scaled, method='ward')
        
        # Visualizar dendrograma
        plt.figure(figsize=(14, 7))
        dendrogram(linkage_matrix, labels=self.df['estacion'].values, 
                  leaf_font_size=10)
        plt.title('Dendrograma - Clustering Jerárquico de Estaciones SETP', 
                 fontsize=14, fontweight='bold')
        plt.xlabel('Estación')
        plt.ylabel('Distancia')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('outputs/dendrograma_estaciones.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/dendrograma_estaciones.png")
        plt.close()
        
    def aplicar_kmeans_estaciones(self, n_clusters=3):
        """Aplica K-Means a estaciones"""
        print(f"\n🎯 Aplicando K-Means con {n_clusters} clusters...")
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.df['cluster'] = kmeans.fit_predict(self.X_scaled)
        
        silhouette = silhouette_score(self.X_scaled, self.df['cluster'])
        print(f"   ✓ Silhouette Score: {silhouette:.4f}")
        
        print("\n   Estaciones por cluster:")
        for cluster_id in range(n_clusters):
            estaciones = self.df[self.df['cluster'] == cluster_id]['estacion'].tolist()
            print(f"   Cluster {cluster_id}: {', '.join(estaciones)}")
            
    def visualizar_caracteristicas_estaciones(self):
        """Visualiza características principales de estaciones"""
        print("\n📊 Generando visualizaciones de estaciones...")
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Flujo de pasajeros
        self.df.sort_values('flujo_pasajeros_diario', ascending=True).plot(
            x='estacion', y='flujo_pasajeros_diario', kind='barh', 
            ax=axes[0, 0], color=plt.cm.viridis(self.df['cluster']/self.df['cluster'].max()),
            legend=False
        )
        axes[0, 0].set_title('Flujo de Pasajeros Diario', fontweight='bold')
        axes[0, 0].set_xlabel('Pasajeros/día')
        
        # Número de conexiones
        self.df.sort_values('numero_conexiones', ascending=True).plot(
            x='estacion', y='numero_conexiones', kind='barh', 
            ax=axes[0, 1], color=plt.cm.plasma(self.df['cluster']/self.df['cluster'].max()),
            legend=False
        )
        axes[0, 1].set_title('Número de Conexiones', fontweight='bold')
        axes[0, 1].set_xlabel('Conexiones')
        
        # Comercios próximos
        self.df.sort_values('comercios_proximos', ascending=True).plot(
            x='estacion', y='comercios_proximos', kind='barh', 
            ax=axes[1, 0], color=plt.cm.coolwarm(self.df['cluster']/self.df['cluster'].max()),
            legend=False
        )
        axes[1, 0].set_title('Comercios Próximos', fontweight='bold')
        axes[1, 0].set_xlabel('Número de comercios')
        
        # Tiempo de espera
        self.df.sort_values('tiempo_espera_promedio_min', ascending=True).plot(
            x='estacion', y='tiempo_espera_promedio_min', kind='barh', 
            ax=axes[1, 1], color=plt.cm.RdYlGn_r(self.df['cluster']/self.df['cluster'].max()),
            legend=False
        )
        axes[1, 1].set_title('Tiempo de Espera Promedio', fontweight='bold')
        axes[1, 1].set_xlabel('Minutos')
        
        plt.suptitle('Características de Estaciones SETP por Cluster', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/caracteristicas_estaciones.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/caracteristicas_estaciones.png")
        plt.close()


def main():
    """Función principal"""
    
    print("=" * 70)
    print("APRENDIZAJE NO SUPERVISADO - SISTEMA SETP NEIVA")
    print("=" * 70)
    
    # ==================== CLUSTERING DE USUARIOS ====================
    print("\n" + "=" * 70)
    print("PARTE 1: CLUSTERING DE USUARIOS")
    print("=" * 70)
    
    cluster_usuarios = ClusteringUsuarios()
    cluster_usuarios.cargar_datos()
    cluster_usuarios.preprocesar_datos()
    
    k_optimo = cluster_usuarios.encontrar_k_optimo()
    cluster_usuarios.aplicar_kmeans(n_clusters=4)
    cluster_usuarios.aplicar_dbscan(eps=0.5, min_samples=10)
    
    cluster_usuarios.aplicar_pca()
    cluster_usuarios.visualizar_clusters_pca()
    cluster_usuarios.analizar_perfiles_clusters()
    
    # ==================== CLUSTERING DE ESTACIONES ====================
    print("\n" + "=" * 70)
    print("PARTE 2: CLUSTERING DE ESTACIONES")
    print("=" * 70)
    
    cluster_estaciones = ClusteringEstaciones()
    cluster_estaciones.cargar_datos()
    cluster_estaciones.preprocesar_datos()
    
    cluster_estaciones.aplicar_clustering_jerarquico()
    cluster_estaciones.aplicar_kmeans_estaciones(n_clusters=3)
    cluster_estaciones.visualizar_caracteristicas_estaciones()
    
    print("\n" + "=" * 70)
    print("✓ ANÁLISIS COMPLETADO")
    print("✓ Todas las visualizaciones guardadas en outputs/")
    print("=" * 70)


if __name__ == "__main__":
    main()
