# APRENDIZAJE NO SUPERVISADO - SETP NEIVA
## Actividad 4: Métodos de Aprendizaje No Supervisado

---

## 📖 DESCRIPCIÓN DEL PROYECTO

Este módulo implementa modelos de **aprendizaje no supervisado** para el Sistema de Transporte Público SETP de Neiva, Colombia. Se desarrollan técnicas de clustering y reducción de dimensionalidad para:

1. **Segmentación de Usuarios**: Identificar perfiles de usuarios del SETP
2. **Agrupación de Estaciones**: Clasificar estaciones según características operacionales
3. **Análisis de Patrones**: Descubrir patrones ocultos en datos de transporte

---

## 🗂️ ESTRUCTURA DE ARCHIVOS

```
No_Supervisado/
├── README.md                           # Este archivo
├── DESCRIPCION_DATOS.md                # Descripción detallada de datasets
├── PRUEBAS.md                          # Documento de pruebas y validación
├── generador_dataset.py                # Genera datasets sintéticos
├── modelo_no_supervisado.py            # Implementación de modelos ML
├── data/                               # Carpeta para datasets
│   ├── dataset_patrones_usuarios.csv   # 2,000 usuarios
│   ├── dataset_estaciones.csv          # 15 estaciones
│   └── dataset_rutas_frecuencias.csv   # Frecuencias por ruta/hora
└── outputs/                            # Carpeta para resultados
    ├── optimizacion_k_usuarios.png
    ├── clusters_usuarios_pca.png
    ├── perfiles_clusters_usuarios.png
    ├── dendrograma_estaciones.png
    └── caracteristicas_estaciones.png
```

---

## 🚀 INSTALACIÓN Y REQUISITOS

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalar Dependencias

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

O desde el directorio raíz del proyecto:

```bash
pip install -r requirements.txt
```

---

## 💻 CÓMO USAR

### Paso 1: Generar Datasets

```bash
cd No_Supervisado
python generador_dataset.py
```

**Salida**:
- `data/dataset_patrones_usuarios.csv` (2,000 usuarios)
- `data/dataset_estaciones.csv` (15 estaciones)
- `data/dataset_rutas_frecuencias.csv` (~5,000 registros)

---

### Paso 2: Aplicar Clustering y Análisis

```bash
python modelo_no_supervisado.py
```

**Salida**:
- Métricas de clustering en consola
- 5 visualizaciones en carpeta `outputs/`
- Análisis de perfiles de clusters

---

## 📊 ALGORITMOS IMPLEMENTADOS

### 1. Clustering de Usuarios

#### K-Means
- **Objetivo**: Segmentar usuarios en grupos homogéneos
- **Método**: Optimización de k con método del codo
- **Métricas**: Silhouette Score, Davies-Bouldin Index
- **K óptimo**: 4 clusters

#### DBSCAN
- **Objetivo**: Detectar clusters de densidad y outliers
- **Parámetros**: eps=0.5, min_samples=10
- **Ventajas**: No requiere k, detecta ruido

#### PCA (Análisis de Componentes Principales)
- **Objetivo**: Reducción de dimensionalidad para visualización
- **Componentes**: 2 (PC1 y PC2)
- **Varianza explicada**: >50%

---

### 2. Clustering de Estaciones

#### K-Means
- **Objetivo**: Agrupar estaciones similares
- **K**: 3 clusters (Principal, Intermedia, Secundaria)
- **Features**: Flujo, conexiones, comercios, espera, área, tarifa

#### Clustering Jerárquico
- **Método**: Ward (minimiza varianza intra-cluster)
- **Visualización**: Dendrograma
- **Ventaja**: Muestra jerarquía de similitud

---

## 📈 RESULTADOS ESPERADOS

### Segmentación de Usuarios

**Cluster 0 - Trabajadores Regulares** (~25%)
- Viajes frecuentes (10-14/semana)
- Horarios laborales (6-7am, 5-7pm)
- Gasto alto, pocas rutas

**Cluster 1 - Estudiantes** (~25%)
- Viajes frecuentes (8-12/semana)
- Horarios escolares (7-8am, 1-2pm)
- Gasto medio, rutas limitadas

**Cluster 2 - Usuarios Ocasionales** (~25%)
- Viajes esporádicos (2-5/semana)
- Horarios variables
- Gasto bajo, muchas rutas

**Cluster 3 - Turistas/Exploradores** (~25%)
- Viajes moderados (3-7/semana)
- Horarios medios (10am-6pm)
- Muchas rutas diferentes

### Agrupación de Estaciones

**Cluster 0 - Principales**
- Terminal, Centro, Estadio
- Flujo >3000 pasajeros/día
- Muchas conexiones

**Cluster 1 - Intermedias**
- San Mateo, Sevilla, Cándido
- Flujo 1500-3000 pasajeros/día
- Conexiones moderadas

**Cluster 2 - Secundarias**
- Resto de estaciones
- Flujo <1500 pasajeros/día
- Pocas conexiones

---

## 📊 VISUALIZACIONES GENERADAS

### 1. Optimización K (`optimizacion_k_usuarios.png`)
- Método del codo (inercia vs k)
- Silhouette score vs k
- Determinación de k óptimo

### 2. Clusters en PCA (`clusters_usuarios_pca.png`)
- Proyección 2D de usuarios
- Comparación K-Means vs DBSCAN
- Colores por cluster

### 3. Perfiles de Clusters (`perfiles_clusters_usuarios.png`)
- Características promedio por cluster
- 5 gráficos de barras comparativos
- Identificación de patrones

### 4. Dendrograma (`dendrograma_estaciones.png`)
- Clustering jerárquico de estaciones
- Visualización de similitudes
- Identificación de grupos

### 5. Características de Estaciones (`caracteristicas_estaciones.png`)
- 4 métricas clave por estación
- Colores por cluster
- Comparación visual

---

## 🔍 VARIABLES Y FEATURES

### Dataset de Usuarios

**Features para Clustering**:
- `viajes_por_semana`: Frecuencia de uso
- `hora_promedio_uso`: Horario típico
- `gasto_mensual`: Inversión en transporte
- `numero_rutas_diferentes`: Diversidad de uso
- `usa_fines_semana`: Patrón semanal
- `tiempo_promedio_viaje_min`: Duración típica
- `distancia_promedio_km`: Distancia recorrida

**Validación**: `tipo_real` (no se usa en clustering)

### Dataset de Estaciones

**Features para Clustering**:
- `flujo_pasajeros_diario`: Demanda
- `numero_conexiones`: Conectividad
- `comercios_proximos`: Entorno comercial
- `tiempo_espera_promedio_min`: Servicio
- `area_cobertura_km2`: Alcance geográfico
- `tarifa_promedio`: Costo

**Validación**: `zona_tipo_real` (no se usa en clustering)

---

## 🧪 PRUEBAS Y VALIDACIÓN

Ver documento completo: [`PRUEBAS.md`](PRUEBAS.md)

**Ejecutar pruebas**:
```bash
# Generar datasets
python generador_dataset.py

# Aplicar clustering
python modelo_no_supervisado.py

# Verificar archivos de salida
ls -l data/
ls -l outputs/
```

### Métricas de Calidad

| Métrica | Valor Esperado | Interpretación |
|---------|----------------|----------------|
| Silhouette Score | 0.35-0.55 | Calidad de separación |
| Davies-Bouldin | 0.8-1.5 | Compacidad de clusters |
| Varianza PCA | >50% | Información preservada |

---

## 📚 REFERENCIAS

- Palma Méndez, J. T. (2008). *Inteligencia artificial: métodos, técnicas y aplicaciones*. Madrid: McGraw-Hill España. Capítulo 16: Técnicas de agrupamiento.
- Scikit-learn Documentation: https://scikit-learn.org/
- K-Means, DBSCAN, PCA, Hierarchical Clustering

---

## 🎯 APLICACIONES PRÁCTICAS

### 1. Marketing Personalizado
- Ofertas específicas por perfil de usuario
- Promociones adaptadas a cada cluster
- Programas de fidelización

### 2. Optimización Operativa
- Asignar recursos según tipo de estación
- Frecuencias ajustadas por cluster
- Personal extra en estaciones principales

### 3. Planificación Estratégica
- Entender demanda por segmento
- Nuevas rutas según necesidades de clusters
- Expansión basada en patrones

### 4. Detección de Anomalías
- Identificar usuarios con comportamiento atípico
- Detectar fraude o mal uso
- Monitorear cambios en patrones

### 5. Mejora de Servicio
- Servicios diferenciados por tipo de usuario
- Infraestructura según cluster de estación
- Horarios optimizados por perfil

---

## 🔬 METODOLOGÍA

### Preprocesamiento
1. Normalización con StandardScaler
2. Features numéricas estandarizadas
3. Sin división train/test (usa todos los datos)

### Clustering
1. Determinar k óptimo con método del codo
2. Aplicar K-Means y DBSCAN
3. Evaluar con métricas internas

### Visualización
1. Reducción con PCA a 2D
2. Proyección de clusters
3. Análisis de perfiles

### Validación
1. Comparar con etiquetas reales
2. Interpretar clusters
3. Verificar coherencia

---

## 👥 EQUIPO

- **Integrante 1**: [Nombre]
- **Integrante 2**: [Nombre]
- **Integrante 3**: [Nombre]

---

## 📝 NOTAS IMPORTANTES

- **Aprendizaje no supervisado**: No requiere etiquetas
- `tipo_real` y `zona_tipo_real` son solo para **validación**
- Los modelos descubren patrones **automáticamente**
- Semilla aleatoria (42) garantiza **reproducibilidad**
- Resultados interpretables y accionables

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: ModuleNotFoundError
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
```

### Error: Carpeta 'data' no existe
```bash
mkdir data outputs
python generador_dataset.py
```

### Silhouette Score bajo (<0.20)
- Ajustar parámetros de clustering
- Probar diferentes valores de k
- Revisar normalización de datos

### DBSCAN no encuentra clusters
- Ajustar parámetro `eps` (probar 0.3-0.8)
- Modificar `min_samples` (5-20)
- Verificar escala de datos

---

## 📧 CONTACTO

**Proyecto**: Sistema Inteligente SETP Neiva  
**Curso**: Inteligencia Artificial  
**Fecha**: 2026-09-27  
**Versión**: 1.0

---

## 📄 LICENCIA

Este proyecto es parte de una actividad académica para el curso de Inteligencia Artificial.
