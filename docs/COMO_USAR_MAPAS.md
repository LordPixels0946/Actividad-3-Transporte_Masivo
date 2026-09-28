# 🗺️ Guía Rápida: Cómo Usar los Mapas Interactivos

## ⚡ Inicio Rápido (3 pasos)

### 1️⃣ Instalar Folium (si no está instalado)

```bash
pip install folium
```

### 2️⃣ Generar Mapas

```bash
python generar_mapas.py
```

### 3️⃣ Abrir un Mapa

Los mapas se guardan en `outputs/` con nombres como:
- `mapa_red_completa_20260927_212504.html`
- `mapa_ruta_Terminal_Estadio_20260927_212504.html`

**Abrir con doble clic** o desde la terminal:

```bash
# Windows
start outputs\mapa_red_completa_*.html

# Abre automáticamente en tu navegador predeterminado
```

---

## 🎮 Uso Interactivo

### Desde la Interfaz Principal

```bash
python main.py
```

**Flujo:**

1. **Pregunta inicial:**
   ```
   ¿Desea ver el mapa de la red completa del SETP? (s/n):
   ```
   - Escribe `s` y presiona Enter
   - Se abre el mapa completo en tu navegador

2. **Selecciona origen y destino:**
   ```
   Ingrese estación de ORIGEN: Terminal
   Ingrese estación de DESTINO: Estadio
   ```

3. **Ve el resultado en consola:**
   ```
   RUTA ÓPTIMA ENCONTRADA:
     ▶ Terminal → Calle 7 → Centro → Alcaldía → Quirinal → Estadio
   Distancia total: 5.90 km
   Tiempo estimado: 20 minutos
   ```

4. **Pregunta final:**
   ```
   ¿Desea ver la ruta en un mapa interactivo? (s/n):
   ```
   - Escribe `s` y presiona Enter
   - Se abre el mapa de la ruta en tu navegador

5. **Repetir:**
   ```
   ¿Desea buscar otra ruta? (s/n):
   ```

---

## 🗺️ Qué Verás en el Mapa

### Panel Informativo (Esquina Superior Izquierda)

```
🚍 SETP Neiva - Ruta Óptima
Origen: Terminal
Destino: Estadio
Distancia: 5.90 km
Tiempo estimado: 20 minutos
Paradas: 5
```

### Marcadores de Estaciones

- **🟢 Verde con ▶**: Estación de origen
- **🔴 Rojo con ⏹**: Estación de destino
- **🟠 Naranja con ℹ**: Paradas intermedias

### Líneas de Ruta

- **Azul gruesa**: Ruta óptima que encontró el algoritmo
- **Gris punteada**: Otras conexiones disponibles en la red

---

## 🎯 Controles del Mapa

### Navegación Básica

- **Zoom:** Rueda del ratón o botones `+` / `-`
- **Mover:** Click y arrastra
- **Centrar:** Doble click

### Controles Avanzados

- **📍 Minimapa:** Esquina inferior izquierda
  - Toggle con el botón
  - Vista general de Neiva

- **⛶ Pantalla Completa:** Esquina superior derecha
  - Click para maximizar
  - Presiona `Esc` para salir

- **📏 Medidor de Distancias:** Esquina superior izquierda
  - Click en el icono de regla
  - Click en el mapa para medir distancias personalizadas

- **💬 Información:**
  - **Hover** sobre marcadores: tooltip rápido
  - **Click** sobre marcadores: popup detallado

---

## 📂 Archivos Generados

Después de ejecutar `generar_mapas.py`, encontrarás en `outputs/`:

```
outputs/
├── mapa_red_completa_20260927_212504.html           (Red completa)
├── mapa_ruta_Terminal_Estadio_20260927_212504.html  (Ejemplo 1)
├── mapa_ruta_San_Mateo_Sevilla_20260927_212504.html (Ejemplo 2)
├── mapa_ruta_Calle_7_Limonar_20260927_212504.html   (Ejemplo 3)
└── mapa_ruta_Centro_Calixto_20260927_212504.html    (Ejemplo 4)
```

Cada archivo:
- ✅ Es completamente independiente
- ✅ Se abre en cualquier navegador moderno
- ✅ Funciona sin conexión (después de primera carga)
- ✅ Puede compartirse por correo o nube

---

## 💡 Casos de Uso Rápidos

### Ver Todas las Estaciones

```bash
python generar_mapas.py
# Abre: outputs\mapa_red_completa_*.html
```

### Buscar Ruta Específica

```bash
python main.py
# Responde: n (no ver red completa primero)
# Origen: Tu_Origen
# Destino: Tu_Destino
# Responde: s (ver mapa interactivo)
```

### Comparar Rutas

Ejecuta varias búsquedas con `main.py`, cada una genera un archivo HTML diferente. Abre varios mapas en pestañas del navegador para compararlos.

---

## 🎨 Personalizar Mapas

### Cambiar Zoom Inicial

Edita `src/mapa_interactivo.py`, línea ~52:

```python
zoom_start=13  # Valores: 10 (más lejos) a 16 (más cerca)
```

### Cambiar Estilo de Mapa

Edita `src/mapa_interactivo.py`, línea ~48:

```python
tiles='OpenStreetMap'        # Estilo predeterminado
# O cambia a:
tiles='CartoDB positron'     # Estilo minimalista
tiles='CartoDB dark_matter'  # Estilo oscuro
tiles='Stamen Terrain'       # Con relieve
```

### Cambiar Colores

Edita `src/mapa_interactivo.py`, línea ~34:

```python
self.colores = {
    'ruta': '#2E86AB',      # Color de la ruta principal
    'origen': '#06A77D',    # Color del origen
    'destino': '#D00000',   # Color del destino
}
```

---

## 🐛 Problemas Comunes

### "ModuleNotFoundError: No module named 'folium'"

**Solución:**
```bash
pip install folium
```

### El mapa no se abre automáticamente

**Solución:**
```bash
# Abre manualmente desde la carpeta outputs/
start outputs\mapa_red_completa_20260927_212504.html
```

### Quiero actualizar las coordenadas GPS

**Solución:**
1. Edita `src/base_conocimiento.py`
2. Busca la sección `self.estaciones = {`
3. Actualiza `lat` y `lon` de cada estación
4. Ejecuta `python generar_mapas.py` nuevamente

Ejemplo:
```python
'Terminal': {'lat': 2.9273, 'lon': -75.2819},
```

---

## ✅ Verificación Rápida

```bash
# 1. Verificar instalación
python -c "import folium; print('✅ Folium instalado')"

# 2. Generar mapas
python generar_mapas.py

# 3. Contar mapas generados
dir outputs\*.html

# 4. Abrir el primero
start outputs\mapa_red_completa_*.html
```

---

## 📱 Compartir Mapas

Los archivos HTML pueden:

1. **Enviarse por correo electrónico**
   - Adjunta el archivo `.html`
   - El receptor solo necesita un navegador

2. **Subirse a Google Drive / OneDrive**
   - Comparte el enlace
   - Se puede ver online (preview) o descargar

3. **Embeberse en sitios web**
   ```html
   <iframe src="mapa.html" width="100%" height="600px"></iframe>
   ```

4. **Incluirse en presentaciones**
   - Abre el mapa en el navegador
   - Captura de pantalla
   - O inserta como hipervínculo en PowerPoint

---

## 🎓 Ejemplo Completo Comentado

```bash
# Paso 1: Verificar que folium está instalado
pip install folium
# Salida: "Successfully installed folium-0.20.0"

# Paso 2: Generar mapas de ejemplo
python generar_mapas.py
# Salida:
# ✅ Mapa de red completa guardado
# ✅ Mapa Terminal → Estadio guardado
# ✅ Mapa San Mateo → Sevilla guardado
# ... (más mapas)

# Paso 3: Abrir mapa de red completa
start outputs\mapa_red_completa_20260927_212504.html
# → Se abre en Chrome/Firefox/Edge
# → Ves todas las estaciones en el mapa de Neiva
# → Puedes hacer zoom, mover, explorar

# Paso 4: Buscar tu propia ruta
python main.py
# ¿Ver mapa de red completa? n
# Origen: Calle 7
# Destino: Limonar
# → Muestra ruta en consola
# ¿Ver mapa interactivo? s
# → Se abre el mapa con la ruta resaltada
```

---

## 📚 Más Información

- **Guía completa:** `docs/MAPAS_INTERACTIVOS.md`
- **Resumen de cambios:** `NUEVA_FUNCIONALIDAD.md`
- **Comandos:** `docs/commands.md`
- **Código:** `src/mapa_interactivo.py`

---

**¡Listo! Ya sabes usar los mapas interactivos del SETP Neiva 🗺️🚍**

*Si tienes dudas, revisa la documentación completa en `docs/MAPAS_INTERACTIVOS.md`*
