"""
Configurações do projeto
"""

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

# Dicin=ario de relatórios do projeto
REPORTS = {
    'INDIVIDUAL': PATHS['REPORTS_DIR']/'relatorio_individual.csv',
    'ERROS': PATHS['REPORTS_DIR']/'erros.csv',
    'KPIS': PATHS['REPORTS_DIR']/'kpis.json'
}