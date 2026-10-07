# DOCUMENTO DE PRUEBAS - APRENDIZAJE SUPERVISADO
## Sistema de Transporte SETP Neiva

---

## 📋 ÍNDICE DE PRUEBAS

1. [Pruebas de Generación de Datasets](#1-pruebas-de-generación-de-datasets)
2. [Pruebas de Modelos de Clasificación](#2-pruebas-de-modelos-de-clasificación)
3. [Pruebas de Modelos de Regresión](#3-pruebas-de-modelos-de-regresión)
4. [Pruebas de Visualización](#4-pruebas-de-visualización)
5. [Pruebas de Integración](#5-pruebas-de-integración)
6. [Resultados Esperados](#6-resultados-esperados)

---

## 1. PRUEBAS DE GENERACIÓN DE DATASETS

### Prueba 1.1: Generación de Dataset de Demanda

**Comando**:
```bash
cd Supervisado
python generador_dataset.py
```

**Verificaciones**:
- ✅ Se crea archivo `data/dataset_demanda_pasajeros.csv`
- ✅ Contiene 10,000 registros
- ✅ Tiene 8 columnas
- ✅ No hay valores nulos
- ✅ Distribución balanceada de clases (Baja, Media, Alta)
- ✅ Rangos de valores válidos:
  - hora: 5-22
  - temperatura: 22-35
  - num_pasajeros: 10-300

**Resultado Esperado**:
```
✓ Generados 10000 registros
✓ Guardado en: data/dataset_demanda_pasajeros.csv

Distribución de demanda:
Media    4XXX
Alta     3XXX
Baja     2XXX
```

**Estado**: ⏳ Por ejecutar

---

### Prueba 1.2: Generación de Dataset de Tiempos

**Comando**:
```bash
cd Supervisado
python generador_dataset.py
```

**Verificaciones**:
- ✅ Se crea archivo `data/dataset_tiempos_viaje.csv`
- ✅ Contiene 5,000 registros
- ✅ Tiene 8 columnas
- ✅ Tiempos de viaje son positivos y realistas (5-60 min)
- ✅ Todas las rutas tienen registros

**Resultado Esperado**:
```
✓ Generados 5000 registros
✓ Guardado en: data/dataset_tiempos_viaje.csv

Promedio: ~20 minutos
Min: ~8 minutos
Max: ~45 minutos
```

**Estado**: ⏳ Por ejecutar

---

## 2. PRUEBAS DE MODELOS DE CLASIFICACIÓN

### Prueba 2.1: Árbol de Decisión

**Comando**:
```bash
cd Supervisado
python modelo_supervisado.py
```

**Verificaciones**:
- ✅ Modelo entrena sin errores
- ✅ Exactitud > 70%
- ✅ Reporte de clasificación muestra Precision/Recall/F1
- ✅ No hay overfitting extremo (diferencia train/test < 15%)

**Métricas Esperadas**:
- Exactitud: 75-85%
- Precision promedio: > 0.70
- Recall promedio: > 0.70
- F1-Score promedio: > 0.70

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
Exactitud: ____
Precision: ____
Recall: ____
F1-Score: ____
```

---

### Prueba 2.2: Random Forest Classifier

**Comando**:
```bash
cd Supervisado
python modelo_supervisado.py
```

**Verificaciones**:
- ✅ Modelo entrena sin errores
- ✅ Exactitud mayor que árbol simple
- ✅ Exactitud > 80%
- ✅ Matriz de confusión muestra buena clasificación

**Métricas Esperadas**:
- Exactitud: 82-92%
- Mejor performance que árbol de decisión simple
- Buena clasificación en las 3 clases

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
Exactitud: ____
Mejora vs Árbol: ____%
```

---

### Prueba 2.3: Importancia de Features

**Verificaciones**:
- ✅ Todas las features tienen importancia > 0
- ✅ `num_pasajeros` debe ser el feature más importante
- ✅ `hora` y `estacion` deben tener alta importancia
- ✅ Suma de importancias = 1.0

**Ranking Esperado**:
1. num_pasajeros (más importante)
2. hora
3. estacion
4. evento_especial
5. clima
6. dia_semana
7. temperatura

**Estado**: ⏳ Por ejecutar

---

## 3. PRUEBAS DE MODELOS DE REGRESIÓN

### Prueba 3.1: Regresión Lineal

**Comando**:
```bash
cd Supervisado
python modelo_supervisado.py
```

**Verificaciones**:
- ✅ Modelo entrena sin errores
- ✅ RMSE < 8 minutos
- ✅ MAE < 6 minutos
- ✅ R² > 0.60

**Métricas Esperadas**:
- RMSE: 4-8 minutos
- MAE: 3-6 minutos
- R²: 0.65-0.80

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
RMSE: ____ minutos
MAE: ____ minutos
R²: ____
```

---

### Prueba 3.2: Random Forest Regressor

**Comando**:
```bash
cd Supervisado
python modelo_supervisado.py
```

**Verificaciones**:
- ✅ Modelo entrena sin errores
- ✅ RMSE menor que regresión lineal
- ✅ R² > 0.80
- ✅ Predicciones dentro de rango razonable

**Métricas Esperadas**:
- RMSE: 2-5 minutos
- MAE: 1.5-4 minutos
- R²: 0.85-0.95

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
RMSE: ____ minutos
MAE: ____ minutos
R²: ____
Mejora vs Lineal: ____%
```

---

## 4. PRUEBAS DE VISUALIZACIÓN

### Prueba 4.1: Árbol de Decisión Visual

**Verificaciones**:
- ✅ Archivo `outputs/arbol_decision_demanda.png` creado
- ✅ Árbol es legible y no muy profundo (max_depth=5)
- ✅ Muestra splits y valores en nodos
- ✅ Colores indican clases correctamente

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.2: Matrices de Confusión

**Verificaciones**:
- ✅ Archivo `outputs/matrices_confusion_demanda.png` creado
- ✅ Dos matrices lado a lado (Árbol y RF)
- ✅ Diagonal principal tiene valores altos (buena clasificación)
- ✅ Etiquetas correctas en ejes

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.3: Importancia de Features

**Verificaciones**:
- ✅ Archivo `outputs/importancia_features_demanda.png` creado
- ✅ Gráfico de barras ordenado de mayor a menor
- ✅ Todas las features visibles
- ✅ Valores entre 0 y 1

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.4: Predicciones vs Reales

**Verificaciones**:
- ✅ Archivo `outputs/predicciones_tiempos_viaje.png` creado
- ✅ Dos scatter plots (Regresión Lineal y RF)
- ✅ Línea diagonal perfecta de referencia
- ✅ Puntos cercanos a la diagonal = buenas predicciones

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.5: Comparación de Modelos

**Verificaciones**:
- ✅ Archivo `outputs/comparacion_modelos_regresion.png` creado
- ✅ Tres gráficos de barras (RMSE, MAE, R²)
- ✅ Comparación visual clara entre modelos
- ✅ Random Forest debe mostrar mejores métricas

**Estado**: ⏳ Por ejecutar

---

## 5. PRUEBAS DE INTEGRACIÓN

### Prueba 5.1: Pipeline Completo

**Comando**:
```bash
cd Supervisado
python generador_dataset.py
python modelo_supervisado.py
```

**Verificaciones**:
- ✅ Ambos scripts ejecutan sin errores
- ✅ Todos los archivos de salida se generan
- ✅ Tiempo de ejecución total < 5 minutos
- ✅ No hay warnings críticos

**Estado**: ⏳ Por ejecutar

---

### Prueba 5.2: Validación de Archivos de Salida

**Verificaciones**:
```bash
ls -l data/
ls -l outputs/
```

**Archivos Esperados**:
- data/dataset_demanda_pasajeros.csv
- data/dataset_tiempos_viaje.csv
- outputs/arbol_decision_demanda.png
- outputs/matrices_confusion_demanda.png
- outputs/importancia_features_demanda.png
- outputs/predicciones_tiempos_viaje.png
- outputs/comparacion_modelos_regresion.png

**Estado**: ⏳ Por ejecutar

---

## 6. RESULTADOS ESPERADOS

### 6.1 Resumen de Métricas Objetivo

| Modelo | Métrica | Valor Esperado | Valor Real |
|--------|---------|----------------|------------|
| Árbol Decisión | Exactitud | 75-85% | ____ |
| Random Forest (Clasificación) | Exactitud | 82-92% | ____ |
| Regresión Lineal | RMSE | 4-8 min | ____ |
| Regresión Lineal | R² | 0.65-0.80 | ____ |
| Random Forest (Regresión) | RMSE | 2-5 min | ____ |
| Random Forest (Regresión) | R² | 0.85-0.95 | ____ |

---

### 6.2 Casos de Prueba Específicos

#### Caso 1: Alta Demanda en Hora Pico
**Input**:
- hora = 7 (7am)
- dia_semana = 1 (Martes)
- estacion = Terminal
- clima = Soleado
- evento_especial = 0
- num_pasajeros = 250

**Predicción Esperada**: **Alta** demanda

**Estado**: ⏳ Por probar

---

#### Caso 2: Baja Demanda Nocturna
**Input**:
- hora = 21 (9pm)
- dia_semana = 6 (Domingo)
- estacion = Miraflores
- clima = Nublado
- evento_especial = 0
- num_pasajeros = 25

**Predicción Esperada**: **Baja** demanda

**Estado**: ⏳ Por probar

---

#### Caso 3: Tiempo de Viaje con Tráfico Alto
**Input**:
- origen = Terminal
- destino = Centro
- hora = 18 (6pm)
- dia_semana = 3 (Jueves)
- clima = Lluvioso
- trafico = Alto
- num_paradas = 8

**Predicción Esperada**: 30-40 minutos

**Estado**: ⏳ Por probar

---

## 7. CRITERIOS DE ACEPTACIÓN

### ✅ El sistema pasa las pruebas si:

1. **Datasets**:
   - Se generan sin errores
   - Tienen el tamaño esperado
   - No contienen valores nulos

2. **Modelos de Clasificación**:
   - Exactitud > 75%
   - No hay overfitting extremo
   - Todas las clases se predicen correctamente

3. **Modelos de Regresión**:
   - RMSE < 8 minutos
   - R² > 0.65
   - Predicciones son razonables

4. **Visualizaciones**:
   - Todos los archivos PNG se generan
   - Son legibles y profesionales
   - Muestran información correcta

5. **Performance**:
   - Ejecución completa < 5 minutos
   - No hay errores de memoria
   - Scripts son reproducibles

---

## 📝 REGISTRO DE EJECUCIÓN

### Ejecución 1
**Fecha**: ___________  
**Ejecutado por**: ___________  
**Resultados**: ___________  
**Observaciones**: ___________

### Ejecución 2
**Fecha**: ___________  
**Ejecutado por**: ___________  
**Resultados**: ___________  
**Observaciones**: ___________

---

**Documento creado**: 2026-09-27  
**Versión**: 1.0  
**Proyecto**: Sistema Inteligente SETP Neiva
