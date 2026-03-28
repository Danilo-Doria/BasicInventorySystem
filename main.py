# Proporciona acceso a variables y funciones del sistema (como las rutas de carpetas)
import sys
# Permite interactuar con el sistema operativo (rutas de archivos, carpetas, etc.)
import os

# Esta línea añade la carpeta 'src' a la lista de lugares donde Python busca archivos.
# 1. os.path.dirname(__file__) obtiene la ubicación de este archivo actual
# 2. os.path.join() crea una ruta que apunta a la subcarpeta 'src'
# 3. sys.path.append() le dice a Python: "Si no encuentras un módulo, búscalo también en 'src'"
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import app

# Esta condición verifica si el script se está ejecutando directamente (no importado por otro).
if __name__ == "__main__":
    app.inventory_system_managment()