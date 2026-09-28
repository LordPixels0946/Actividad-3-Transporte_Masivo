# Sistema Inteligente de Búsqueda de Rutas - SETP Neiva

Sistema de búsqueda de rutas óptimas para el Sistema Estratégico de Transporte Público (SETP) de Neiva, implementado con el algoritmo A* y búsqueda heurística.

## 📋 Descripción

Este proyecto implementa un motor de búsqueda inteligente que encuentra la ruta óptima entre dos estaciones del sistema de transporte masivo de Neiva. Utiliza:

- **Base de conocimiento**: Representa estaciones y conexiones como hechos lógicos
- **Algoritmo A***: Motor de búsqueda heurística para encontrar rutas óptimas
- **Heurística**: Distancia euclidiana en coordenadas geográficas
- **Interfaz por consola**: Permite al usuario buscar rutas interactivamente

## 🗺️ Estaciones Incluidas

El sistema incluye 12 estaciones reales del SETP Neiva:

1. Terminal
2. Calle 7
3. Centro
4. Alcaldía
5. Quirinal
6. Limonar
7. Gran Centro
8. Calixto
9. Estadio
10. Cándido
11. San Mateo
12. Sevilla

Con 16 conexiones bidireccionales entre ellas.

## 🚀 Requisitos

- Python 3.6 o superior
- No requiere librerías externas (solo módulos estándar de Python)

## 📦 Instalación

1. Clone o descargue este repositorio
2. No se requieren instalaciones adicionales

## ▶️ Ejecución

Para ejecutar el sistema, abra una terminal en el directorio del proyecto y ejecute:

```bash
python main.py
```

O directamente:

```bash
python interfaz_usuario.py
```

## 💻 Uso del Sistema

1. Al iniciar, el sistema muestra todas las estaciones disponibles
2. Ingrese la estación de origen (puede escribir en mayúsculas o minúsculas)
3. Ingrese la estación de destino
4. El sistema calcula y muestra:
   - Ruta óptima completa (secuencia de estaciones)
   - Número de paradas
   - Distancia total en kilómetros
   - Tiempo estimado de viaje

### Ejemplo de Uso

```
ESTACIONES DISPONIBLES:
----------------------------------------
   1. Alcaldía
   2. Calixto
   3. Calle 7
   ...

Ingrese estación de ORIGEN: Terminal
Ingrese estación de DESTINO: Estadio

🔍 Buscando ruta óptima...

============================================================
  RESULTADO DE LA BÚSQUEDA
============================================================

RUTA ÓPTIMA ENCONTRADA:
----------------------------------------
  ▶ Terminal (Origen)
  ▶ Calle 7
  ▶ Centro
  ▶ Alcaldía
  ▶ Quirinal
  ▶ Estadio (Destino)

----------------------------------------
Número de paradas: 5
Distancia total: 5.50 km
Tiempo estimado: 19 minutos
============================================================
```

## 📁 Estructura del Proyecto

```
.
├── base_conocimiento.py      # Base de datos con estaciones y conexiones
├── algoritmo_a_estrella.py   # Implementación del algoritmo A*
├── interfaz_usuario.py        # Interfaz de usuario por consola
├── main.py                    # Punto de entrada principal
├── test_sistema.py            # Script de pruebas automatizadas
├── visualizacion_red.txt      # Mapa visual de la red de transporte
├── README.md                  # Este archivo
├── commands.md                # Comandos Git y pruebas
└── .gitignore                 # Archivos a ignorar en Git
```

## 🔍 Detalles Técnicos

### Base de Conocimiento

La clase `BaseConocimiento` almacena:
- Coordenadas geográficas (latitud, longitud) de cada estación
- Conexiones bidireccionales con distancia y tiempo
- Métodos para consultar vecinos y validar estaciones

### Algoritmo A*

La clase `AlgoritmoAEstrella` implementa:
- **Función de evaluación**: f(n) = g(n) + h(n)
  - g(n): Costo real desde el origen
  - h(n): Estimación heurística al destino
- **Heurística admisible**: Distancia euclidiana (nunca sobreestima)
- **Cola de prioridad**: Explora nodos con menor f(n) primero
- **Reconstrucción de ruta**: Sigue punteros padre hasta el origen

### Complejidad

- **Tiempo**: O(b^d) donde b es el factor de ramificación y d la profundidad
- **Espacio**: O(b^d) para almacenar la frontera y nodos visitados
- **Optimalidad**: Garantizada por heurística admisible

## 🧪 Casos de Prueba

### Pruebas Interactivas

Ejecute el programa principal y pruebe diferentes combinaciones:

```bash
python main.py
```

### Pruebas Automatizadas

Para ejecutar el conjunto completo de pruebas sin interacción manual:

```bash
python test_sistema.py
```

Este script verifica:
- Rutas cortas directas
- Rutas con múltiples paradas
- Optimización de caminos alternativos
- Conectividad completa de la red
- Bidireccionalidad de las rutas

Ver archivo `commands.md` para casos de prueba detallados.

## 👥 Autor

Sistema desarrollado para el curso de Inteligencia Artificial.

## 📄 Licencia

Este proyecto es de uso académico.
