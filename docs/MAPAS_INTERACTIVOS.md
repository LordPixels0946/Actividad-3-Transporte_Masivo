# 🗺️ Guía de Mapas Interactivos - SETP Neiva

## Descripción

El sistema ahora incluye visualización de rutas sobre **mapas reales de Neiva** utilizando coordenadas GPS reales y la biblioteca **Folium** con datos de OpenStreetMap.

---

## 🚀 Cómo Usar los Mapas

### Opción 1: Desde el Modo Interactivo

```bash
python main.py
```

1. Al iniciar, el sistema preguntará si deseas ver el mapa de la red completa
2. Después de calcular una ruta, preguntará si deseas verla en un mapa interactivo
3. Los mapas se abren automáticamente en tu navegador predeterminado

### Opción 2: Generar Mapas Directamente

```bash
python generar_mapas.py
```

Este comando genera automáticamente:
- 1 mapa de la red completa con todas las estaciones
- 4 mapas de rutas de ejemplo predefinidas
- Todos se guardan en la carpeta `outputs/`

---

## 🎨 Características de los Mapas

### Elementos Visuales

- **🟢 Marcador Verde**: Estación de origen (icono de play ▶)
- **🔴 Marcador Rojo**: Estación de destino (icono de stop ⏹)
- **🟠 Marcadores Naranjas**: Paradas intermedias (numeradas)
- **🔵 Línea Azul Gruesa**: Ruta óptima seleccionada
- **⚪ Líneas Punteadas Grises**: Otras conexiones de la red (no usadas)

### Información Mostrada

Cada mapa incluye un panel informativo con:
- Origen y destino
- Distancia total en kilómetros
- Tiempo estimado en minutos
- Número de paradas

### Controles Interactivos

Los mapas incluyen:

1. **📍 Zoom y Navegación**: Acerca o aleja el mapa con la rueda del ratón o botones
2. **🗺️ Mini Mapa**: Vista miniatura para ubicación general (esquina inferior izquierda)
3. **⛶ Pantalla Completa**: Botón para maximizar el mapa
4. **📏 Medidor de Distancias**: Herramienta para medir distancias personalizadas
5. **💬 Tooltips**: Pasa el cursor sobre estaciones y rutas para ver información
6. **📌 Popups**: Haz clic en los marcadores para ver detalles completos

---

## 📂 Archivos Generados

Los mapas se guardan como archivos HTML en la carpeta `outputs/` con nombres descriptivos:

```
outputs/
├── mapa_red_completa_20260927_143022.html
├── mapa_ruta_Terminal_Estadio_20260927_143023.html
├── mapa_ruta_San_Mateo_Sevilla_20260927_143024.html
└── ...
```

Cada archivo incluye un timestamp para evitar sobrescrituras.

---

## 🌐 Tecnologías Utilizadas

### Folium
- Biblioteca Python para crear mapas interactivos
- Construida sobre Leaflet.js (JavaScript)
- Genera HTML independiente que funciona sin servidor

### OpenStreetMap
- Mapas colaborativos de código abierto
- Datos geográficos reales de Neiva, Colombia
- Actualización constante por la comunidad

### Coordenadas GPS Reales

Las estaciones del SETP Neiva utilizan coordenadas geográficas reales:

| Estación | Latitud | Longitud |
|----------|---------|----------|
| Terminal | 2.9273 | -75.2819 |
| Calle 7 | 2.9298 | -75.2850 |
| Centro | 2.9342 | -75.2809 |
| Alcaldía | 2.9356 | -75.2795 |
| Quirinal | 2.9410 | -75.2880 |
| Limonar | 2.9450 | -75.2920 |
| Gran Centro | 2.9320 | -75.2770 |
| Calixto | 2.9280 | -75.2740 |
| Estadio | 2.9500 | -75.2850 |
| Cándido | 2.9380 | -75.2730 |
| San Mateo | 2.9240 | -75.2900 |
| Sevilla | 2.9550 | -75.2800 |

---

## 🎯 Casos de Uso

### 1. Visualización Educativa
- Entender la topología de la red de transporte
- Identificar estaciones centrales y periféricas
- Planificar expansiones de la red

### 2. Presentaciones y Reportes
- Incluir mapas en presentaciones (capturas de pantalla o embebidos)
- Generar informes visuales profesionales
- Compartir rutas con otros usuarios

### 3. Análisis de Rutas
- Comparar diferentes rutas visualmente
- Identificar áreas de alta conectividad
- Detectar zonas con poca cobertura

### 4. Validación de Datos
- Verificar que las conexiones tengan sentido geográfico
- Detectar errores en distancias o coordenadas
- Confirmar la lógica del algoritmo A*

---

## 💡 Consejos de Uso

### Navegación en el Mapa

1. **Zoom Inteligente**: El mapa se centra automáticamente para mostrar toda la ruta
2. **Click en Marcadores**: Obtén información detallada de cada estación
3. **Hover sobre Líneas**: Ve distancias y tiempos de cada segmento
4. **Usa el Mini Mapa**: Para contexto geográfico amplio de Neiva

### Compartir Mapas

Los archivos HTML son completamente independientes y pueden:
- Abrirse sin conexión a internet (después de la primera carga)
- Compartirse por correo o servicios en la nube
- Embeberse en sitios web con un `<iframe>`

### Personalización

El archivo `src/mapa_interactivo.py` permite personalizar:
- Colores de las rutas y marcadores
- Zoom inicial
- Estilo del mapa (OpenStreetMap, CartoDB, Stamen, etc.)
- Elementos adicionales (polígonos, círculos, etc.)

---

## 🔧 Solución de Problemas

### El mapa no se abre automáticamente

**Solución**: Abre manualmente el archivo HTML desde la carpeta `outputs/`

### Las coordenadas no son exactas

Las coordenadas son aproximadas para fines educativos. Para coordenadas precisas:
1. Visita [Google Maps](https://www.google.com/maps)
2. Busca cada estación en Neiva
3. Click derecho → "¿Qué hay aquí?"
4. Copia las coordenadas
5. Actualiza `src/base_conocimiento.py`

### El mapa se ve en blanco

**Causas posibles**:
- Falta conexión a internet (primera carga requiere internet)
- Navegador bloqueando JavaScript
- Archivos corruptos

**Solución**: Regenera el mapa con `python generar_mapas.py`

### Quiero cambiar el estilo del mapa

En `src/mapa_interactivo.py`, línea donde se crea el mapa, cambia:

```python
tiles='OpenStreetMap'  # Opciones: 'CartoDB positron', 'CartoDB dark_matter', 'Stamen Terrain'
```

---

## 📚 Recursos Adicionales

- **Documentación de Folium**: https://python-visualization.github.io/folium/
- **OpenStreetMap**: https://www.openstreetmap.org
- **Leaflet.js**: https://leafletjs.com/
- **Coordenadas de Neiva**: https://www.geodatos.net/coordenadas/colombia/neiva

---

## 🎓 Ejemplo Completo de Uso

```bash
# 1. Instalar dependencias (primera vez)
pip install -r requirements.txt

# 2. Generar mapas de ejemplo
python generar_mapas.py

# 3. Usar modo interactivo
python main.py

# Cuando se solicite:
# - Ingresa "s" para ver el mapa de la red completa
# - Elige origen: Terminal
# - Elige destino: Estadio
# - Ingresa "s" para ver la ruta en el mapa

# 4. Los mapas se abren automáticamente en tu navegador
# 5. Encuentra los archivos HTML en la carpeta outputs/
```

---

## ✨ Mejoras Futuras

Ideas para expandir la funcionalidad:

- [ ] Integrar rutas de transporte real de Neiva (si hay APIs disponibles)
- [ ] Añadir información de tráfico en tiempo real
- [ ] Calcular rutas alternativas y mostrarlas en diferentes colores
- [ ] Integrar datos demográficos o estadísticas de uso
- [ ] Crear animaciones de recorrido de la ruta
- [ ] Exportar mapas a PDF o imágenes PNG
- [ ] Modo oscuro para los mapas
- [ ] Agregar puntos de interés cercanos a las estaciones

---

*Última actualización: Septiembre 2026*
