# DESCRIPCIÓN DE DATOS - APRENDIZAJE NO SUPERVISADO
## Sistema de Transporte SETP Neiva

---

## 📊 DATASETS GENERADOS

### 1. Dataset de Patrones de Usuarios (`dataset_patrones_usuarios.csv`)

**Propósito**: Clustering para identificar perfiles de usuarios del SETP

**Tamaño**: 2,000 usuarios

**Variables (Features)**:

| Variable | Tipo | Descripción | Rango |
|----------|------|-------------|-------|
| `usuario_id` | Identificador | ID único del usuario | 1-2000 |
| `viajes_por_semana` | Numérica | Número de viajes semanales | 2-14 |
| `hora_promedio_uso` | Numérica | Hora típica de uso | 5-22 |
| `gasto_mensual` | Numérica | Gasto mensual en COP | 15,000-120,000 |
| `numero_rutas_diferentes` | Numérica | Rutas únicas utilizadas | 1-8 |
| `usa_fines_semana` | Binaria | Usa servicio en fin de semana | 0, 1 |
| `tiempo_promedio_viaje_min` | Numérica | Tiempo promedio de viaje | 15-45 min |
| `distancia_promedio_km` | Numérica | Distancia promedio recorrida | 3-15 km |
| `tipo_real` | Categórica | Tipo real (para validación) | Estudiante, Trabajador, Ocasional, Turista |

**Perfiles de usuarios esperados**:

1. **Estudiantes**
   - Viajes frecuentes (8-12/semana)
   - Horarios escolares (7-8am, 1-2pm, 5-6pm)
   - Gasto moderado (40,000-80,000 COP)
   - Pocas rutas (2-3)

2. **Trabajadores**
   - Viajes muy frecuentes (10-14/semana)
   - Horarios laborales (6-7am, 5-7pm)
   - Gasto alto (60,000-120,000 COP)
   - Muy pocas rutas (1-2, consistentes)

3. **Ocasionales**
   - Viajes esporádicos (2-5/semana)
   - Horarios variables
   - Gasto bajo (15,000-40,000 COP)
   - Muchas rutas diferentes (3-6)

4. **Turistas**
   - Viajes moderados (3-7/semana)
   - Horarios medios (10am-6pm)
   - Gasto medio (20,000-60,000 COP)
   - Muchas rutas (4-8, exploratorio)

---

### 2. Dataset de Estaciones (`dataset_estaciones.csv`)

**Propósito**: Clustering para agrupar estaciones por similitud operacional

**Tamaño**: 15 estaciones

**Variables (Features)**:

| Variable | Tipo | Descripción | Rango |
|----------|------|-------------|-------|
| `estacion` | Identificador | Nombre de la estación | 15 estaciones |
| `flujo_pasajeros_diario` | Numérica | Pasajeros por día | 500-5000 |
| `numero_conexiones` | Numérica | Rutas conectadas | 3-12 |
| `comercios_proximos` | Numérica | Comercios cercanos | 5-100 |
| `tiempo_espera_promedio_min` | Numérica | Tiempo de espera | 3-15 min |
| `area_cobertura_km2` | Numérica | Área de cobertura | 0.5-3.0 km² |
| `tarifa_promedio` | Numérica | Tarifa promedio en COP | 1500-2500 |
| `zona_tipo_real` | Categórica | Tipo de zona (validación) | Principal, Intermedia, Secundaria |

**Tipos de estaciones esperadas**:

1. **Estaciones Principales**
   - Alto flujo (3000-5000 pasajeros/día)
   - Muchas conexiones (8-12)
   - Zona comercial (50-100 comercios)
   - Ejemplos: Terminal, Centro, Estadio

2. **Estaciones Intermedias**
   - Flujo medio (1500-3000 pasajeros/día)
   - Conexiones moderadas (5-8)
   - Zona mixta (20-50 comercios)
   - Ejemplos: San Mateo, Sevilla, Cándido

3. **Estaciones Secundarias**
   - Flujo bajo (500-1500 pasajeros/día)
   - Pocas conexiones (3-6)
   - Zona residencial (5-20 comercios)
   - Ejemplos: Limonar, Granjas, Quirinal

---

### 3. Dataset de Rutas y Frecuencias (`dataset_rutas_frecuencias.csv`)

**Propósito**: Análisis de patrones temporales y clustering de comportamiento de rutas

**Tamaño**: ~5,000 registros (15 rutas × 18 horas × variaciones)

**Variables (Features)**:

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `ruta_origen` | Categórica | Estación de origen |
| `ruta_destino` | Categórica | Estación de destino |
| `hora` | Numérica | Hora del día (5-22) |
| `pasajeros_hora` | Numérica | Pasajeros por hora |
| `ocupacion_promedio` | Numérica | % de ocupación (0-1) |
| `velocidad_promedio_kmh` | Numérica | Velocidad promedio |

**Rutas principales incluidas**:
1. Terminal - Estadio
2. Terminal - Centro
3. Estadio - San Mateo
4. Centro - Sevilla
5. San Mateo - Sevilla
6. Sevilla - La Toma
7. Centro - Cándido
8. Y 8 rutas más...

---

## 🎯 PROBLEMAS A RESOLVER

### Problema 1: Segmentación de Usuarios
**Objetivo**: Identificar grupos de usuarios con comportamientos similares

**Algoritmos utilizados**:
1. **K-Means Clustering**
   - Agrupa usuarios en k grupos
   - Método del codo para determinar k óptimo
   - Silhouette score para evaluar calidad

2. **DBSCAN**
   - Identifica clusters de densidad
   - Detecta usuarios atípicos (outliers)
   - No requiere especificar k a priori

3. **PCA (Principal Component Analysis)**
   - Reduce dimensionalidad para visualización
   - Proyecta datos a 2D
   - Mantiene máxima varianza

**Métricas de evaluación**:
- Silhouette Score (calidad de clusters)
- Davies-Bouldin Index (separación)
- Comparación con tipos reales

---

### Problema 2: Agrupación de Estaciones
**Objetivo**: Clasificar estaciones según características operacionales

**Algoritmos utilizados**:
1. **K-Means Clustering**
   - Agrupa estaciones similares
   - 3 grupos: Principal, Intermedia, Secundaria

2. **Clustering Jerárquico**
   - Dendrograma para visualizar relaciones
   - Método Ward para minimizar varianza

**Aplicaciones**:
- Estrategias diferenciadas por tipo
- Asignación de recursos
- Planificación de mantenimiento

---

## 📈 APLICACIONES PRÁCTICAS

1. **Marketing personalizado**: Ofertas según perfil de usuario
2. **Optimización de recursos**: Asignar personal según tipo de estación
3. **Detección de anomalías**: Identificar usuarios con patrones inusuales
4. **Planificación estratégica**: Entender tipos de demanda
5. **Mejora de servicio**: Adaptar frecuencias según clusters de rutas

---

## 🔄 PREPROCESAMIENTO APLICADO

1. **Normalización**:
   - StandardScaler para todas las features numéricas
   - Escala media=0, desviación=1

2. **Reducción de dimensionalidad**:
   - PCA para visualización en 2D
   - Mantiene >70% de varianza explicada

3. **Sin división train/test**:
   - Aprendizaje no supervisado usa todos los datos
   - Validación mediante métricas internas

---

## 📝 NOTAS

- Datos sintéticos basados en patrones de transporte urbano real
- `tipo_real` y `zona_tipo_real` son etiquetas de validación (no se usan en clustering)
- Variabilidad aleatoria simula incertidumbre del mundo real
- Semilla aleatoria (42) garantiza reproducibilidad

---

**Fecha de generación**: 2026-09-27  
**Versión**: 1.0  
**Proyecto**: Sistema Inteligente SETP Neiva
