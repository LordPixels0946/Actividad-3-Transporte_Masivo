# -*- coding: utf-8 -*-
"""
MODELOS DE APRENDIZAJE SUPERVISADO - SETP NEIVA
Implementa:
1. Clasificación: Predicción de demanda (Árbol de Decisión, Random Forest)
2. Regresión: Predicción de tiempos de viaje (Regresión Lineal, Random Forest)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    mean_squared_error, r2_score, mean_absolute_error
)
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)


class ModeloClasificacionDemanda:
    """Modelo de clasificación para predecir demanda de pasajeros"""
    
    def __init__(self, ruta_dataset='data/dataset_demanda_pasajeros.csv'):
        self.ruta_dataset = ruta_dataset
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.modelo_arbol = None
        self.modelo_rf = None
        self.label_encoders = {}
        
    def cargar_datos(self):
        """Carga y preprocesa los datos"""
        print("\n📊 Cargando dataset de demanda...")
        self.df = pd.read_csv(self.ruta_dataset)
        print(f"   ✓ Dataset cargado: {self.df.shape[0]} registros, {self.df.shape[1]} columnas")
        
        # Mostrar información
        print("\n📈 Distribución de clases:")
        print(self.df['demanda'].value_counts())
        
    def preprocesar_datos(self):
        """Preprocesa los datos para el modelo"""
        print("\n🔧 Preprocesando datos...")
        
        # Variables categóricas a codificar
        cols_categoricas = ['estacion', 'clima']
        
        for col in cols_categoricas:
            le = LabelEncoder()
            self.df[col + '_encoded'] = le.fit_transform(self.df[col])
            self.label_encoders[col] = le
            
        # Seleccionar features
        features = ['hora', 'dia_semana', 'estacion_encoded', 'clima_encoded', 
                   'temperatura', 'evento_especial', 'num_pasajeros']
        
        X = self.df[features]
        y = self.df['demanda']
        
        # Dividir en train/test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.25, random_state=42, stratify=y
        )
        
        print(f"   ✓ Datos de entrenamiento: {len(self.X_train)}")
        print(f"   ✓ Datos de prueba: {len(self.X_test)}")
        
    def entrenar_arbol_decision(self):
        """Entrena un árbol de decisión"""
        print("\n🌳 Entrenando Árbol de Decisión...")
        
        self.modelo_arbol = DecisionTreeClassifier(
            max_depth=5,
            min_samples_split=20,
            random_state=42
        )
        
        self.modelo_arbol.fit(self.X_train, self.y_train)
        
        # Evaluación
        y_pred = self.modelo_arbol.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        
        print(f"   ✓ Exactitud: {accuracy:.4f}")
        print("\n📊 Reporte de clasificación:")
        print(classification_report(self.y_test, y_pred))
        
        return accuracy
        
    def entrenar_random_forest(self):
        """Entrena un Random Forest"""
        print("\n🌲 Entrenando Random Forest...")
        
        self.modelo_rf = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=10,
            random_state=42
        )
        
        self.modelo_rf.fit(self.X_train, self.y_train)
        
        # Evaluación
        y_pred = self.modelo_rf.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        
        print(f"   ✓ Exactitud: {accuracy:.4f}")
        print("\n📊 Reporte de clasificación:")
        print(classification_report(self.y_test, y_pred))
        
        return accuracy
        
    def visualizar_arbol(self):
        """Visualiza el árbol de decisión"""
        print("\n📊 Generando visualización del árbol...")
        
        plt.figure(figsize=(20, 10))
        plot_tree(
            self.modelo_arbol,
            feature_names=['hora', 'dia_semana', 'estacion', 'clima', 
                          'temperatura', 'evento_especial', 'num_pasajeros'],
            class_names=['Alta', 'Baja', 'Media'],
            filled=True,
            rounded=True,
            fontsize=10
        )
        plt.title('Árbol de Decisión - Predicción de Demanda SETP', 
                 fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/arbol_decision_demanda.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/arbol_decision_demanda.png")
        plt.close()
        
    def visualizar_matriz_confusion(self):
        """Visualiza matriz de confusión para ambos modelos"""
        print("\n📊 Generando matrices de confusión...")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Árbol de Decisión
        y_pred_arbol = self.modelo_arbol.predict(self.X_test)
        cm_arbol = confusion_matrix(self.y_test, y_pred_arbol)
        sns.heatmap(cm_arbol, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                   xticklabels=['Alta', 'Baja', 'Media'],
                   yticklabels=['Alta', 'Baja', 'Media'])
        axes[0].set_title('Árbol de Decisión', fontweight='bold')
        axes[0].set_ylabel('Real')
        axes[0].set_xlabel('Predicho')
        
        # Random Forest
        y_pred_rf = self.modelo_rf.predict(self.X_test)
        cm_rf = confusion_matrix(self.y_test, y_pred_rf)
        sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', ax=axes[1],
                   xticklabels=['Alta', 'Baja', 'Media'],
                   yticklabels=['Alta', 'Baja', 'Media'])
        axes[1].set_title('Random Forest', fontweight='bold')
        axes[1].set_ylabel('Real')
        axes[1].set_xlabel('Predicho')
        
        plt.suptitle('Matrices de Confusión - Predicción de Demanda SETP', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/matrices_confusion_demanda.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/matrices_confusion_demanda.png")
        plt.close()
        
    def importancia_features(self):
        """Visualiza importancia de características"""
        print("\n📊 Analizando importancia de características...")
        
        importancias = self.modelo_rf.feature_importances_
        features = ['hora', 'dia_semana', 'estacion', 'clima', 
                   'temperatura', 'evento_especial', 'num_pasajeros']
        
        df_importancia = pd.DataFrame({
            'Feature': features,
            'Importancia': importancias
        }).sort_values('Importancia', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df_importancia, x='Importancia', y='Feature', palette='viridis')
        plt.title('Importancia de Características - Random Forest\nPredicción de Demanda SETP', 
                 fontweight='bold')
        plt.xlabel('Importancia')
        plt.tight_layout()
        plt.savefig('outputs/importancia_features_demanda.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/importancia_features_demanda.png")
        plt.close()


class ModeloRegresionTiempos:
    """Modelo de regresión para predecir tiempos de viaje"""
    
    def __init__(self, ruta_dataset='data/dataset_tiempos_viaje.csv'):
        self.ruta_dataset = ruta_dataset
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.modelo_lr = None
        self.modelo_rf = None
        self.label_encoders = {}
        
    def cargar_datos(self):
        """Carga y preprocesa los datos"""
        print("\n📊 Cargando dataset de tiempos de viaje...")
        self.df = pd.read_csv(self.ruta_dataset)
        print(f"   ✓ Dataset cargado: {self.df.shape[0]} registros, {self.df.shape[1]} columnas")
        
        # Estadísticas
        print(f"\n📈 Tiempo de viaje (minutos):")
        print(f"   - Promedio: {self.df['tiempo_viaje_minutos'].mean():.2f}")
        print(f"   - Min: {self.df['tiempo_viaje_minutos'].min():.2f}")
        print(f"   - Max: {self.df['tiempo_viaje_minutos'].max():.2f}")
        
    def preprocesar_datos(self):
        """Preprocesa los datos para el modelo"""
        print("\n🔧 Preprocesando datos...")
        
        # Variables categóricas a codificar
        cols_categoricas = ['origen', 'destino', 'clima', 'trafico']
        
        for col in cols_categoricas:
            le = LabelEncoder()
            self.df[col + '_encoded'] = le.fit_transform(self.df[col])
            self.label_encoders[col] = le
            
        # Seleccionar features
        features = ['origen_encoded', 'destino_encoded', 'hora', 'dia_semana',
                   'clima_encoded', 'trafico_encoded', 'num_paradas']
        
        X = self.df[features]
        y = self.df['tiempo_viaje_minutos']
        
        # Dividir en train/test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.25, random_state=42
        )
        
        print(f"   ✓ Datos de entrenamiento: {len(self.X_train)}")
        print(f"   ✓ Datos de prueba: {len(self.X_test)}")
        
    def entrenar_regresion_lineal(self):
        """Entrena regresión lineal"""
        print("\n📈 Entrenando Regresión Lineal...")
        
        self.modelo_lr = LinearRegression()
        self.modelo_lr.fit(self.X_train, self.y_train)
        
        # Evaluación
        y_pred = self.modelo_lr.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        print(f"   ✓ RMSE: {rmse:.4f} minutos")
        print(f"   ✓ MAE: {mae:.4f} minutos")
        print(f"   ✓ R²: {r2:.4f}")
        
        return rmse, mae, r2
        
    def entrenar_random_forest_regresion(self):
        """Entrena Random Forest para regresión"""
        print("\n🌲 Entrenando Random Forest (Regresión)...")
        
        self.modelo_rf = RandomForestRegressor(
            n_estimators=100,
            max_depth=15,
            min_samples_split=5,
            random_state=42
        )
        
        self.modelo_rf.fit(self.X_train, self.y_train)
        
        # Evaluación
        y_pred = self.modelo_rf.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        print(f"   ✓ RMSE: {rmse:.4f} minutos")
        print(f"   ✓ MAE: {mae:.4f} minutos")
        print(f"   ✓ R²: {r2:.4f}")
        
        return rmse, mae, r2
        
    def visualizar_predicciones(self):
        """Visualiza predicciones vs valores reales"""
        print("\n📊 Generando gráficas de predicciones...")
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Regresión Lineal
        y_pred_lr = self.modelo_lr.predict(self.X_test)
        axes[0].scatter(self.y_test, y_pred_lr, alpha=0.5)
        axes[0].plot([self.y_test.min(), self.y_test.max()], 
                    [self.y_test.min(), self.y_test.max()], 
                    'r--', lw=2)
        axes[0].set_xlabel('Tiempo Real (min)')
        axes[0].set_ylabel('Tiempo Predicho (min)')
        axes[0].set_title('Regresión Lineal', fontweight='bold')
        axes[0].grid(True, alpha=0.3)
        
        # Random Forest
        y_pred_rf = self.modelo_rf.predict(self.X_test)
        axes[1].scatter(self.y_test, y_pred_rf, alpha=0.5, color='green')
        axes[1].plot([self.y_test.min(), self.y_test.max()], 
                    [self.y_test.min(), self.y_test.max()], 
                    'r--', lw=2)
        axes[1].set_xlabel('Tiempo Real (min)')
        axes[1].set_ylabel('Tiempo Predicho (min)')
        axes[1].set_title('Random Forest', fontweight='bold')
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle('Predicciones vs Valores Reales - Tiempos de Viaje SETP', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/predicciones_tiempos_viaje.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/predicciones_tiempos_viaje.png")
        plt.close()
        
    def comparar_modelos(self, metricas_lr, metricas_rf):
        """Compara métricas de ambos modelos"""
        print("\n📊 Generando comparativa de modelos...")
        
        modelos = ['Regresión Lineal', 'Random Forest']
        rmse_values = [metricas_lr[0], metricas_rf[0]]
        mae_values = [metricas_lr[1], metricas_rf[1]]
        r2_values = [metricas_lr[2], metricas_rf[2]]
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        # RMSE
        axes[0].bar(modelos, rmse_values, color=['steelblue', 'forestgreen'])
        axes[0].set_ylabel('RMSE (minutos)')
        axes[0].set_title('Error Cuadrático Medio', fontweight='bold')
        axes[0].grid(axis='y', alpha=0.3)
        
        # MAE
        axes[1].bar(modelos, mae_values, color=['steelblue', 'forestgreen'])
        axes[1].set_ylabel('MAE (minutos)')
        axes[1].set_title('Error Absoluto Medio', fontweight='bold')
        axes[1].grid(axis='y', alpha=0.3)
        
        # R²
        axes[2].bar(modelos, r2_values, color=['steelblue', 'forestgreen'])
        axes[2].set_ylabel('R² Score')
        axes[2].set_title('Coeficiente de Determinación', fontweight='bold')
        axes[2].set_ylim([0, 1])
        axes[2].grid(axis='y', alpha=0.3)
        
        plt.suptitle('Comparación de Modelos - Predicción de Tiempos SETP', 
                    fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/comparacion_modelos_regresion.png', dpi=300, bbox_inches='tight')
        print("   ✓ Guardado: outputs/comparacion_modelos_regresion.png")
        plt.close()


def main():
    """Función principal"""
    
    print("=" * 70)
    print("APRENDIZAJE SUPERVISADO - SISTEMA SETP NEIVA")
    print("=" * 70)
    
    # ==================== CLASIFICACIÓN ====================
    print("\n" + "=" * 70)
    print("PARTE 1: CLASIFICACIÓN DE DEMANDA DE PASAJEROS")
    print("=" * 70)
    
    clasificador = ModeloClasificacionDemanda()
    clasificador.cargar_datos()
    clasificador.preprocesar_datos()
    
    acc_arbol = clasificador.entrenar_arbol_decision()
    acc_rf = clasificador.entrenar_random_forest()
    
    clasificador.visualizar_arbol()
    clasificador.visualizar_matriz_confusion()
    clasificador.importancia_features()
    
    # ==================== REGRESIÓN ====================
    print("\n" + "=" * 70)
    print("PARTE 2: REGRESIÓN DE TIEMPOS DE VIAJE")
    print("=" * 70)
    
    regresor = ModeloRegresionTiempos()
    regresor.cargar_datos()
    regresor.preprocesar_datos()
    
    metricas_lr = regresor.entrenar_regresion_lineal()
    metricas_rf = regresor.entrenar_random_forest_regresion()
    
    regresor.visualizar_predicciones()
    regresor.comparar_modelos(metricas_lr, metricas_rf)
    
    # ==================== RESUMEN ====================
    print("\n" + "=" * 70)
    print("RESUMEN DE RESULTADOS")
    print("=" * 70)
    print("\n📊 CLASIFICACIÓN (Predicción de Demanda):")
    print(f"   - Árbol de Decisión: {acc_arbol:.4f} exactitud")
    print(f"   - Random Forest: {acc_rf:.4f} exactitud")
    
    print("\n📈 REGRESIÓN (Predicción de Tiempos):")
    print(f"   - Regresión Lineal: RMSE={metricas_lr[0]:.2f} min, R²={metricas_lr[2]:.4f}")
    print(f"   - Random Forest: RMSE={metricas_rf[0]:.2f} min, R²={metricas_rf[2]:.4f}")
    
    print("\n✓ Todas las visualizaciones guardadas en outputs/")
    print("=" * 70)


if __name__ == "__main__":
    main()
