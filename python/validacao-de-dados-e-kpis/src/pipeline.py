"""
Pipeline principal do projeto
"""

from src import project_config
from src.etl.extract import extract_employees
from src.etl.validation import consolidate_validation
from src.etl.transform import run_KPIs
from src.etl.load import run_reports

def main() -> None:
    # 1. Extract
    employees = extract_employees()

    # 2. Validate
    errors = consolidate_validation(employees)

    # 3. Transform
    results = run_KPIs(employees, errors)

    # 4. Load
    run_reports(results, errors)

    print(f"Relatórios gerados com sucesso!")

if __name__ == "__main__":
    main()