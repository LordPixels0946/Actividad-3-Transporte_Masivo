# DOCUMENTO DE PRUEBAS - APRENDIZAJE NO SUPERVISADO
## Sistema de Transporte SETP Neiva

---

## 📋 ÍNDICE DE PRUEBAS

1. [Pruebas de Generación de Datasets](#1-pruebas-de-generación-de-datasets)
2. [Pruebas de Clustering de Usuarios](#2-pruebas-de-clustering-de-usuarios)
3. [Pruebas de Clustering de Estaciones](#3-pruebas-de-clustering-de-estaciones)
4. [Pruebas de Visualización](#4-pruebas-de-visualización)
5. [Pruebas de Calidad de Clusters](#5-pruebas-de-calidad-de-clusters)
6. [Resultados Esperados](#6-resultados-esperados)

---

## 1. PRUEBAS DE GENERACIÓN DE DATASETS

### Prueba 1.1: Generación de Dataset de Usuarios

**Comando**:
```bash
cd No_Supervisado
python generador_dataset.py
```

**Verificaciones**:
- ✅ Se crea archivo `data/dataset_patrones_usuarios.csv`
- ✅ Contiene 2,000 usuarios
- ✅ Tiene 9 columnas
- ✅ No hay valores nulos
- ✅ Distribución esperada de tipos de usuario
- ✅ Rangos válidos:
  - viajes_por_semana: 2-14
  - gasto_mensual: 15,000-120,000
  - hora_promedio_uso: 5-22

**Resultado Esperado**:
```
✓ Generados 2000 usuarios
✓ Guardado en: data/dataset_patrones_usuarios.csv

Distribución real:
Trabajador    ~500
Estudiante    ~500
Ocasional     ~500
Turista       ~500
```

**Estado**: ⏳ Por ejecutar

---

### Prueba 1.2: Generación de Dataset de Estaciones

**Comando**:
```bash
cd No_Supervisado
python generador_dataset.py
```

**Verificaciones**:
- ✅ Se crea archivo `data/dataset_estaciones.csv`
- ✅ Contiene 15 estaciones
- ✅ Tiene 8 columnas
- ✅ Estaciones principales tienen mayor flujo
- ✅ Distribución por zona tipo correcta

**Resultado Esperado**:
```
✓ Generadas 15 estaciones
✓ Guardado en: data/dataset_estaciones.csv

Zona Principal:    ~3 estaciones
Zona Intermedia:   ~4 estaciones
Zona Secundaria:   ~8 estaciones
```

**Estado**: ⏳ Por ejecutar

---

### Prueba 1.3: Generación de Dataset de Rutas

**Comando**:
```bash
cd No_Supervisado
python generador_dataset.py
```

**Verificaciones**:
- ✅ Se crea archivo `data/dataset_rutas_frecuencias.csv`
- ✅ Contiene registros de 15 rutas × 18 horas
- ✅ Tiene 6 columnas
- ✅ Horas pico muestran mayor flujo de pasajeros

**Estado**: ⏳ Por ejecutar

---

## 2. PRUEBAS DE CLUSTERING DE USUARIOS

### Prueba 2.1: Método del Codo para K-Means

**Comando**:
```bash
cd No_Supervisado
python modelo_no_supervisado.py
```

**Verificaciones**:
- ✅ Se genera gráfica de inercia vs k
- ✅ Se genera gráfica de silhouette vs k
- ✅ K óptimo sugerido está entre 3-5
- ✅ Archivo `outputs/optimizacion_k_usuarios.png` creado

**Resultado Esperado**:
```
✓ K óptimo sugerido: 4
```

**Estado**: ⏳ Por ejecutar

---

### Prueba 2.2: K-Means Clustering

**Comando**:
```bash
cd No_Supervisado
python modelo_no_supervisado.py
```

**Verificaciones**:
- ✅ Modelo entrena sin errores
- ✅ Silhouette Score > 0.30
- ✅ Davies-Bouldin Index < 2.0
- ✅ Usuarios distribuidos en todos los clusters
- ✅ No hay clusters con < 50 usuarios

**Métricas Esperadas**:
- Silhouette Score: 0.35-0.55
- Davies-Bouldin Index: 0.8-1.5
- 4 clusters balanceados

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
Silhouette Score: ____
Davies-Bouldin: ____
Distribución: 
  Cluster 0: ____
  Cluster 1: ____
  Cluster 2: ____
  Cluster 3: ____
```

---

### Prueba 2.3: DBSCAN Clustering

**Comando**:
```bash
cd No_Supervisado
python modelo_no_supervisado.py
```

**Verificaciones**:
- ✅ Modelo ejecuta sin errores
- ✅ Encuentra al menos 2 clusters
- ✅ Identifica algunos puntos de ruido (< 10%)
- ✅ Clusters tienen al menos 10 puntos cada uno

**Métricas Esperadas**:
- Clusters encontrados: 3-6
- Puntos de ruido: 5-15%
- Silhouette Score: > 0.25

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
Clusters: ____
Puntos ruido: ____
Silhouette: ____
```

---

### Prueba 2.4: PCA - Reducción de Dimensionalidad

**Comando**:
```bash
cd No_Supervisado
python modelo_no_supervisado.py
```

**Verificaciones**:
- ✅ PCA ejecuta sin errores
- ✅ Varianza explicada PC1 > 25%
- ✅ Varianza explicada PC2 > 15%
- ✅ Varianza total explicada > 50%

**Resultado Esperado**:
```
✓ Varianza PC1: 30-45%
✓ Varianza PC2: 18-30%
✓ Varianza total: 55-70%
```

**Estado**: ⏳ Por ejecutar

---

## 3. PRUEBAS DE CLUSTERING DE ESTACIONES

### Prueba 3.1: Clustering Jerárquico

**Comando**:
```bash
cd No_Supervisado
python modelo_no_supervisado.py
```

**Verificaciones**:
- ✅ Dendrograma se genera correctamente
- ✅ Archivo `outputs/dendrograma_estaciones.png` creado
- ✅ Todas las estaciones aparecen en el dendrograma
- ✅ Muestra agrupamiento lógico (estaciones similares juntas)

**Verificación Visual**:
- Terminal, Centro, Estadio deben estar en grupo similar
- Estaciones secundarias deben agruparse juntas

**Estado**: ⏳ Por ejecutar

---

### Prueba 3.2: K-Means en Estaciones

**Comando**:
```bash
cd No_Supervisado
python modelo_no_supervisado.py
```

**Verificaciones**:
- ✅ Modelo entrena sin errores
- ✅ 3 clusters definidos
- ✅ Silhouette Score > 0.40
- ✅ Cada cluster tiene al menos 3 estaciones

**Agrupamiento Esperado**:
- **Cluster 0 (Principales)**: Terminal, Centro, Estadio
- **Cluster 1 (Intermedias)**: San Mateo, Sevilla, Cándido, Calixto
- **Cluster 2 (Secundarias)**: Resto de estaciones

**Estado**: ⏳ Por ejecutar

**Resultados Reales**:
```
[Se llenarán después de ejecutar]
Cluster 0: ________________
Cluster 1: ________________
Cluster 2: ________________
```

---

## 4. PRUEBAS DE VISUALIZACIÓN

### Prueba 4.1: Optimización K

**Verificaciones**:
- ✅ Archivo `outputs/optimizacion_k_usuarios.png` existe
- ✅ Dos subgráficas: método del codo y silhouette
- ✅ Gráficas muestran tendencia clara
- ✅ Ejes y título correctos

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.2: Clusters en Espacio PCA

**Verificaciones**:
- ✅ Archivo `outputs/clusters_usuarios_pca.png` existe
- ✅ Dos scatter plots: K-Means y DBSCAN
- ✅ Colores distinguen clusters claramente
- ✅ Ejes muestran porcentaje de varianza explicada
- ✅ Clusters visualmente separados

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.3: Perfiles de Clusters

**Verificaciones**:
- ✅ Archivo `outputs/perfiles_clusters_usuarios.png` existe
- ✅ 5 gráficos de barras (uno por feature)
- ✅ Muestra diferencias claras entre clusters
- ✅ Valores son interpretables

**Interpretación Esperada**:
- Un cluster debe mostrar alto `viajes_por_semana` + bajo `numero_rutas` = Trabajadores
- Un cluster debe mostrar bajo `viajes_por_semana` + alto `numero_rutas` = Ocasionales
- Etc.

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.4: Dendrograma de Estaciones

**Verificaciones**:
- ✅ Archivo `outputs/dendrograma_estaciones.png` existe
- ✅ Todas las 15 estaciones visibles
- ✅ Etiquetas legibles (no solapadas)
- ✅ Estructura jerárquica clara

**Estado**: ⏳ Por ejecutar

---

### Prueba 4.5: Características de Estaciones

**Verificaciones**:
- ✅ Archivo `outputs/caracteristicas_estaciones.png` existe
- ✅ 4 gráficos de barras horizontales
- ✅ Colores por cluster facilitan identificación
- ✅ Estaciones ordenadas por valor

**Estado**: ⏳ Por ejecutar

---

## 5. PRUEBAS DE CALIDAD DE CLUSTERS

### Prueba 5.1: Validación con Datos Reales

**Verificaciones**:
- ✅ Tabla de comparación clusters vs tipos reales
- ✅ Hay correspondencia entre clusters y tipos reales
- ✅ Clusters capturan patrones significativos

**Comparación Esperada**:
```
Crosstab tipo_real vs cluster_kmeans:
                Cluster 0  Cluster 1  Cluster 2  Cluster 3
Estudiante          X          -          -          -
Trabajador          -          X          -          -
Ocasional           -          -          X          -
Turista             -          -          -          X
```
(donde X = mayoría de usuarios)

**Estado**: ⏳ Por ejecutar

---

### Prueba 5.2: Métricas de Calidad

**Métricas a Verificar**:

| Algoritmo | Métrica | Valor Mínimo | Valor Esperado | Valor Real |
|-----------|---------|--------------|----------------|------------|
| K-Means Usuarios | Silhouette | 0.30 | 0.35-0.55 | ____ |
| K-Means Usuarios | Davies-Bouldin | - | 0.8-1.5 | ____ |
| DBSCAN Usuarios | Silhouette | 0.25 | 0.30-0.50 | ____ |
| K-Means Estaciones | Silhouette | 0.40 | 0.45-0.65 | ____ |
| PCA | Varianza Total | 50% | 55-70% | ____ |

**Estado**: ⏳ Por ejecutar

---

## 6. RESULTADOS ESPERADOS

### 6.1 Interpretación de Clusters de Usuarios

**Cluster 0 - "Trabajadores Regulares"**:
- viajes_por_semana: 10-14
- hora_promedio_uso: 6-7, 17-19
- gasto_mensual: Alto
- numero_rutas_diferentes: 1-2
- usa_fines_semana: Mayormente No

**Cluster 1 - "Estudiantes"**:
- viajes_por_semana: 8-12
- hora_promedio_uso: 7-8, 13-14
- gasto_mensual: Medio
- numero_rutas_diferentes: 2-3
- usa_fines_semana: Mayormente No

**Cluster 2 - "Usuarios Ocasionales"**:
- viajes_por_semana: 2-5
- hora_promedio_uso: Variable
- gasto_mensual: Bajo
- numero_rutas_diferentes: 3-6
- usa_fines_semana: Variable

**Cluster 3 - "Turistas/Exploradores"**:
- viajes_por_semana: 3-7
- hora_promedio_uso: 10-18
- gasto_mensual: Medio
- numero_rutas_diferentes: 4-8
- usa_fines_semana: Sí

**Estado**: ⏳ Por validar

---

### 6.2 Interpretación de Clusters de Estaciones

**Cluster 0 - "Estaciones Principales"**:
- Flujo alto (> 3000 pasajeros/día)
- Muchas conexiones (> 8)
- Zona comercial
- Ejemplos: Terminal, Centro, Estadio

**Cluster 1 - "Estaciones Intermedias"**:
- Flujo medio (1500-3000 pasajeros/día)
- Conexiones moderadas (5-8)
- Zona mixta
- Ejemplos: San Mateo, Sevilla

**Cluster 2 - "Estaciones Secundarias"**:
- Flujo bajo (< 1500 pasajeros/día)
- Pocas conexiones (< 6)
- Zona residencial
- Ejemplos: Resto de estaciones

**Estado**: ⏳ Por validar

---

## 7. CRITERIOS DE ACEPTACIÓN

### ✅ El sistema pasa las pruebas si:

1. **Datasets**:
   - Se generan sin errores
   - Tienen el tamaño esperado
   - Reflejan distribuciones lógicas

2. **Clustering de Usuarios**:
   - Silhouette Score > 0.30
   - Encuentra 3-5 clusters
   - Clusters tienen interpretación clara
   - Hay correspondencia con tipos reales

3. **Clustering de Estaciones**:
   - Agrupa estaciones similares
   - 3 clusters representan Principal/Intermedia/Secundaria
   - Dendrograma muestra jerarquía lógica

4. **Visualizaciones**:
   - Todos los archivos PNG se generan
   - Son legibles y profesionales
   - Facilitan interpretación de resultados

5. **Calidad General**:
   - Ejecución sin errores
   - Resultados reproducibles
   - Tiempo de ejecución < 3 minutos

---

## 📝 REGISTRO DE EJECUCIÓN

### Ejecución 1
**Fecha**: ___________  
**Ejecutado por**: ___________  
**Silhouette K-Means**: ___________  
**Clusters identificados**: ___________  
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
