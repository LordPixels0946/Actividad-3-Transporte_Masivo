# DESCRIPCIÓN DE DATOS - APRENDIZAJE SUPERVISADO
## Sistema de Transporte SETP Neiva

---

## 📊 DATASETS GENERADOS

### 1. Dataset de Demanda de Pasajeros (`dataset_demanda_pasajeros.csv`)

**Propósito**: Clasificación de la demanda en estaciones del SETP

**Tamaño**: 10,000 registros

**Variables de Entrada (Features)**:

| Variable | Tipo | Descripción | Rango |
|----------|------|-------------|-------|
| `hora` | Numérica | Hora del día (24h) | 5-22 |
| `dia_semana` | Categórica | Día de la semana | 0-6 (0=Lunes, 6=Domingo) |
| `estacion` | Categórica | Nombre de la estación SETP | 10 estaciones |
| `clima` | Categórica | Condición climática | Soleado, Lluvioso, Nublado |
| `temperatura` | Numérica | Temperatura en °C | 22-35 |
| `evento_especial` | Binaria | Presencia de evento especial | 0 (No), 1 (Sí) |
| `num_pasajeros` | Numérica | Número de pasajeros | 10-300 |

**Variable Objetivo (Target)**:
- `demanda`: Clasificación categórica
  - **Baja**: 10-50 pasajeros
  - **Media**: 51-150 pasajeros
  - **Alta**: 151-300 pasajeros

**Estaciones incluidas**:
- Terminal
- Estadio
- San Mateo
- Sevilla
- La Toma
- Centro
- Cándido
- Calixto
- Alcalá
- Miraflores

**Lógica de generación**:
- **Horas pico** (6-8am, 12-2pm, 5-7pm): Mayor demanda
- **Días laborales** (Lunes-Viernes): Mayor flujo que fines de semana
- **Estaciones principales** (Terminal, Centro, Estadio): Mayor afluencia
- **Clima lluvioso**: Incrementa demanda
- **Eventos especiales**: Aumentan significativamente la demanda

---

### 2. Dataset de Tiempos de Viaje (`dataset_tiempos_viaje.csv`)

**Propósito**: Regresión para predecir tiempos de viaje entre estaciones

**Tamaño**: 5,000 registros

**Variables de Entrada (Features)**:

| Variable | Tipo | Descripción | Rango |
|----------|------|-------------|-------|
| `origen` | Categórica | Estación de origen | 10 estaciones |
| `destino` | Categórica | Estación de destino | 10 estaciones |
| `hora` | Numérica | Hora del viaje | 5-22 |
| `dia_semana` | Categórica | Día de la semana | 0-6 |
| `clima` | Categórica | Condición climática | Soleado, Lluvioso, Nublado |
| `trafico` | Categórica | Nivel de tráfico | Bajo, Medio, Alto |
| `num_paradas` | Numérica | Número de paradas en ruta | 3-10 |

**Variable Objetivo (Target)**:
- `tiempo_viaje_minutos`: Tiempo de viaje en minutos (continua)

**Rutas principales incluidas**:
1. Terminal - Estadio (15-25 min base)
2. Terminal - Centro (20-30 min base)
3. Estadio - San Mateo (10-18 min base)
4. Centro - Sevilla (12-20 min base)
5. San Mateo - Sevilla (8-15 min base)
6. Y más combinaciones...

**Factores que afectan el tiempo**:
- **Horas pico**: +40% tiempo
- **Días laborales**: +20% tiempo
- **Clima lluvioso**: +30% tiempo
- **Tráfico alto**: +50% tiempo
- **Número de paradas**: +0.5-1.5 min por parada

---

## 🎯 PROBLEMAS A RESOLVER

### Problema 1: Clasificación de Demanda
**Objetivo**: Predecir si la demanda en una estación será Baja, Media o Alta

**Algoritmos utilizados**:
1. **Árbol de Decisión**
   - Interpretable y visual
   - Muestra reglas de decisión claras
   - Ideal para entender qué factores influyen más

2. **Random Forest**
   - Mayor precisión que árbol simple
   - Robusto ante overfitting
   - Proporciona importancia de features

**Métricas de evaluación**:
- Exactitud (Accuracy)
- Precisión, Recall, F1-Score por clase
- Matriz de confusión

### Problema 2: Predicción de Tiempos de Viaje
**Objetivo**: Predecir el tiempo de viaje en minutos entre dos estaciones

**Algoritmos utilizados**:
1. **Regresión Lineal**
   - Modelo base simple
   - Relaciones lineales entre variables
   
2. **Random Forest Regressor**
   - Captura relaciones no lineales
   - Mejor para datos complejos

**Métricas de evaluación**:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² (Coeficiente de determinación)

---

## 📈 APLICACIONES PRÁCTICAS

1. **Optimización de flota**: Asignar buses según demanda predicha
2. **Planificación de rutas**: Ajustar frecuencias en horas pico
3. **Información a usuarios**: Estimar tiempos de viaje precisos
4. **Gestión de recursos**: Personal extra en estaciones con alta demanda
5. **Análisis de impacto**: Evaluar efectos de eventos o clima

---

## 🔄 PREPROCESAMIENTO APLICADO

1. **Codificación de variables categóricas**:
   - Label Encoding para variables ordinales
   - One-Hot Encoding para variables nominales

2. **Normalización**:
   - StandardScaler para features numéricas

3. **División de datos**:
   - 75% entrenamiento
   - 25% prueba
   - Estratificación para mantener balance de clases

---

## 📝 NOTAS

- Los datos son sintéticos pero basados en patrones reales de transporte
- Se incluye variabilidad aleatoria para simular incertidumbre real
- Los factores y pesos fueron calibrados para reflejar comportamiento real del SETP
- Semilla aleatoria fijada (42) para reproducibilidad

---

**Fecha de generación**: 2026-09-27  
**Versión**: 1.0  
**Proyecto**: Sistema Inteligente SETP Neiva
