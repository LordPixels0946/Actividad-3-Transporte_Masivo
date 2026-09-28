# 🎉 Nueva Funcionalidad: Mapas Interactivos con Geolocalización

## 📋 Resumen de Cambios

Se ha implementado una **visualización profesional de rutas sobre mapas reales de Neiva** con las siguientes características:

### ✨ Características Nuevas

1. **Mapas Interactivos con Folium**
   - Visualización sobre OpenStreetMap
   - Coordenadas GPS reales de Neiva, Colombia
   - Mapas HTML independientes y compartibles

2. **Visualización Profesional**
   - Colores diferenciados por tipo (origen verde, destino rojo, paradas naranja)
   - Línea de ruta destacada en azul
   - Red completa visible en segundo plano
   - Panel informativo con métricas clave

3. **Controles Interactivos**
   - Minimapa para contexto geográfico
   - Modo pantalla completa
   - Herramienta de medición de distancias
   - Tooltips y popups informativos
   - Zoom y navegación fluida

---

## 📁 Archivos Nuevos Creados

```
src/
└── mapa_interactivo.py       # Módulo para generar mapas con Folium

generar_mapas.py               # Script para generar mapas automáticamente

docs/
└── MAPAS_INTERACTIVOS.md      # Documentación completa de mapas
```

## 📝 Archivos Modificados

```
src/interfaz_usuario.py        # Añadida integración con mapas
docs/commands.md               # Actualizados comandos con mapas
requirements.txt               # Ya incluía folium
```

---

## 🚀 Cómo Usar

### Opción 1: Modo Interactivo (Recomendado)

```bash
python main.py
```

**Flujo de uso:**
1. Pregunta si deseas ver el mapa de la red completa → Responde `s` o `n`
2. Selecciona estación de origen
3. Selecciona estación de destino
4. Ve el resultado en consola
5. Pregunta si deseas ver el mapa interactivo → Responde `s` para abrir
6. El mapa se abre automáticamente en tu navegador

### Opción 2: Generar Múltiples Mapas

```bash
python generar_mapas.py
```

**Genera automáticamente:**
- 1 mapa de la red completa
- 4 mapas de rutas de ejemplo:
  - Terminal → Estadio
  - San Mateo → Sevilla
  - Calle 7 → Limonar
  - Centro → Calixto

---

## 🗺️ Ejemplo de Salida

Cuando ejecutas `python generar_mapas.py`:

```
============================================================
  GENERADOR DE MAPAS INTERACTIVOS - SETP NEIVA
============================================================

📍 1. Generando mapa de la red completa...
✅ Mapa de red completa guardado en: outputs\mapa_red_completa_20260927_212504.html

📍 2. Generando 4 mapas de rutas de ejemplo...

   → Calculando ruta: Terminal → Estadio
✅ Mapa guardado en: outputs\mapa_ruta_Terminal_Estadio_20260927_212504.html
     ✓ Ruta: Terminal → Calle 7 → Centro → Alcaldía → Quirinal → Estadio
     ✓ Distancia: 5.90 km | Tiempo: 20 min

   [... más rutas ...]

============================================================
  ✅ MAPAS GENERADOS EXITOSAMENTE
============================================================
```

---

## 🎨 Elementos del Mapa

### Panel Informativo
Cada mapa incluye un panel flotante con:
- 🚍 Título del sistema
- 📍 Origen (en verde)
- 📍 Destino (en rojo)
- 📏 Distancia total
- ⏱️ Tiempo estimado
- 🔢 Número de paradas

### Marcadores de Estaciones
- **Verde con ▶**: Estación de origen
- **Rojo con ⏹**: Estación de destino
- **Naranja con ℹ**: Paradas intermedias (numeradas)

### Líneas de Conexión
- **Azul gruesa (peso 6)**: Ruta óptima seleccionada
- **Gris punteada (peso 2)**: Otras conexiones disponibles

---

## 🌍 Coordenadas GPS Reales

Las estaciones usan coordenadas aproximadas de Neiva:

| Estación | Latitud | Longitud | Zona |
|----------|---------|----------|------|
| Terminal | 2.9273 | -75.2819 | Terminal de Transportes |
| Centro | 2.9342 | -75.2809 | Centro histórico |
| Alcaldía | 2.9356 | -75.2795 | Zona administrativa |
| Estadio | 2.9500 | -75.2850 | Norte de la ciudad |
| Sevilla | 2.9550 | -75.2800 | Sector norte |
| ... | ... | ... | ... |

---

## 💻 Tecnologías Utilizadas

### Python - Folium 0.20.0
Biblioteca de visualización de mapas que genera HTML/JavaScript interactivo

**Ventajas:**
- ✅ Mapas HTML independientes
- ✅ No requiere servidor
- ✅ Funciona offline (después de primera carga)
- ✅ Fácil de compartir

### OpenStreetMap
Plataforma de mapas colaborativa de código abierto

**Ventajas:**
- ✅ Datos reales y actualizados
- ✅ Gratuito y sin límites
- ✅ Cobertura global
- ✅ Alta calidad

### Leaflet.js (bajo el capó)
Motor JavaScript para mapas interactivos

---

## 📊 Comparación: Antes vs Ahora

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| Visualización | Solo texto en consola | Mapas interactivos en HTML |
| Contexto geográfico | Ninguno | Mapa real de Neiva |
| Interactividad | Solo lectura | Zoom, pan, clicks, tooltips |
| Compartir resultados | Copiar texto | Enviar archivo HTML |
| Profesionalismo | Básico | Alta calidad visual |
| Geolocalización | No | Coordenadas GPS reales |

---

## 🎯 Casos de Uso

### 1. Presentaciones Académicas
- Incluir capturas de los mapas en diapositivas
- Demostrar el algoritmo A* visualmente
- Mostrar optimización de rutas en contexto real

### 2. Informes Técnicos
- Adjuntar mapas HTML como evidencia
- Documentar rutas calculadas
- Validar resultados geográficamente

### 3. Análisis de Red
- Identificar zonas de alta conectividad
- Detectar estaciones centrales
- Proponer expansiones del sistema

### 4. Validación de Datos
- Verificar que las distancias sean realistas
- Confirmar que las conexiones tengan sentido geográfico
- Detectar errores en la base de conocimiento

---

## 🔧 Personalización Avanzada

### Cambiar Estilo del Mapa

Edita `src/mapa_interactivo.py`, línea ~50:

```python
# Opciones de tiles:
tiles='OpenStreetMap'        # Estilo estándar
tiles='CartoDB positron'     # Estilo minimalista claro
tiles='CartoDB dark_matter'  # Estilo oscuro
tiles='Stamen Terrain'       # Con relieve topográfico
```

### Cambiar Colores

Edita el diccionario `self.colores` en `src/mapa_interactivo.py`, línea ~34:

```python
self.colores = {
    'ruta': '#2E86AB',           # Azul de la ruta principal
    'origen': '#06A77D',          # Verde del origen
    'destino': '#D00000',         # Rojo del destino
    'parada': '#F77F00',          # Naranja de paradas
    'red': '#95A3A4',             # Gris de la red
}
```

### Ajustar Zoom Inicial

Línea ~52:

```python
zoom_start=13  # Aumenta para más cerca, disminuye para más lejos
```

---

## 📚 Documentación Adicional

Consulta estos archivos para más información:

- **`docs/MAPAS_INTERACTIVOS.md`**: Guía completa de uso de mapas
- **`docs/commands.md`**: Comandos actualizados con mapas
- **`src/mapa_interactivo.py`**: Código documentado del módulo

---

## ✅ Verificación de Instalación

```bash
# Verificar que folium está instalado
python -c "import folium; print(f'✅ Folium {folium.__version__} instalado')"

# Generar un mapa de prueba
python generar_mapas.py

# Verificar archivos generados
dir outputs\*.html
```

---

## 🐛 Solución de Problemas

### Error: ModuleNotFoundError: No module named 'folium'

**Solución:**
```bash
pip install folium
```

### El mapa no se abre automáticamente

**Solución:**
Abre manualmente desde `outputs/`:
```bash
start outputs\mapa_red_completa_*.html
```

### Quiero actualizar coordenadas GPS

**Solución:**
1. Edita `src/base_conocimiento.py`
2. Busca `self.estaciones = {`
3. Actualiza las coordenadas `lat` y `lon` de cada estación
4. Regenera los mapas

---

## 🎓 Ejemplo Completo Paso a Paso

```bash
# 1. Instalar folium (si no está instalado)
pip install folium

# 2. Generar mapas de ejemplo
python generar_mapas.py
# → Se crean 5 archivos HTML en outputs/

# 3. Abrir un mapa manualmente
start outputs\mapa_red_completa_20260927_212504.html
# → Se abre en tu navegador predeterminado

# 4. Usar modo interactivo para buscar tu propia ruta
python main.py
# → Responde las preguntas:
#   - ¿Ver mapa de red completa? s
#   - Origen: Terminal
#   - Destino: Limonar
#   - ¿Ver mapa de la ruta? s
# → El mapa se abre automáticamente

# 5. Compartir el mapa
# → Envía el archivo HTML por correo o súbelo a Google Drive
# → Cualquiera puede abrirlo sin instalar nada
```

---

## 🚀 Siguientes Pasos Sugeridos

1. **Probar diferentes rutas** con `python main.py`
2. **Revisar los mapas generados** en la carpeta `outputs/`
3. **Personalizar colores o estilos** editando `mapa_interactivo.py`
4. **Actualizar coordenadas** si conoces las ubicaciones exactas
5. **Compartir mapas** con compañeros o en presentaciones

---

## 📞 Soporte

Para más información:
- Revisa `docs/MAPAS_INTERACTIVOS.md`
- Consulta la documentación de Folium: https://python-visualization.github.io/folium/
- Explora ejemplos en: https://github.com/python-visualization/folium/tree/main/examples

---

**¡Disfruta de los mapas interactivos del SETP Neiva! 🗺️🚍**

*Última actualización: Septiembre 2026*
