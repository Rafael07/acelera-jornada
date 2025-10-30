"""
Configurações do projeto
"""


import os 
from pathlib import Path

# Path raiz do projeto
PROJECT_ROOT = Path(__file__).parent.parent

# Dicionário com paths do projeto
PATHS = {
    'ROOT_DIR': PROJECT_ROOT,
    'DATA_DIR': PROJECT_ROOT/'data',
    'SRC_DIR': PROJECT_ROOT/'src',
    'REPORTS_DIR': PROJECT_ROOT/'reports'
}
