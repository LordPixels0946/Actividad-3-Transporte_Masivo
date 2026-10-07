# GUÍA DE ACTIVIDADES DE MACHINE LEARNING
## Sistema de Transporte SETP Neiva

---

## 📚 CONTENIDO

Este documento explica cómo ejecutar las **Actividades 3 y 4** de Inteligencia Artificial:
- **Actividad 3**: Aprendizaje Supervisado
- **Actividad 4**: Aprendizaje No Supervisado

---

## 📂 ESTRUCTURA DEL PROYECTO

```
Actividad 3 Transporte Masivo/
│
├── Supervisado/                    # ✅ Actividad 3
│   ├── README.md
│   ├── DESCRIPCION_DATOS.md
│   ├── PRUEBAS.md
│   ├── generador_dataset.py
│   ├── modelo_supervisado.py
│   ├── data/                       # Datasets generados
│   └── outputs/                    # Resultados y gráficas
│
├── No_Supervisado/                 # ✅ Actividad 4
│   ├── README.md
│   ├── DESCRIPCION_DATOS.md
│   ├── PRUEBAS.md
│   ├── generador_dataset.py
│   ├── modelo_no_supervisado.py
│   ├── data/                       # Datasets generados
│   └── outputs/                    # Resultados y gráficas
│
├── src/                            # Sistema base SETP
├── docs/                           # Documentación general
├── requirements.txt                # Dependencias
└── ACTIVIDADES_ML.md              # Este archivo
```

---

## 🚀 INSTALACIÓN RÁPIDA

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy openpyxl
```

### 2. Verificar Instalación

```bash
python -c "import sklearn; print('scikit-learn:', sklearn.__version__)"
python -c "import pandas; print('pandas:', pandas.__version__)"
python -c "import numpy; print('numpy:', numpy.__version__)"
```

---

## 📊 ACTIVIDAD 3: APRENDIZAJE SUPERVISADO

### Descripción
Implementa modelos de clasificación y regresión para:
- **Clasificar demanda** de pasajeros (Baja, Media, Alta)
- **Predecir tiempos** de viaje entre estaciones

### Ejecución Paso a Paso

#### Paso 1: Ir a la carpeta
```bash
cd Supervisado
```

#### Paso 2: Generar datasets
```bash
python generador_dataset.py
```

**Salida esperada**:
- `data/dataset_demanda_pasajeros.csv` (10,000 registros)
- `data/dataset_tiempos_viaje.csv` (5,000 registros)

#### Paso 3: Entrenar modelos
```bash
python modelo_supervisado.py
```

**Salida esperada**:
- Métricas en consola
- 5 gráficas PNG en carpeta `outputs/`

### Modelos Implementados

1. **Árbol de Decisión** (Clasificación)
   - Visualización del árbol
   - Exactitud: 75-85%

2. **Random Forest** (Clasificación)
   - Matriz de confusión
   - Exactitud: 82-92%
   - Importancia de features

3. **Regresión Lineal** (Regresión)
   - Predicción de tiempos
   - RMSE: 4-8 minutos

4. **Random Forest** (Regresión)
   - Mejor precisión
   - RMSE: 2-5 minutos
   - R²: 0.85-0.95

### Archivos Generados

```
Supervisado/outputs/
├── arbol_decision_demanda.png
├── matrices_confusion_demanda.png
├── importancia_features_demanda.png
├── predicciones_tiempos_viaje.png
└── comparacion_modelos_regresion.png
```

### Documentación Completa
📖 Ver: [`Supervisado/README.md`](Supervisado/README.md)

---

## 🔍 ACTIVIDAD 4: APRENDIZAJE NO SUPERVISADO

### Descripción
Implementa clustering y reducción de dimensionalidad para:
- **Segmentar usuarios** del SETP (4 perfiles)
- **Agrupar estaciones** (Principal, Intermedia, Secundaria)
- **Descubrir patrones** ocultos

### Ejecución Paso a Paso

#### Paso 1: Ir a la carpeta
```bash
cd No_Supervisado
```

#### Paso 2: Generar datasets
```bash
python generador_dataset.py
```

**Salida esperada**:
- `data/dataset_patrones_usuarios.csv` (2,000 usuarios)
- `data/dataset_estaciones.csv` (15 estaciones)
- `data/dataset_rutas_frecuencias.csv` (~5,000 registros)

#### Paso 3: Aplicar clustering
```bash
python modelo_no_supervisado.py
```

**Salida esperada**:
- Métricas en consola (Silhouette, Davies-Bouldin)
- 5 gráficas PNG en carpeta `outputs/`

### Algoritmos Implementados

1. **K-Means Clustering**
   - Segmentación de usuarios (k=4)
   - Agrupación de estaciones (k=3)
   - Método del codo para optimizar k

2. **DBSCAN**
   - Detección de clusters por densidad
   - Identificación de usuarios atípicos

3. **PCA (Reducción de Dimensionalidad)**
   - Proyección a 2D para visualización
   - Varianza explicada >50%

4. **Clustering Jerárquico**
   - Dendrograma de estaciones
   - Visualización de similitudes

### Archivos Generados

```
No_Supervisado/outputs/
├── optimizacion_k_usuarios.png
├── clusters_usuarios_pca.png
├── perfiles_clusters_usuarios.png
├── dendrograma_estaciones.png
└── caracteristicas_estaciones.png
```

### Perfiles de Usuario Identificados

1. **Trabajadores** (~25%): Uso regular, pocas rutas
2. **Estudiantes** (~25%): Horarios escolares
3. **Ocasionales** (~25%): Uso esporádico, muchas rutas
4. **Turistas** (~25%): Exploración, horarios variables

### Documentación Completa
📖 Ver: [`No_Supervisado/README.md`](No_Supervisado/README.md)

---

## 🧪 PRUEBAS Y VALIDACIÓN

### Actividad 3 - Supervisado
```bash
cd Supervisado
python generador_dataset.py
python modelo_supervisado.py
ls -l data/
ls -l outputs/
```

📋 Ver: [`Supervisado/PRUEBAS.md`](Supervisado/PRUEBAS.md)

### Actividad 4 - No Supervisado
```bash
cd No_Supervisado
python generador_dataset.py
python modelo_no_supervisado.py
ls -l data/
ls -l outputs/
```

📋 Ver: [`No_Supervisado/PRUEBAS.md`](No_Supervisado/PRUEBAS.md)

---

## 📈 MÉTRICAS DE ÉXITO

### Actividad 3 (Supervisado)

| Modelo | Métrica | Objetivo |
|--------|---------|----------|
| Árbol de Decisión | Exactitud | >75% |
| Random Forest (Clasificación) | Exactitud | >82% |
| Regresión Lineal | RMSE | <8 min |
| Random Forest (Regresión) | R² | >0.85 |

### Actividad 4 (No Supervisado)

| Algoritmo | Métrica | Objetivo |
|-----------|---------|----------|
| K-Means | Silhouette Score | >0.35 |
| DBSCAN | Clusters encontrados | 3-6 |
| PCA | Varianza explicada | >50% |
| Jerárquico | Dendrograma | Legible |

---

## 🎯 ENTREGABLES REQUERIDOS

### Para Ambas Actividades

1. ✅ **Archivos de fuentes de datos** (CSV en carpetas `data/`)
2. ✅ **Código fuente Python** (`generador_dataset.py`, `modelo_*.py`)
3. ✅ **Descripción de datos** (`DESCRIPCION_DATOS.md`)
4. ✅ **Documento de pruebas** (`PRUEBAS.md`)
5. ⏳ **Video explicativo** (10 min Actividad 3, 5 min Actividad 4)
6. ⏳ **Repositorio Git** con commits de cada integrante

### Checklist de Entrega

- [ ] Datasets generados sin errores
- [ ] Modelos entrenan correctamente
- [ ] Todas las visualizaciones creadas
- [ ] Métricas cumplen objetivos
- [ ] Documentación completa y clara
- [ ] Video grabado con participación de todos
- [ ] Repositorio Git actualizado
- [ ] Tutor agregado como colaborador
- [ ] PDF con links subido a plataforma

---

## 📹 GUÍA PARA VIDEO

### Actividad 3 (Máx. 10 minutos)

**Estructura sugerida**:
1. Introducción (1 min)
   - Presentación del equipo
   - Objetivo del proyecto

2. Descripción de datos (2 min)
   - Datasets generados
   - Variables y features
   - Tamaño de datasets

3. Modelos implementados (4 min)
   - Árbol de decisión y Random Forest
   - Regresión lineal y RF Regressor
   - Mostrar código clave

4. Resultados (2 min)
   - Métricas obtenidas
   - Visualizaciones generadas
   - Comparación de modelos

5. Conclusiones (1 min)
   - Aprendizajes
   - Aplicaciones prácticas

### Actividad 4 (Máx. 5 minutos)

**Estructura sugerida**:
1. Introducción (30 seg)
   - Objetivo: clustering y patrones

2. Algoritmos (2 min)
   - K-Means, DBSCAN, PCA
   - Clustering jerárquico
   - Mostrar código

3. Resultados (2 min)
   - Perfiles identificados
   - Visualizaciones
   - Interpretación de clusters

4. Conclusiones (30 seg)
   - Aplicaciones prácticas

---

## 🐛 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: ModuleNotFoundError: No module named 'sklearn'
```bash
pip install scikit-learn
```

### Error: Carpetas data/ u outputs/ no existen
```bash
cd Supervisado
mkdir data outputs

cd ../No_Supervisado
mkdir data outputs
```

### Datasets vacíos o faltantes
Ejecutar primero `generador_dataset.py`:
```bash
python generador_dataset.py
```

### Gráficas no se generan
Verificar que carpeta `outputs/` existe:
```bash
mkdir outputs
```

### Métricas muy bajas
- Verificar que datasets se generaron correctamente
- Revisar normalización de datos
- Ajustar hiperparámetros de modelos

---

## 📚 REFERENCIAS BIBLIOGRÁFICAS

1. **Palma Méndez, J. T. (2008)**. *Inteligencia artificial: métodos, técnicas y aplicaciones*. Madrid: McGraw-Hill España.
   - Capítulo 16: Técnicas de agrupamiento (No Supervisado)
   - Capítulo 17: Aprendizaje de árboles y reglas de decisión (Supervisado)

2. **Scikit-learn Documentation**
   - https://scikit-learn.org/stable/

3. **Python Data Science Handbook**
   - Machine Learning con Scikit-learn

---

## 👥 INFORMACIÓN DEL EQUIPO

### Actividad 3 (Máx. 4 integrantes)
- Integrante 1: [Nombre] - [Email]
- Integrante 2: [Nombre] - [Email]
- Integrante 3: [Nombre] - [Email]
- Integrante 4: [Nombre] - [Email]

### Actividad 4 (Máx. 3 integrantes)
- Integrante 1: [Nombre] - [Email]
- Integrante 2: [Nombre] - [Email]
- Integrante 3: [Nombre] - [Email]

---

## 📧 CONTACTO Y SOPORTE

**Proyecto**: Sistema Inteligente SETP Neiva  
**Curso**: Inteligencia Artificial  
**Fecha**: 2026-09-27  
**Repositorio**: https://github.com/LordPixels0946/Actividad-3-Transporte_Masivo.git

---

## ✅ VALIDACIÓN FINAL

Antes de entregar, verificar:

```bash
# Supervisado
cd Supervisado
python generador_dataset.py && python modelo_supervisado.py
ls data/ outputs/

# No Supervisado
cd ../No_Supervisado
python generador_dataset.py && python modelo_no_supervisado.py
ls data/ outputs/
```

**Todo listo si**:
- ✅ No hay errores en consola
- ✅ Todos los archivos CSV se generaron
- ✅ Todas las PNG se crearon
- ✅ Métricas cumplen objetivos

---

¡Éxito con las actividades! 🚀
