# 📋 Comandos Python - Sistema SETP Neiva

## 🚀 Comandos Principales

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```
**Descripción:** Instala todas las bibliotecas necesarias para ejecutar el proyecto (networkx, matplotlib, pandas, openpyxl, numpy, seaborn, folium).

---

### 2. Modo Interactivo con Mapas

```bash
python main.py
```
**Descripción:** Inicia la interfaz interactiva por consola que permite buscar rutas óptimas entre estaciones. Ahora incluye la opción de visualizar las rutas en mapas interactivos de Neiva con geolocalización real.

---

### 3. Generar Mapas Interactivos

```bash
python generar_mapas.py
```
**Descripción:** Genera automáticamente mapas HTML interactivos de la red completa del SETP y rutas de ejemplo sobre el mapa real de Neiva usando OpenStreetMap.

---

### 4. Análisis Completo

```bash
python generar_analisis_completo.py
```
**Descripción:** Genera automáticamente todos los análisis, gráficos PNG, reportes Excel y archivos de métricas del sistema SETP en la carpeta `outputs/`.

---

### 5. Pruebas Automatizadas

```bash
python src/test_sistema.py
```
**Descripción:** Ejecuta la suite completa de 8 pruebas predefinidas que verifican rutas cortas, medias, largas, optimización y conectividad de la red.

---

## 🔍 Comandos de Verificación

### 6. Verificar Versión de Python

```bash
python --version
```
**Descripción:** Muestra la versión de Python instalada (debe ser 3.6 o superior).

---

### 7. Verificar Módulos Instalados

```bash
python -c "import networkx, matplotlib, pandas, folium; print('✅ Módulos instalados correctamente')"
```
**Descripción:** Verifica que las bibliotecas principales estén correctamente instaladas, incluyendo folium para mapas interactivos.

---

### 8. Verificar Sintaxis

```bash
python -m py_compile src\*.py main.py generar_analisis_completo.py generar_mapas.py
```
**Descripción:** Compila todos los archivos Python para verificar que no haya errores de sintaxis sin ejecutar el código.

---

### 9. Verificar Backend de Matplotlib

```bash
python -c "import matplotlib; print(matplotlib.get_backend())"
```
**Descripción:** Muestra el backend actual de matplotlib usado para generar gráficos.

---

## 📊 Comandos de Análisis

### 10. Verificar Estilo de Código (requiere pylint)

```bash
pylint *.py
```
**Descripción:** Analiza el código Python para detectar errores de estilo y posibles problemas de calidad.

---

## 🗺️ Características de los Mapas Interactivos

Los mapas generados incluyen:
- ✅ Visualización sobre mapas reales de Neiva con OpenStreetMap
- ✅ Coordenadas GPS reales de las estaciones
- ✅ Rutas marcadas con colores profesionales
- ✅ Marcadores diferenciados para origen (verde), destino (rojo) y paradas (naranja)
- ✅ Información emergente con distancias y tiempos
- ✅ Minimapa para navegación
- ✅ Modo pantalla completa
- ✅ Herramienta de medición de distancias
- ✅ Archivos HTML interactivos que se abren en cualquier navegador

---

*Última actualización: Septiembre 2026*
