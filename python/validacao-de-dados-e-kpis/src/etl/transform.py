import pandas as pd
from typing import Any, Dict, List

BONUS_BASE: int = 1000

def calcular_bonus(df: pd.DataFrame) -> pd.DataFrame:
    df['bonus'] = BONUS_BASE + (df['salario'].astype(float) * df['bonus_percentual'].astype(float))
    return df

def quantidade_de_funcionarios_por_area(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['area'])['id'].count().reset_index(name='quantidade_funcionarios')
    return df

def calcular_media_salarial_por_area(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['area'])['salario'].mean().reset_index(name='media_salarial')
    return df

def calcular_bonus_total(df: pd.DataFrame) -> float:
    df = df['bonus'].sum()
    return df

def mostrar_top3_funcionario_com_bonus(df: pd.DataFrame) -> pd.DataFrame:
    df.sort_values(by='bonus', ascending=False).head(3)
    return df

def run_KPIs(employee_list: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    df = pd.DataFrame(employee_list)

    df_com_bonus = calcular_bonus(df)
    funcionarios_por_area = quantidade_de_funcionarios_por_area(df_com_bonus)
    media_salarial_por_area = calcular_media_salarial_por_area(df_com_bonus)
    bonus_total = calcular_bonus_total(df_com_bonus)
    top3_bonus = mostrar_top3_funcionario_com_bonus(df_com_bonus)

    transformed_dict: Dict[str, List[Dict[str, Any]]] = {
        "df_com_bonus": df_com_bonus.to_dict(orient='records'),
        "funcionarios_por_area": funcionarios_por_area.to_dict(orient='records'),
        "media_salarial_por_area": media_salarial_por_area.to_dict(orient='records'),
        "bonus_total": [{'bonus_total': bonus_total}],
        "top3_bonus": top3_bonus.to_dict(orient='records')
    }
    return transformed_dict
