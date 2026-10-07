# APRENDIZAJE SUPERVISADO - SETP NEIVA
## Actividad 3: Métodos de Aprendizaje Supervisado

---

## 📖 DESCRIPCIÓN DEL PROYECTO

Este módulo implementa modelos de **aprendizaje supervisado** para el Sistema de Transporte Público SETP de Neiva, Colombia. Se desarrollan dos tipos de modelos:

1. **Clasificación**: Predicción de demanda de pasajeros (Baja, Media, Alta)
2. **Regresión**: Predicción de tiempos de viaje entre estaciones

---

## 🗂️ ESTRUCTURA DE ARCHIVOS

```
Supervisado/
├── README.md                           # Este archivo
├── DESCRIPCION_DATOS.md                # Descripción detallada de datasets
├── PRUEBAS.md                          # Documento de pruebas y validación
├── generador_dataset.py                # Genera datasets sintéticos
├── modelo_supervisado.py               # Implementación de modelos ML
├── data/                               # Carpeta para datasets
│   ├── dataset_demanda_pasajeros.csv   # Dataset de clasificación
│   └── dataset_tiempos_viaje.csv       # Dataset de regresión
└── outputs/                            # Carpeta para resultados
    ├── arbol_decision_demanda.png
    ├── matrices_confusion_demanda.png
    ├── importancia_features_demanda.png
    ├── predicciones_tiempos_viaje.png
    └── comparacion_modelos_regresion.png
```

---

## 🚀 INSTALACIÓN Y REQUISITOS

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalar Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

O desde el directorio raíz del proyecto:

```bash
pip install -r requirements.txt
```

---

## 💻 CÓMO USAR

### Paso 1: Generar Datasets

```bash
cd Supervisado
python generador_dataset.py
```

**Salida**:
- `data/dataset_demanda_pasajeros.csv` (10,000 registros)
- `data/dataset_tiempos_viaje.csv` (5,000 registros)

---

### Paso 2: Entrenar Modelos y Generar Resultados

```bash
python modelo_supervisado.py
```

**Salida**:
- Métricas de evaluación en consola
- 5 visualizaciones en carpeta `outputs/`
- Comparación de modelos

---

## 📊 MODELOS IMPLEMENTADOS

### 1. Clasificación de Demanda

#### Árbol de Decisión
- **Algoritmo**: DecisionTreeClassifier
- **Parámetros**: max_depth=5, min_samples_split=20
- **Métricas**: Exactitud, Precision, Recall, F1-Score
- **Ventajas**: Interpretable, visualizable

#### Random Forest
- **Algoritmo**: RandomForestClassifier
- **Parámetros**: n_estimators=100, max_depth=10
- **Métricas**: Exactitud, Matriz de confusión
- **Ventajas**: Mayor precisión, robusto

---

### 2. Predicción de Tiempos de Viaje

#### Regresión Lineal
- **Algoritmo**: LinearRegression
- **Métricas**: RMSE, MAE, R²
- **Ventajas**: Simple, rápido

#### Random Forest Regressor
- **Algoritmo**: RandomForestRegressor
- **Parámetros**: n_estimators=100, max_depth=15
- **Métricas**: RMSE, MAE, R²
- **Ventajas**: Captura relaciones no lineales

---

## 📈 RESULTADOS ESPERADOS

### Clasificación de Demanda
- **Árbol de Decisión**: 75-85% exactitud
- **Random Forest**: 82-92% exactitud

### Predicción de Tiempos
- **Regresión Lineal**: RMSE 4-8 min, R² 0.65-0.80
- **Random Forest**: RMSE 2-5 min, R² 0.85-0.95

---

## 📊 VISUALIZACIONES GENERADAS

### 1. Árbol de Decisión (`arbol_decision_demanda.png`)
Visualización completa del árbol de decisión mostrando:
- Nodos de decisión con splits
- Valores en hojas
- Clases predichas

### 2. Matrices de Confusión (`matrices_confusion_demanda.png`)
Comparación lado a lado de:
- Árbol de Decisión
- Random Forest
- Clasificación por clase

### 3. Importancia de Features (`importancia_features_demanda.png`)
Gráfico de barras mostrando:
- Ranking de características más importantes
- Valores de importancia

### 4. Predicciones vs Reales (`predicciones_tiempos_viaje.png`)
Scatter plots para:
- Regresión Lineal
- Random Forest
- Línea de predicción perfecta

### 5. Comparación de Modelos (`comparacion_modelos_regresion.png`)
Comparativa de métricas:
- RMSE
- MAE
- R²

---

## 🔍 VARIABLES Y FEATURES

### Dataset de Demanda

**Features**:
- `hora`: Hora del día (5-22)
- `dia_semana`: Día de la semana (0-6)
- `estacion`: Estación del SETP
- `clima`: Condición climática
- `temperatura`: Temperatura en °C
- `evento_especial`: Presencia de evento (0/1)
- `num_pasajeros`: Número de pasajeros

**Target**: `demanda` (Baja, Media, Alta)

### Dataset de Tiempos de Viaje

**Features**:
- `origen`: Estación de origen
- `destino`: Estación de destino
- `hora`: Hora del viaje
- `dia_semana`: Día de la semana
- `clima`: Condición climática
- `trafico`: Nivel de tráfico
- `num_paradas`: Paradas en ruta

**Target**: `tiempo_viaje_minutos` (continua)

---

## 🧪 PRUEBAS Y VALIDACIÓN

Ver documento completo: [`PRUEBAS.md`](PRUEBAS.md)

**Ejecutar pruebas**:
```bash
# Generar datasets
python generador_dataset.py

# Entrenar y evaluar modelos
python modelo_supervisado.py

# Verificar archivos de salida
ls -l data/
ls -l outputs/
```

---

## 📚 REFERENCIAS

- Palma Méndez, J. T. (2008). *Inteligencia artificial: métodos, técnicas y aplicaciones*. Madrid: McGraw-Hill España. Capítulo 17: Aprendizaje de árboles y reglas de decisión.
- Scikit-learn Documentation: https://scikit-learn.org/
- Aprendizaje Supervisado: Clasificación y Regresión

---

## 🎯 APLICACIONES PRÁCTICAS

1. **Gestión de Flota**
   - Asignar buses según demanda predicha
   - Optimizar frecuencias por estación

2. **Información a Usuarios**
   - Estimar tiempos de viaje precisos
   - Alertas de alta demanda

3. **Planificación Operativa**
   - Personal extra en horas/lugares con alta demanda
   - Rutas alternativas en condiciones adversas

4. **Análisis de Impacto**
   - Evaluar efectos de eventos especiales
   - Planificar para condiciones climáticas

---

## 👥 EQUIPO

- **Integrante 1**: [Nombre]
- **Integrante 2**: [Nombre]
- **Integrante 3**: [Nombre]
- **Integrante 4**: [Nombre]

---

## 📝 NOTAS IMPORTANTES

- Los datos son **sintéticos** pero basados en patrones reales
- Semilla aleatoria (42) garantiza **reproducibilidad**
- Los modelos son **entrenable** y pueden mejorarse con datos reales
- División 75/25 para train/test con **estratificación**

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: ModuleNotFoundError
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Error: Carpeta 'data' no existe
```bash
mkdir data outputs
python generador_dataset.py
```

### Datasets vacíos
Ejecutar primero `generador_dataset.py` antes de `modelo_supervisado.py`

---

## 📧 CONTACTO

**Proyecto**: Sistema Inteligente SETP Neiva  
**Curso**: Inteligencia Artificial  
**Fecha**: 2026-09-27  
**Versión**: 1.0

---

## 📄 LICENCIA

Este proyecto es parte de una actividad académica para el curso de Inteligencia Artificial.
