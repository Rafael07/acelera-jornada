import pandas as pd
from typing import Any, Dict, List

BONUS_BASE: int = 1000

def calcular_bonus(df: pd.DataFrame) -> pd.DataFrame:
    df['bonus'] = BONUS_BASE + (df['salario'] * df['bonus_percentual'])
    return df

def quantidade_de_funcionarios_por_area(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['area'])['id'].count().reset_index()
    return df

def calcular_media_salarial_por_area(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(['area'])['salario'].mean().reset_index()
    return df

def calcular_bonus_total(df: pd.DataFrame) -> pd.DataFrame:
    df = df['bonus'].sum().reset_index()
    return df

def mostrar_top3_funcionario_com_bonus(df: pd.DataFrame) -> pd.DataFrame:
    df.sort_values(by='bonus', ascending=False).head(3)
    return df

def run_KPIs(employee_list: List[Dict[str, Any]]):
    df = pd.DataFrame(employee_list)
    calcular_bonus(df)
    quantidade_de_funcionarios_por_area(df)
    calcular_media_salarial_por_area(df)
    calcular_bonus_total(df)
    mostrar_top3_funcionario_com_bonus(df)
