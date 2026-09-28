# 🚀 Inicio Rápido

Guía express para ejecutar el sistema en 3 pasos.

## ⚡ Ejecutar el Sistema

### Opción 1: Interfaz Interactiva

```bash
python main.py
```

Sigue las instrucciones en pantalla:
1. Ingresa estación de origen
2. Ingresa estación de destino
3. Visualiza la ruta óptima

### Opción 2: Pruebas Automatizadas

```bash
python test_sistema.py
```

Ejecuta 8 casos de prueba predefinidos y muestra estadísticas.

## 📝 Ejemplo de Uso

```
============================================================
  SISTEMA INTELIGENTE DE RUTAS - SETP NEIVA
  Algoritmo A* con Búsqueda Heurística
============================================================

ESTACIONES DISPONIBLES:
----------------------------------------
   1. Alcaldía        7. Gran Centro
   2. Calixto         8. Limonar
   3. Calle 7         9. Quirinal
   4. Centro         10. San Mateo
   5. Cándido        11. Sevilla
   6. Estadio        12. Terminal

Ingrese estación de ORIGEN: terminal
Ingrese estación de DESTINO: estadio

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
Distancia total: 5.90 km
Tiempo estimado: 20 minutos
============================================================
```

## 🎯 Casos de Prueba Sugeridos

### Ruta Corta
- **Origen**: Terminal
- **Destino**: Calle 7
- **Resultado esperado**: 1 parada, ~1.2 km

### Ruta Media
- **Origen**: Centro
- **Destino**: Calixto
- **Resultado esperado**: 2 paradas, ~2.1 km

### Ruta Larga
- **Origen**: San Mateo
- **Destino**: Sevilla
- **Resultado esperado**: 4 paradas, ~5.6 km

## 📚 Documentación Completa

- `README.md` - Documentación general y guía de uso
- `ARQUITECTURA.md` - Explicación técnica del diseño
- `commands.md` - Comandos Git y casos de prueba detallados
- `visualizacion_red.txt` - Mapa de la red de transporte

## 🔧 Requisitos

- Python 3.6 o superior
- Sin librerías externas necesarias

## ❓ Ayuda

Si tienes problemas:
1. Verifica que Python esté instalado: `python --version`
2. Asegúrate de estar en el directorio correcto
3. Revisa la documentación en `README.md`
