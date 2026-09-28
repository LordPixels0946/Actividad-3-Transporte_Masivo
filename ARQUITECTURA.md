# Arquitectura del Sistema

Este documento explica la arquitectura técnica del sistema de búsqueda de rutas óptimas.

## 📐 Diseño General

El sistema sigue una arquitectura modular de 3 capas:

```
┌─────────────────────────────────────┐
│   INTERFAZ DE USUARIO (Consola)    │
│      interfaz_usuario.py            │
└─────────────┬───────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│   MOTOR DE BÚSQUEDA (Algoritmo A*)  │
│    algoritmo_a_estrella.py          │
└─────────────┬───────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│   BASE DE CONOCIMIENTO (Datos)      │
│     base_conocimiento.py            │
└─────────────────────────────────────┘
```

## 🗂️ Componentes

### 1. Base de Conocimiento (`base_conocimiento.py`)

**Responsabilidad**: Almacenar y gestionar los hechos lógicos de la red de transporte.

**Estructuras de datos**:
- `estaciones`: Diccionario con coordenadas geográficas (lat, lon)
- `conexiones`: Lista de tuplas (origen, destino, distancia, tiempo)

**Métodos principales**:
- `obtener_estaciones()`: Lista todas las estaciones
- `obtener_coordenadas(estacion)`: Devuelve coordenadas de una estación
- `obtener_vecinos(estacion)`: Lista vecinos con costos (bidireccional)
- `validar_estacion(estacion)`: Verifica existencia

**Características**:
- Las conexiones son **bidireccionales** automáticamente
- Coordenadas reales aproximadas de Neiva
- Distancias realistas entre estaciones

### 2. Motor de Búsqueda (`algoritmo_a_estrella.py`)

**Responsabilidad**: Implementar el algoritmo A* para encontrar rutas óptimas.

**Clases**:

#### `NodoAStar`
Representa un nodo en el espacio de búsqueda:
- `estacion`: Nombre de la estación
- `g`: Costo real desde el origen (distancia acumulada)
- `h`: Heurística (estimación al destino)
- `f`: Función de evaluación (f = g + h)
- `padre`: Referencia al nodo padre (para reconstruir ruta)

#### `AlgoritmoAEstrella`
Implementa el motor de búsqueda:

**Métodos principales**:

1. `calcular_heuristica(actual, destino)`:
   - Calcula distancia euclidiana entre coordenadas
   - Factor de conversión: 1° ≈ 111 km
   - Ajusta por latitud para coordenadas geográficas
   - **Es admisible**: nunca sobreestima el costo real

2. `buscar_ruta(origen, destino)`:
   - Implementa A* completo
   - Usa `PriorityQueue` para la frontera
   - Ordena por f(n) = g(n) + h(n)
   - Retorna: (ruta, paradas, costo) o (None, error)

3. `_reconstruir_ruta(nodo_final)`:
   - Sigue punteros `padre` desde destino a origen
   - Invierte la lista para obtener ruta correcta
   - Calcula estadísticas de la ruta

### 3. Interfaz de Usuario (`interfaz_usuario.py`)

**Responsabilidad**: Gestionar la interacción con el usuario.

**Clase `InterfazUsuario`**:

**Métodos principales**:
- `mostrar_banner()`: Encabezado del sistema
- `mostrar_estaciones()`: Lista ordenada de estaciones
- `solicitar_estacion(tipo)`: Entrada con validación flexible
- `mostrar_resultado(ruta, paradas, costo)`: Formato de salida
- `ejecutar()`: Bucle principal interactivo

**Características de usabilidad**:
- Entrada case-insensitive (mayúsculas/minúsculas)
- Validación de estaciones con sugerencias
- Formato claro y legible de resultados
- Opción de realizar múltiples búsquedas

## 🧮 Algoritmo A*: Detalles de Implementación

### Pseudocódigo

```
función buscar_ruta(origen, destino):
    frontera ← cola_prioridad()
    frontera.agregar(origen con g=0, h=heuristica(origen, destino))
    
    visitados ← conjunto_vacío()
    mejor_g ← {origen: 0}
    
    mientras frontera no vacía:
        nodo ← frontera.extraer_mínimo()  // menor f
        
        si nodo.estacion == destino:
            retornar reconstruir_ruta(nodo)
        
        visitados.agregar(nodo.estacion)
        
        para cada vecino de nodo.estacion:
            si vecino no en visitados:
                nuevo_g ← nodo.g + distancia(nodo, vecino)
                
                si nuevo_g < mejor_g[vecino]:
                    mejor_g[vecino] ← nuevo_g
                    h ← heuristica(vecino, destino)
                    frontera.agregar(vecino con g=nuevo_g, h=h)
    
    retornar None  // no hay ruta
```

### Propiedades del Algoritmo

1. **Completitud**: Siempre encuentra una solución si existe
2. **Optimalidad**: Garantiza la ruta más corta (con heurística admisible)
3. **Complejidad temporal**: O(b^d) donde b=ramificación, d=profundidad
4. **Complejidad espacial**: O(b^d) para almacenar frontera y visitados

### Heurística Euclidiana

```python
def calcular_heuristica(estacion_actual, estacion_destino):
    lat1, lon1 = coordenadas(estacion_actual)
    lat2, lon2 = coordenadas(estacion_destino)
    
    # Conversión aproximada de grados a km
    dx = (lon2 - lon1) * 111 * cos(lat1)
    dy = (lat2 - lat1) * 111
    
    return sqrt(dx² + dy²)
```

**¿Por qué es admisible?**
- La distancia euclidiana es siempre ≤ distancia real por carreteras
- Representa la "línea recta" entre dos puntos
- Nunca sobreestima el costo real de llegar al destino

## 🔄 Flujo de Ejecución

```
1. Usuario ejecuta main.py
   ↓
2. InterfazUsuario inicializa BaseConocimiento y AlgoritmoAEstrella
   ↓
3. Sistema muestra estaciones disponibles
   ↓
4. Usuario ingresa origen y destino
   ↓
5. InterfazUsuario valida estaciones
   ↓
6. AlgoritmoAEstrella.buscar_ruta(origen, destino)
   ├─ Inicializa frontera con nodo origen
   ├─ BUCLE: Explora nodos con menor f
   │  ├─ Extrae nodo con menor f de frontera
   │  ├─ ¿Es el destino? → Reconstruir ruta
   │  └─ Expandir vecinos → Agregar a frontera
   └─ Retorna (ruta, paradas, costo)
   ↓
7. InterfazUsuario muestra resultado formateado
   ↓
8. ¿Otra búsqueda? → Volver al paso 3 o Salir
```

## 📊 Representación de la Red

La red se representa como un **grafo no dirigido ponderado**:

- **Nodos**: Estaciones (12 en total)
- **Aristas**: Conexiones bidireccionales (16 conexiones = 32 aristas direccionales)
- **Pesos**: Distancia en kilómetros

Propiedades:
- **Conexo**: Todos los nodos son alcanzables desde cualquier otro
- **No dirigido**: Las conexiones funcionan en ambas direcciones
- **Ponderado**: Cada arista tiene un peso (distancia)
- **Sin ciclos negativos**: Todos los pesos son positivos

## 🎯 Decisiones de Diseño

### ¿Por qué A* en lugar de Dijkstra?

A* es más eficiente que Dijkstra porque:
- Usa información heurística para guiar la búsqueda
- Explora menos nodos al priorizar direcciones prometedoras
- Mantiene la optimalidad de Dijkstra con heurística admisible

### ¿Por qué distancia euclidiana como heurística?

- Simple y eficiente de calcular
- Admisible (requisito para A*)
- Representa bien la geometría del espacio geográfico
- No requiere información adicional

### ¿Por qué cola de prioridad?

- Permite extraer eficientemente el nodo con menor f
- Complejidad O(log n) para inserción y extracción
- Esencial para la eficiencia de A*

## 🧪 Testing

El archivo `test_sistema.py` implementa:
- 8 casos de prueba automatizados
- Verificación de rutas cortas, medias y largas
- Validación de optimización con caminos alternativos
- Prueba de conectividad completa de la red

## 📈 Posibles Extensiones

1. **Múltiples criterios**: Optimizar por tiempo en lugar de distancia
2. **Restricciones**: Evitar ciertas estaciones o conexiones
3. **Rutas alternativas**: Encontrar las k mejores rutas
4. **Tiempo real**: Integrar información de tráfico
5. **Interfaz gráfica**: Visualización del mapa y rutas
6. **Persistencia**: Base de datos para histórico de búsquedas
7. **API REST**: Servicio web para integraciones
8. **Horarios**: Considerar frecuencia de buses y tiempos de espera
