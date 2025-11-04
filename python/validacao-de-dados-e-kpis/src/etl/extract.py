import csv
import os
import sys
from typing import List, Dict, Any

# Adiciona o diretório src ao path do Python
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)  # sobe um nível para src/
sys.path.insert(0, src_dir)

from project_config import PATHS

def extract_employees() -> List[Dict[str, Any]]:
    employee_list: list = []
    csv_path = PATHS['DATA_DIR']/'funcionarios.csv'

    with open(csv_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for rows in csv_reader:
            employee_list.append(rows)
    
    return employee_list


