# Comandos Git y Guía de Pruebas

Este documento contiene los comandos Git necesarios para gestionar el proyecto y los casos de prueba recomendados.

## 🔧 Comandos Git

### Inicializar Repositorio

```bash
# Inicializar repositorio Git
git init

# Agregar todos los archivos
git add .

# Crear el primer commit
git commit -m "Implementación inicial del sistema de rutas SETP Neiva con A*"
```

### Crear .gitignore

Crear archivo `.gitignore` con el siguiente contenido:

```
# Archivos de Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Entornos virtuales
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Sistema operativo
.DS_Store
Thumbs.db
```

Luego agregarlo:

```bash
git add .gitignore
git commit -m "Agregar .gitignore para Python"
```

### Comandos Básicos de Git

```bash
# Ver estado del repositorio
git status

# Ver historial de commits
git log --oneline

# Ver diferencias
git diff

# Crear una rama nueva
git branch nombre-rama
git checkout nombre-rama
# O en un solo comando:
git checkout -b nombre-rama

# Volver a la rama principal
git checkout main

# Fusionar una rama
git merge nombre-rama

# Subir cambios a GitHub (después de crear el repositorio remoto)
git remote add origin https://github.com/tu-usuario/setp-neiva.git
git branch -M main
git push -u origin main
```

### Trabajo con Cambios

```bash
# Agregar archivos específicos
git add base_conocimiento.py
git add algoritmo_a_estrella.py

# Agregar todos los cambios
git add .

# Commit con mensaje descriptivo
git commit -m "Descripción del cambio"

# Ver diferencias antes de hacer commit
git diff

# Deshacer cambios no guardados
git checkout -- archivo.py

# Ver cambios en un archivo específico
git log -p archivo.py
```

## 🧪 Casos de Prueba Recomendados

### Prueba 1: Ruta Corta

**Objetivo**: Verificar rutas directas

```
Origen: Terminal
Destino: Calle 7

Resultado esperado:
- Ruta: Terminal → Calle 7
- Paradas: 1
- Distancia: ~1.2 km
```

### Prueba 2: Ruta Media

**Objetivo**: Verificar búsqueda con múltiples paradas

```
Origen: Terminal
Destino: Alcaldía

Resultado esperado:
- Ruta: Terminal → Calle 7 → Centro → Alcaldía
- Paradas: 3
- Distancia: ~3.0 km
```

### Prueba 3: Ruta Larga

**Objetivo**: Verificar optimización en rutas complejas

```
Origen: Terminal
Destino: Estadio

Resultado esperado:
- Ruta óptima con 5-6 paradas
- El sistema debe elegir el camino más corto
```

### Prueba 4: Ruta con Alternativas

**Objetivo**: Verificar que A* elige la mejor ruta

```
Origen: Centro
Destino: Calixto

Rutas posibles:
- Centro → Gran Centro → Calixto
- Centro → Calle 7 → Calixto

El sistema debe elegir la más corta.
```

### Prueba 5: Estaciones Extremas

**Objetivo**: Verificar conectividad completa de la red

```
Origen: San Mateo
Destino: Sevilla

Debe encontrar una ruta válida atravesando varias estaciones.
```

### Prueba 6: Misma Estación

**Objetivo**: Verificar caso límite

```
Origen: Centro
Destino: Centro

Resultado esperado: Mensaje indicando que origen y destino son iguales.
```

### Prueba 7: Estación Inválida

**Objetivo**: Verificar validación de entrada

```
Origen: EstacionInexistente
Destino: Centro

Resultado esperado: Mensaje de error y solicitud de estación válida.
```

### Prueba 8: Mayúsculas/Minúsculas

**Objetivo**: Verificar flexibilidad en entrada

```
Origen: terminal (minúsculas)
Destino: ESTADIO (mayúsculas)

Resultado esperado: Debe funcionar correctamente ignorando mayúsculas.
```

### Prueba 9: Ruta Completa de la Red

**Objetivo**: Verificar todas las conexiones

```
Probar diferentes combinaciones para asegurar que:
- Todas las estaciones son alcanzables
- No hay estaciones aisladas
- Las distancias son coherentes
```

### Prueba 10: Rendimiento

**Objetivo**: Verificar tiempo de respuesta

```
Realizar múltiples búsquedas consecutivas.

Resultado esperado:
- Cada búsqueda debe completarse en menos de 1 segundo
- La interfaz debe ser fluida
```

## 📊 Verificación de Resultados

Para cada prueba, verificar:

1. ✅ **Ruta encontrada**: El sistema encuentra una ruta válida
2. ✅ **Optimalidad**: La ruta es la más corta (menor distancia)
3. ✅ **Cálculos correctos**: Número de paradas y distancia son coherentes
4. ✅ **Interfaz clara**: Los resultados se muestran de forma comprensible
5. ✅ **Manejo de errores**: Los casos límite se manejan apropiadamente

## 🔍 Comandos para Ejecutar Pruebas

```bash
# Ejecutar el programa
python main.py

# Ejecutar con salida detallada (si se implementa logging)
python main.py --verbose

# Verificar sintaxis sin ejecutar
python -m py_compile *.py

# Verificar estilo de código (requiere pylint)
pylint *.py
```

## 📝 Registro de Pruebas

Crear un archivo `pruebas.txt` para documentar los resultados:

```
Fecha: [fecha]
Prueba 1 - Ruta Corta: ✅ PASÓ
  Origen: Terminal, Destino: Calle 7
  Resultado: 1 parada, 1.2 km

Prueba 2 - Ruta Media: ✅ PASÓ
  Origen: Terminal, Destino: Alcaldía
  Resultado: 3 paradas, 3.0 km
  
...
```

## 🚀 Flujo de Trabajo Recomendado

1. Hacer cambios en el código
2. Ejecutar pruebas manuales
3. Verificar que todo funciona correctamente
4. Agregar archivos modificados: `git add .`
5. Crear commit descriptivo: `git commit -m "Descripción"`
6. Subir cambios: `git push`

## 📚 Recursos Adicionales

- [Git - Documentación oficial](https://git-scm.com/doc)
- [Python - Documentación oficial](https://docs.python.org/es/)
- [Algoritmo A* - Wikipedia](https://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda_A*)
