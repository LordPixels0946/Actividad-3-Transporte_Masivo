# 🚍 Sistema Inteligente de Rutas - SETP Neiva

Sistema avanzado de búsqueda de rutas óptimas con análisis profesional, visualizaciones de red y comparativas internacionales para el Sistema Estratégico de Transporte Público de Neiva.

## 🌟 Características Principales

### 🧠 Motor Inteligente
- **Algoritmo A*** con heurística euclidiana optimizada
- Base de conocimiento con 12 estaciones y 16 conexiones reales
- Búsqueda óptima garantizada con métricas de rendimiento

### 🗺️ **Mapas Interactivos**
- **Visualización sobre mapas reales de Neiva** con OpenStreetMap
- **Coordenadas GPS reales** de todas las estaciones
- **Mapas HTML interactivos** con zoom, tooltips y navegación
- **Controles profesionales**: minimapa, pantalla completa, medidor de distancias
- Colores diferenciados:R origen verde, destino rojo, paradas naranja
- Ver ruta óptima sobre el contexto geográfico real de la ciudad

### 📊 Análisis Profesional
- **Reportes Excel** completos con 7 hojas de análisis
- **Gráficos de alta calidad** (300 DPI) tipo red de tráfico
- **Análisis de centralidad** de estaciones (grado, intermediación, cercanía)
- **Mapas de calor** de conectividad
- **Métricas de rendimiento** en tiempo real

### 🌎 Comparación Internacional
- Comparación con 8 sistemas BRT de Latinoamérica
- Gráficos comparativos multi-criterio
- Análisis de posicionamiento y rankings
- Estadísticas poblacionales y de cobertura

### 📈 Visualizaciones Avanzadas
- Red completa con coordenadas geográficas
- Rutas individuales resaltadas
- Análisis de tráfico y flujos
- Gráficos comparativos de rutas

## 🚀 Inicio Rápido

### Instalación

```bash
# 1. Clonar o descargar el repositorio
git clone <url-repositorio>

# 2. Entrar al directorio
cd "Actividad 3 Transporte Masivo"

# 3. Instalar dependencias (incluye folium para mapas)
pip install -r requirements.txt
```

### Uso Básico

#### 1️⃣ Interfaz Interactiva con Mapas 🗺️ (Recomendado)

```bash
python main.py
```

**Flujo de uso:**
1. Opción de ver el mapa de la red completa al inicio
2. Selecciona estación de **origen** (ej: Terminal)
3. Selecciona estación de **destino** (ej: Estadio)
4. El sistema **calcula la ruta óptima** con algoritmo A*
5. Muestra el resultado en consola (ruta, distancia, tiempo)
6. **Pregunta si deseas ver el mapa interactivo en el navegador**
7. El mapa se genera y abre automáticamente con la ruta sobre el mapa real de Neiva

**Resultado:** Archivo HTML interactivo en `outputs/` que puedes compartir

#### 2️⃣ Generar Mapas Automáticamente

```bash
python generar_mapas.py
```

**Genera automáticamente:**
- 1 mapa de la red completa del SETP
- 4 mapas de rutas de ejemplo predefinidas
- Todos como archivos HTML interactivos en `outputs/`

#### 3. Análisis Completo

```bash
python generar_analisis_completo.py
```

Genera todo el análisis profesional:
- 6+ gráficos PNG (red, rutas, comparativas)
- 2 reportes Excel (SETP + comparativa internacional)
- Informes de texto (métricas, posicionamiento)
- Logs de rendimiento

#### 3. Pruebas Automatizadas

```bash
python src/test_sistema.py
```

Ejecuta suite de 8 pruebas automatizadas.

## 📁 Estructura del Proyecto

```
.
├── src/                           # Código fuente
│   ├── base_conocimiento.py      # Base de datos de red
│   ├── algoritmo_a_estrella.py   # Motor A*
│   ├── interfaz_usuario.py       # CLI interactiva
│   ├── mapa_interactivo.py       # 🗺️ NUEVO: Mapas con Folium
│   ├── visualizador.py           # Gráficos NetworkX
│   ├── analizador_excel.py       # Reportes Excel
│   ├── logger_metricas.py        # Sistema de logging
│   ├── comparador_ciudades.py    # Análisis internacional
│   └── test_sistema.py           # Suite de pruebas
├── outputs/                       # Archivos generados
│   ├── *.png                     # Gráficos
│   ├── *.xlsx                    # Reportes Excel
│   ├── *.html                    # 🗺️ NUEVO: Mapas interactivos
│   └── logs/                     # Logs y métricas
├── data/                          # Datos auxiliares
├── docs/                          # Documentación completa
│   ├── README.md                 # Guía detallada
│   ├── ARQUITECTURA.md           # Diseño técnico
│   ├── commands.md               # Comandos actualizados
│   └── MAPAS_INTERACTIVOS.md     # 🗺️ NUEVO: Guía de mapas
├── main.py                        # Entrada principal
├── generar_analisis_completo.py  # Análisis completo
├── generar_mapas.py               # 🗺️ NUEVO: Generador de mapas
├── NUEVA_FUNCIONALIDAD.md         # 🗺️ NUEVO: Resumen de cambios
└── requirements.txt               # Dependencias Python (incluye folium)
```

## 📊 Ejemplos de Salida

### Terminal Interactiva

```
============================================================
  SISTEMA INTELIGENTE DE RUTAS - SETP NEIVA
============================================================

Ingrese estación de ORIGEN: Terminal
Ingrese estación de DESTINO: Estadio

🔍 Buscando ruta óptima...

RUTA ÓPTIMA ENCONTRADA:
  ▶ Terminal (Origen)
  ▶ Calle 7
  ▶ Centro
  ▶ Alcaldía
  ▶ Quirinal
  ▶ Estadio (Destino)

Número de paradas: 5
Distancia total: 5.90 km
Tiempo estimado: 20 minutos
```

### Análisis Completo

```
ANÁLISIS COMPLETADO EXITOSAMENTE
============================================================

📁 Archivos generados:
   • 6 gráficos de red y rutas (PNG 300 DPI)
   • 1 reporte Excel completo (7 hojas)
   • 3 gráficos de comparación internacional
   • 1 tabla comparativa Excel con rankings
   • 1 informe de posicionamiento
   • 1 reporte de métricas de rendimiento
   • 8 rutas óptimas analizadas

⏱️  Tiempo total: 3.45 segundos

🔝 Top 5 Estaciones Más Importantes:
   1. Centro: 0.8234
   2. Alcaldía: 0.7891
   3. Quirinal: 0.7456
   ...
```

## 🔍 Detalles Técnicos

### Algoritmo A*

- **Función de evaluación**: f(n) = g(n) + h(n)
- **Heurística**: Distancia euclidiana en coordenadas geográficas
- **Garantía**: Optimalidad con heurística admisible
- **Complejidad**: O(b^d) tiempo y espacio

### Visualizaciones

- **NetworkX** para análisis de grafos
- **Matplotlib** para renderizado
- **Seaborn** para estilos profesionales
- **Coordenadas reales** de Neiva, Colombia

### Análisis Excel

- **7 hojas de análisis**:
  1. Resumen de red
  2. Detalle de estaciones
  3. Matriz de conexiones
  4. Análisis de centralidad
  5. Matriz de distancias
  6. Resultados de búsquedas
  7. Estadísticas generales
  
- **Formato profesional** con colores, bordes y ajuste automático

### Comparación Internacional

Incluye datos de:
- Bogotá (TransMilenio)
- Medellín (Metro)
- Cali (MIO)
- Curitiba (RIT)
- Ciudad de México (Metrobús)
- Lima (Metropolitano)
- Santiago (Transantiago)

## 📦 Dependencias

- **Python 3.6+**
- **NetworkX** - Análisis de grafos
- **Matplotlib** - Gráficos
- **Pandas** - Análisis de datos
- **OpenPyXL** - Excel
- **NumPy** - Cálculos numéricos

Ver `requirements.txt` para lista completa.

## 📖 Documentación Completa

- **[docs/README.md](docs/README.md)** - Guía de usuario completa
- **[docs/ARQUITECTURA.md](docs/ARQUITECTURA.md)** - Diseño técnico detallado
- **[docs/commands.md](docs/commands.md)** - Comandos Git y casos de prueba

## 🧪 Testing

```bash
# Pruebas automatizadas
python src/test_sistema.py

# Resultados esperados:
# ✅ 8/8 pruebas exitosas (100%)
```

## 📝 Logs y Métricas

El sistema registra automáticamente:
- Tiempo de ejecución de cada búsqueda
- Generación de visualizaciones
- Creación de reportes
- Estadísticas de uso

Archivos en `outputs/logs/`:
- `setp_YYYYMMDD.log` - Log detallado
- `metricas.json` - Métricas en JSON
- `reporte_metricas.txt` - Resumen de métricas

## 🎯 Casos de Uso

1. **Planificación urbana**: Análisis de centralidad de estaciones
2. **Optimización de rutas**: Búsqueda A* con garantía de optimalidad
3. **Estudios comparativos**: Benchmarking con ciudades similares
4. **Reportes ejecutivos**: Excel profesional con múltiples análisis
5. **Presentaciones**: Gráficos de alta calidad para informes

## 🔧 Configuración Avanzada

### Agregar Nuevas Estaciones

Editar `src/base_conocimiento.py`:

```python
self.estaciones['Nueva_Estacion'] = {'lat': 2.9500, 'lon': -75.2800}
self.conexiones.append(('Estacion_A', 'Nueva_Estacion', 1.5, 5))
```

### Personalizar Visualizaciones

Editar `src/visualizador.py` para ajustar:
- Colores y estilos
- Tamaño de nodos
- Grosor de aristas
- Resolución de salida

## 🤝 Contribuciones

Este es un proyecto académico. Para mejoras:
1. Fork del repositorio
2. Crear rama feature
3. Commit de cambios
4. Push y Pull Request

## 📄 Licencia

Proyecto académico - Universidad

## 👥 Autor

Desarrollado para el curso de Inteligencia Artificial - 2026

## 🆘 Soporte

Para problemas o preguntas:
1. Revisar `docs/` para documentación completa
2. Ejecutar con `--help` para opciones
3. Verificar logs en `outputs/logs/`

---

**Versión**: 2.0  
**Fecha**: Septiembre 2026  
**Python**: 3.6+  
**Estado**: ✅ Producción
