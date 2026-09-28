# -*- coding: utf-8 -*-
"""
PUNTO DE ENTRADA PRINCIPAL
Sistema Inteligente de Búsqueda de Rutas - SETP Neiva
"""

import sys
sys.path.insert(0, 'src')

from src.interfaz_usuario import InterfazUsuario


def main():
    """Función principal que inicia el sistema"""
    try:
        interfaz = InterfazUsuario()
        interfaz.ejecutar()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
        print("¡Hasta luego!\n")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")


if __name__ == "__main__":
    main()
