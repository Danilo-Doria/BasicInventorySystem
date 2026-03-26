import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import app

if __name__ == "__main__":
    app.inventory_system_managment()