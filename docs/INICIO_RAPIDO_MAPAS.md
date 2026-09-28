# 🚀 Inicio Rápido: Mapas Interactivos SETP Neiva

## ⚡ 3 Pasos para Ver los Mapas

### 1️⃣ Instalar Folium

```bash
pip install folium
```

### 2️⃣ Generar Mapas

```bash
python generar_mapas.py
```

### 3️⃣ Abrir un Mapa

```bash
start outputs\mapa_red_completa_20260927_212504.html
```

**¡Listo! El mapa se abre en tu navegador 🌐**

---

## 🗺️ Lo que Verás

### Panel Informativo
```
╔══════════════════════════════════════════╗
║ 🚍 SETP Neiva - Ruta Óptima             ║
║ Origen: Terminal                         ║
║ Destino: Estadio                         ║
║ Distancia: 5.90 km                       ║
║ Tiempo estimado: 20 minutos              ║
║ Paradas: 5                               ║
╚══════════════════════════════════════════╝
```

### Mapa Interactivo
```
     [Mapa Real de Neiva]
     
  🟢 Terminal (Origen)
   ↓
  🟠 Calle 7 (Parada 1)
   ↓
  🟠 Centro (Parada 2)
   ↓
  🟠 Alcaldía (Parada 3)
   ↓
  🟠 Quirinal (Parada 4)
   ↓
  🔴 Estadio (Destino)
  
  [Línea azul conectando la ruta]
  [Red completa en gris claro]
```

---

## 🎮 Controles del Mapa

```
┌─────────────────────────────────────┐
│ 📏 Medidor    [Panel Info]   ⛶ Full│
│                                     │
│                                     │
│          [MAPA DE NEIVA]            │
│                                     │
│                                     │
│               🗺️ MiniMapa          │
└─────────────────────────────────────┘
   [+] [-] Zoom
```

### Acciones Disponibles

- **Zoom:** Rueda del ratón o botones +/-
- **Mover:** Click y arrastra
- **Info rápida:** Pasa el cursor sobre marcadores
- **Info detallada:** Click en marcadores
- **Pantalla completa:** Botón ⛶ (ESC para salir)
- **Medir distancias:** Botón 📏

---

## 📁 Archivos Generados

```
outputs/
├── 🗺️ mapa_red_completa_20260927_212504.html         (33 KB)
│   └── Muestra todas las estaciones y conexiones
│
├── 🗺️ mapa_ruta_Terminal_Estadio_20260927_212504.html (28 KB)
│   └── Ruta: Terminal → Calle 7 → Centro → Alcaldía → Quirinal → Estadio
│
├── 🗺️ mapa_ruta_San_Mateo_Sevilla_20260927_212504.html (27 KB)
│   └── Ruta: San Mateo → Calixto → Gran Centro → Cándido → Sevilla
│
├── 🗺️ mapa_ruta_Calle_7_Limonar_20260927_212504.html (27 KB)
│   └── Ruta: Calle 7 → Centro → Alcaldía → Quirinal → Limonar
│
└── 🗺️ mapa_ruta_Centro_Calixto_20260927_212504.html (23 KB)
    └── Ruta: Centro → Gran Centro → Calixto
```

**Total: 5 mapas HTML (138 KB)**

---

## 🎯 Dos Formas de Usar

### Opción A: Generar Múltiples Mapas

```bash
python generar_mapas.py
```

**Resultado:**
- 1 mapa de red completa
- 4 mapas de rutas de ejemplo
- Todos guardados en `outputs/`

---

### Opción B: Búsqueda Interactiva

```bash
python main.py
```

**Flujo:**

```
┌────────────────────────────────────────┐
│ ¿Ver mapa de red completa? (s/n): s   │ ← Escribe 's'
└────────────────────────────────────────┘
           ↓
    [Mapa se abre en navegador]
           ↓
┌────────────────────────────────────────┐
│ Origen: Terminal                       │ ← Escribe origen
│ Destino: Estadio                       │ ← Escribe destino
└────────────────────────────────────────┘
           ↓
    [Sistema calcula ruta con A*]
           ↓
┌────────────────────────────────────────┐
│ RUTA ÓPTIMA ENCONTRADA:                │
│ Terminal → Calle 7 → Centro →          │
│ Alcaldía → Quirinal → Estadio          │
│                                        │
│ Distancia: 5.90 km                     │
│ Tiempo: 20 minutos                     │
└────────────────────────────────────────┘
           ↓
┌────────────────────────────────────────┐
│ ¿Ver mapa interactivo? (s/n): s       │ ← Escribe 's'
└────────────────────────────────────────┘
           ↓
    [Mapa de la ruta se abre]
```

---

## 🎨 Colores en el Mapa

| Color | Elemento | Significado |
|-------|----------|-------------|
| 🟢 Verde | Marcador con ▶ | Estación de origen |
| 🔴 Rojo | Marcador con ⏹ | Estación de destino |
| 🟠 Naranja | Marcadores numerados | Paradas intermedias |
| 🔵 Azul grueso | Línea continua | Ruta óptima seleccionada |
| ⚪ Gris | Líneas punteadas | Otras conexiones disponibles |

---

## 📊 Características Principales

### ✅ Mapa Real de Neiva
- Calles y avenidas reales
- Ríos y geografía real
- Barrios y zonas identificables

### ✅ Coordenadas GPS Reales
- Cada estación tiene lat/lon real
- Posiciones aproximadas en Neiva
- Verificables en Google Maps

### ✅ Interactividad Completa
- Navegación fluida
- Información en tiempo real
- Controles profesionales

### ✅ Archivos Independientes
- HTML puro (no requiere servidor)
- Funcionan offline (tras primera carga)
- Compartibles por cualquier medio

---

## 🔧 Comandos Útiles

### Ver todos los mapas generados
```bash
dir outputs\*.html
```

### Abrir el último mapa generado
```bash
start outputs\mapa_*.html | Select-Object -Last 1
```

### Contar cuántos mapas hay
```bash
(Get-ChildItem outputs\*.html).Count
```

### Ver tamaño total de mapas
```bash
(Get-ChildItem outputs\*.html | Measure-Object -Property Length -Sum).Sum / 1KB
```

---

## 💡 Trucos y Consejos

### 🎯 Para Presentaciones

1. Genera el mapa de tu ruta
2. Abre en navegador
3. Ajusta zoom y posición
4. Presiona F11 (pantalla completa)
5. Presenta directamente desde el navegador

### 📧 Para Compartir

1. Copia el archivo HTML
2. Envía por correo o sube a Drive
3. El receptor solo necesita un navegador
4. Funciona en Windows, Mac, Linux, móviles

### 🖼️ Para Documentos

1. Abre el mapa en navegador
2. Ajusta la vista
3. Captura de pantalla (Win + Shift + S)
4. Pega en Word/PowerPoint/PDF

---

## 🚨 Solución Rápida de Problemas

### ❌ Error: "ModuleNotFoundError: No module named 'folium'"

✅ **Solución:**
```bash
pip install folium
```

---

### ❌ El mapa no se abre automáticamente

✅ **Solución:**
```bash
# Abre manualmente
start outputs\mapa_red_completa_20260927_212504.html
```

---

### ❌ Quiero cambiar los colores

✅ **Solución:**
1. Abre `src/mapa_interactivo.py`
2. Busca línea ~34: `self.colores = {`
3. Cambia los códigos hexadecimales:
   ```python
   'ruta': '#2E86AB',    # Azul (cambia a tu color)
   'origen': '#06A77D',  # Verde
   'destino': '#D00000', # Rojo
   ```
4. Guarda y ejecuta `python generar_mapas.py`

---

### ❌ Las coordenadas no son exactas

✅ **Solución:**
1. Abre `src/base_conocimiento.py`
2. Busca `self.estaciones = {`
3. Actualiza lat y lon de cada estación:
   ```python
   'Terminal': {'lat': 2.9273, 'lon': -75.2819},
   ```
4. Busca coordenadas reales en Google Maps:
   - Click derecho → "¿Qué hay aquí?"
   - Copia lat, lon
5. Guarda y regenera mapas

---

## 📚 Documentación Completa

Si necesitas más información:

| Archivo | Contenido |
|---------|-----------|
| `COMO_USAR_MAPAS.md` | Guía de uso completa |
| `docs/MAPAS_INTERACTIVOS.md` | Documentación técnica detallada |
| `NUEVA_FUNCIONALIDAD.md` | Resumen de características |
| `VERIFICACION_MAPAS.md` | Estado de implementación |
| `RESUMEN_IMPLEMENTACION.md` | Detalles técnicos |

---

## ✨ ¡Eso es todo!

Con estos 3 comandos ya puedes visualizar las rutas del SETP Neiva sobre mapas reales:

```bash
# 1. Instalar
pip install folium

# 2. Generar
python generar_mapas.py

# 3. Abrir
start outputs\mapa_red_completa_20260927_212504.html
```

**🗺️ ¡Disfruta explorando Neiva con el sistema de rutas inteligentes! 🚍**

---

*Guía de inicio rápido | Septiembre 2026*
*Para más ayuda, consulta COMO_USAR_MAPAS.md*
