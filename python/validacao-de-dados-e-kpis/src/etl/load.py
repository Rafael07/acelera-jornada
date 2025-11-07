import csv
import json
import project_config 
from typing import Any, Dict, List

def gerar_relatorio_individual(transformed_dict: Dict) -> None:
    employees_with_bonus = transformed_dict.get('df_com_bonus', [])
    if not employees_with_bonus:
        return
    
    path = project_config.REPORTS['INDIVIDUAL']
    
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=list(employees_with_bonus[0].keys()))
        writer.writeheader()
        writer.writerows(employees_with_bonus)
    
    print(f"Relatório individual gerado em: {project_config.REPORTS['INDIVIDUAL']}")

def gerar_relatorio_erros(errors: List[Dict[str, Any]]) -> None:
    path = project_config.REPORTS['ERROS']
    
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=list(errors[0].keys()))
        writer.writeheader()
        writer.writerows(errors)

    print(f"Log de erros gerado em: {project_config.REPORTS['ERROS']}")

def gerar_kpis(trasformed_dict: Dict) -> None:
    path = project_config.REPORTS['KPIS']
    
    kpis = {
        "funcionarios_por_area": trasformed_dict.get('funcionarios_por_area', []),
        "media_salarial_por_area": trasformed_dict.get('media_salarial_por_area', []),
        "bonus_total": trasformed_dict.get('bonus_total', []),
        "top3_bonus": trasformed_dict.get('top3_bonus', [])
    }

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(kpis, file, ensure_ascii=False, indent=4)

    print(f"Relatório de KPIs gerado em: {project_config.REPORTS['KPIS']}")

def run_reports(transformed_dict: Dict, errors: List[Dict[str, Any]]) -> None:
    gerar_relatorio_individual(transformed_dict)
    gerar_relatorio_erros(errors)
    gerar_kpis(transformed_dict)