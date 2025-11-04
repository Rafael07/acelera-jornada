from typing import Any, Dict, List
import extract

area_atuacao: List[str] = ['Vendas', 'TI', 'Financeiro', 'RH', 'Operações']

def name_validation(employee: Dict[str, Any], errors: List[Dict[str, Any]]) -> None:
    # Validação nome vazio
    if not employee['nome']:
        errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'nome',
            'valor': employee['nome'],
            'erro': 'O campo "nome" é obrigatório.'
        })
    # validação nome com números
    for char in employee['nome']:
        if char.isdigit():
            errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'nome',
            'valor': employee['nome'],
            'erro': 'O campo "nome" não deve conter nenhum número.'
        })

def area_validation(employee: Dict[str, Any], errors: List[Dict[str, Any]]) -> None:
    # validação da area do funcionario
    if employee['area'] not in area_atuacao:
        errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'area',
            'valor': employee['area'],
            'erro': 'A área informada não existe na empresa.'
        })
        
def salario_validation(employee: Dict[str, Any], errors: List[Dict[str, Any]]) -> None:
    # validação do salario
    try:
        salario = float(employee['salario'])
        if salario <= 0:
            errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'salario',
            'valor': employee['salario'],
            'erro': 'O campo "salario" deve ser maior que zero.'
        })
    except (ValueError, TypeError):
        errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'salario',
            'valor': employee['salario'],
            'erro': 'O campo "salario" deve ser um número.'
        })
        
def bonus_validation(employee: Dict[str, Any], errors: List[Dict[str, Any]]) -> None:
    # validação do bonus percentual
    try:
        salario = float(employee['salario'])
        if salario <= 0:
            errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'bonus_percentual',
            'valor': employee['bonus_percentual'],
            'erro': 'O campo "bonus_percentual" deve estar entre 0 e 1.'
        })
    except (ValueError, TypeError):
        errors.append({
            'emplolyee_id': employee['id'],
            'campo': 'bonus_percentual',
            'valor': employee['bonus_percentual'],
            'erro': 'O campo "bonus_percentual" deve ser um número.'
        })

def consolidate_validation(employee_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # consolidação de todas as validações
    errors: List[Dict[str, Any]] = []
    for employee in employee_list:
        name_validation(employee, errors)
        area_validation(employee, errors)
        salario_validation(employee, errors)
        bonus_validation(employee, errors)
    return errors
        