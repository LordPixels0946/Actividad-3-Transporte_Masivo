# 🚀 EMPIEZA AQUÍ - Sistema SETP Neiva

## 👋 Bienvenido

Este es un **sistema inteligente de búsqueda de rutas** para el SETP (Sistema Estratégico de Transporte Público) de Neiva que:

✅ Calcula **rutas óptimas** con el algoritmo A*  
✅ Muestra las rutas sobre **mapas reales** de Neiva  
✅ Genera **archivos HTML interactivos** que puedes compartir  

---

## ⚡ 3 Pasos para Empezar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Incluye:** folium, networkx, matplotlib, pandas y más

### 2. Ejecutar el sistema

```bash
python main.py
```

### 3. Seguir las instrucciones en pantalla

```
¿Ver mapa red completa? → Escribe: s  (o n para omitir)
Origen: → Escribe: Terminal
Destino: → Escribe: Estadio
¿Ver mapa interactivo? → Escribe: s
```

**El mapa se abre en tu navegador automáticamente** 🌐

---

## 📖 ¿Qué leer según tu nivel?

### 👤 Soy nuevo, quiero empezar rápido

**Lee esto:**
1. 👉 **Este archivo** (ya estás aquí)
2. `LEEME.md` - Guía rápida en español (5 minutos)
3. `docs/INICIO_RAPIDO_MAPAS.md` - Mapas en 3 pasos

**Ejecuta esto:**
```bash
python main.py
```

---

### 👨‍💻 Quiero saber cómo funciona

**Lee esto:**
1. `README.md` - Documentación completa del proyecto
2. `docs/COMO_USAR_MAPAS.md` - Guía práctica de mapas
3. `docs/commands.md` - Todos los comandos disponibles

**Ejecuta esto:**
```bash
python generar_mapas.py  # Genera 5 mapas de ejemplo
```

---

### 🔧 Soy desarrollador, quiero ver el código

**Lee esto:**
1. `docs/ARQUITECTURA.md` - Diseño técnico del sistema
2. `docs/MAPAS_INTERACTIVOS.md` - Implementación de mapas
3. `docs/RESUMEN_IMPLEMENTACION.md` - Detalles técnicos

**Revisa esto:**
- `src/` - Todo el código fuente
- `src/mapa_interactivo.py` - Generador de mapas (nuevo)
- `src/algoritmo_a_estrella.py` - Algoritmo A*

---

## 🗺️ ¿Qué son los mapas interactivos?

Son archivos HTML que muestran:

- **🟢 Marcador verde** → Tu estación de origen
- **🔴 Marcador rojo** → Tu estación de destino
- **🟠 Marcadores naranjas** → Paradas intermedias
- **🔵 Línea azul** → La ruta óptima calculada
- **Mapa real de Neiva** → De OpenStreetMap

**Puedes:**
- Hacer zoom y mover el mapa
- Click en marcadores para ver info
- Medir distancias
- Compartir el archivo HTML

---

## 📂 Estructura Simple del Proyecto

```
.
├── main.py                    👈 EJECUTA ESTE
├── generar_mapas.py           👈 O ESTE para mapas automáticos
├── LEEME.md                   👈 LEE ESTE primero
│
├── src/                       → Código fuente
├── outputs/                   → Mapas y reportes generados
└── docs/                      → Toda la documentación
    ├── INICIO_RAPIDO_MAPAS.md → Mapas en 3 pasos
    ├── COMO_USAR_MAPAS.md     → Guía completa
    └── INDICE.md              → Índice de todo
```

---

## 🎯 Flujo del Sistema

```
1. Usuario ejecuta: python main.py
        ↓
2. Ingresa ORIGEN y DESTINO
        ↓
3. Sistema CALCULA ruta con A*
        ↓
4. Muestra resultado en CONSOLA
        ↓
5. Pregunta: ¿Ver mapa?
        ↓
6. Genera mapa HTML
        ↓
7. Abre en NAVEGADOR
```

**Importante:** El sistema primero calcula, luego muestra, y después genera el mapa.

---

## 🚍 Estaciones Disponibles

El sistema tiene **12 estaciones** del SETP Neiva:

```
1.  Alcaldía       7.  Gran Centro
2.  Calixto        8.  Limonar
3.  Calle 7        9.  Quirinal
4.  Cándido       10.  San Mateo
5.  Centro        11.  Sevilla
6.  Estadio       12.  Terminal
```

Todas con coordenadas GPS reales.

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Buscar una ruta

```bash
python main.py
```

```
Origen: Terminal
Destino: Estadio
¿Ver mapa? s

RESULTADO:
Terminal → Calle 7 → Centro → Alcaldía → Quirinal → Estadio
Distancia: 5.90 km
Tiempo: 20 minutos

[Mapa se abre en navegador]
```

### Ejemplo 2: Generar varios mapas

```bash
python generar_mapas.py
```

```
Generando:
✅ Mapa de red completa
✅ Mapa Terminal → Estadio
✅ Mapa San Mateo → Sevilla
✅ Mapa Calle 7 → Limonar
✅ Mapa Centro → Calixto

Archivos guardados en outputs/
```

---

## 🐛 ¿Problemas?

### Error: "No module named 'folium'"

```bash
pip install folium
```

### El mapa no se abre

```bash
# Ábrelo manualmente desde outputs/
start outputs\mapa_red_completa_*.html
```

### Más ayuda

- Lee `LEEME.md`
- Consulta `docs/COMO_USAR_MAPAS.md`
- Revisa `docs/commands.md`

---

## 📚 Índice de Documentación

| Archivo | Para quién | Contenido |
|---------|------------|-----------|
| **EMPEZAR_AQUI.md** | **Todos** | **Este archivo - Inicio rápido** |
| LEEME.md | Usuarios nuevos | Guía rápida en español |
| README.md | Todos | Documentación completa |
| ORGANIZACION_PROYECTO.md | Todos | Estructura del proyecto |
| RESUMEN_FINAL.md | Todos | Estado final completo |
| docs/INICIO_RAPIDO_MAPAS.md | Usuarios | Mapas en 3 pasos |
| docs/COMO_USAR_MAPAS.md | Usuarios | Guía práctica de mapas |
| docs/MAPAS_INTERACTIVOS.md | Desarrolladores | Documentación técnica |
| docs/ARQUITECTURA.md | Desarrolladores | Diseño del sistema |
| docs/commands.md | Todos | Referencia de comandos |
| docs/INDICE.md | Todos | Índice completo |

---

## ✨ Lo Más Importante

### Para empezar AHORA:

```bash
# 1. Instalar
pip install -r requirements.txt

# 2. Ejecutar
python main.py

# 3. Escribir
Origen: Terminal
Destino: Estadio
¿Ver mapa? s

# 4. ¡Listo! El mapa se abre solo
```

### Para aprender más:

1. Lee `LEEME.md` (5 minutos)
2. Prueba diferentes rutas
3. Explora `docs/` cuando tengas tiempo

---

## 🎉 ¡Eso es todo!

**Ya estás listo para usar el sistema.**

**Comando para empezar:** `python main.py`

**Documentación completa:** Carpeta `docs/`

**Ayuda rápida:** `LEEME.md`

---

**🚍 ¡Calcula tu ruta óptima ahora! 🗺️**

*Si tienes dudas, consulta `docs/INDICE.md` para encontrar la documentación que necesitas*
