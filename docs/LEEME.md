# 🚍 Sistema SETP Neiva - Guía Rápida

## 🎯 ¿Qué hace este sistema?

Calcula **rutas óptimas** entre estaciones del SETP Neiva usando el **algoritmo A*** y las muestra sobre **mapas reales** de la ciudad.

---

## ⚡ Inicio Rápido (3 comandos)

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Buscar tu ruta

```bash
python main.py
```

### 3. Seguir las instrucciones

```
¿Ver mapa de red completa? (s/n): s    ← Opcional: ver todas las estaciones
Origen: Terminal                        ← Escribe tu origen
Destino: Estadio                        ← Escribe tu destino

🔍 El sistema CALCULA la ruta óptima...

RESULTADO:
  ▶ Terminal → Calle 7 → Centro → Alcaldía → Quirinal → Estadio
  Distancia: 5.90 km | Tiempo: 20 min

¿Ver mapa interactivo? (s/n): s         ← El mapa se abre en tu navegador
```

---

## 🗺️ Cómo Funciona

### Flujo del Sistema

```
1. Usuario ingresa ORIGEN y DESTINO
            ↓
2. Sistema calcula ruta con ALGORITMO A*
            ↓
3. Muestra resultado en CONSOLA
            ↓
4. Pregunta si quiere ver el MAPA
            ↓
5. Genera mapa HTML con la ruta
            ↓
6. Abre en NAVEGADOR automáticamente
```

### El Algoritmo A*

- Encuentra la **ruta más corta** entre dos estaciones
- Usa **heurística euclidiana** (distancia en línea recta)
- Garantiza la **solución óptima**
- Considera todas las conexiones disponibles

---

## 📋 Comandos Disponibles

### Búsqueda Interactiva (Recomendado)

```bash
python main.py
```

**Qué hace:**
1. Te pregunta origen y destino
2. Calcula la ruta óptima
3. Muestra resultado en consola
4. Opcionalmente genera mapa interactivo

---

### Generar Mapas de Ejemplo

```bash
python generar_mapas.py
```

**Qué hace:**
- Genera 5 mapas HTML automáticamente
- 1 mapa de red completa
- 4 mapas de rutas de ejemplo
- Los guarda en `outputs/`

---

### Análisis Completo

```bash
python generar_analisis_completo.py
```

**Qué hace:**
- Genera gráficos PNG de la red
- Crea reportes Excel profesionales
- Análisis de centralidad de estaciones
- Comparativa con otros sistemas BRT

---

### Ejecutar Pruebas

```bash
python src/test_sistema.py
```

**Qué hace:**
- Ejecuta 8 pruebas automatizadas
- Verifica rutas cortas, medias y largas
- Valida conectividad de la red

---

## 🗺️ Mapas Interactivos

### Características

- **Mapa real de Neiva** con OpenStreetMap
- **Coordenadas GPS** de 12 estaciones
- **Marcadores de colores:**
  - 🟢 Verde = Origen
  - 🔴 Rojo = Destino
  - 🟠 Naranja = Paradas intermedias
- **Líneas:**
  - Azul gruesa = Ruta óptima calculada
  - Gris punteada = Otras conexiones disponibles

### Controles del Mapa

- **Zoom:** Rueda del ratón o botones +/-
- **Mover:** Click y arrastra
- **Info:** Click en marcadores
- **Pantalla completa:** Botón en esquina superior derecha
- **Medir distancias:** Herramienta de medición

### Archivos Generados

Los mapas se guardan como HTML en `outputs/`:

```
outputs/
├── mapa_red_completa_FECHA_HORA.html
├── mapa_ruta_Terminal_Estadio_FECHA_HORA.html
└── ... más mapas
```

**Puedes:**
- Abrirlos en cualquier navegador
- Compartirlos por correo
- Incluirlos en presentaciones
- Subirlos a la web

---

## 📊 Estaciones Disponibles

```
1.  Alcaldía        7.  Gran Centro
2.  Calixto         8.  Limonar
3.  Calle 7         9.  Quirinal
4.  Cándido        10.  San Mateo
5.  Centro         11.  Sevilla
6.  Estadio        12.  Terminal
```

Todas con coordenadas GPS reales en Neiva.

---

## 📁 Estructura del Proyecto

```
.
├── main.py                        → Ejecuta interfaz interactiva
├── generar_mapas.py               → Genera mapas automáticamente
├── generar_analisis_completo.py   → Análisis completo
├── requirements.txt               → Dependencias
├── README.md                      → Documentación completa
│
├── src/                           → Código fuente
│   ├── base_conocimiento.py      → Estaciones y conexiones
│   ├── algoritmo_a_estrella.py   → Algoritmo A*
│   ├── interfaz_usuario.py       → Interfaz de consola
│   ├── mapa_interactivo.py       → Generador de mapas
│   └── ...
│
├── outputs/                       → Archivos generados
│   ├── *.html                    → Mapas interactivos
│   ├── *.png                     → Gráficos
│   └── *.xlsx                    → Reportes Excel
│
└── docs/                          → Documentación
    ├── INICIO_RAPIDO_MAPAS.md    → Guía rápida
    ├── COMO_USAR_MAPAS.md        → Guía completa
    ├── MAPAS_INTERACTIVOS.md     → Documentación técnica
    ├── commands.md               → Referencia de comandos
    └── INDICE.md                 → Índice de documentación
```

---

## 🎓 Ejemplo Completo

```bash
# 1. Instalar (solo primera vez)
pip install -r requirements.txt

# 2. Ejecutar sistema
python main.py

# Salida:
============================================================
  SISTEMA INTELIGENTE DE RUTAS - SETP NEIVA
============================================================

¿Desea ver el mapa de la red completa del SETP? (s/n): n

ESTACIONES DISPONIBLES:
  1. Alcaldía      7. Gran Centro
  2. Calixto       8. Limonar
  3. Calle 7       9. Quirinal
  4. Cándido      10. San Mateo
  5. Centro       11. Sevilla
  6. Estadio      12. Terminal

Ingrese estación de ORIGEN: Terminal
Ingrese estación de DESTINO: Estadio

🔍 Buscando ruta óptima...

============================================================
  RESULTADO DE LA BÚSQUEDA
============================================================

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
============================================================

¿Desea ver la ruta en un mapa interactivo? (s/n): s

🗺️  Generando mapa interactivo...
✅ Mapa guardado en: outputs\mapa_ruta_Terminal_Estadio_20260927_210120.html
🌐 Abriendo mapa en el navegador...

¿Desea buscar otra ruta? (s/n): n

¡Gracias por usar el Sistema de Rutas SETP Neiva!
```

---

## 📚 Más Información

### Guías Rápidas
- **`docs/INICIO_RAPIDO_MAPAS.md`** - 3 pasos para usar mapas
- **`docs/COMO_USAR_MAPAS.md`** - Guía práctica completa

### Documentación Técnica
- **`docs/MAPAS_INTERACTIVOS.md`** - Implementación de mapas
- **`docs/ARQUITECTURA.md`** - Diseño del sistema
- **`docs/commands.md`** - Todos los comandos

### Índice
- **`docs/INDICE.md`** - Índice completo de documentación

---

## 🐛 Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'folium'"

```bash
pip install folium
```

### El mapa no se abre automáticamente

```bash
# Abre manualmente desde outputs/
start outputs\mapa_red_completa_*.html
```

### Quiero actualizar coordenadas GPS

1. Edita `src/base_conocimiento.py`
2. Busca `self.estaciones = {`
3. Actualiza `lat` y `lon`

---

## ✨ Características Destacadas

✅ **Algoritmo A*** - Encuentra la ruta más corta garantizada  
✅ **Mapas reales** - Visualización sobre OpenStreetMap  
✅ **Coordenadas GPS** - Ubicaciones reales en Neiva  
✅ **Interactivo** - Zoom, navegación, información detallada  
✅ **Compartible** - Archivos HTML independientes  
✅ **Profesional** - Colores, diseño y presentación de calidad  

---

**¡Listo para calcular tu ruta óptima! 🚍🗺️**

*Para más detalles, consulta `README.md` o la carpeta `docs/`*
