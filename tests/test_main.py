import pytest
from src.employee import SalaryEmployees
import json

@pytest.fixture
def get_csv_file():
    # Данные для CSV-файла
    csv_data = [
        "id,email,name,department,hours_worked,hourly_rate",
        "1,alice@example.com,Alice Johnson,Marketing,160,50",
        "2,bob@example.com,Bob Smith,Design,150,40"
    ]

    csv_path = './dada.csv'
    with open(csv_path, 'w') as f:
        f.write('\n'.join(csv_data))
    return [str(csv_path)]


def test_get_data_from_report(get_csv_file):
    # Проверка чтения данных из файла csv
    salary = SalaryEmployees(get_csv_file)
    data = salary.get_data_from_report()

    # Проверка полученных данных
    assert len(data) == 2
    assert type(data[0]) is dict
    assert data[0]["name"] == "Alice Johnson"
    assert data[1]["name"] == "Bob Smith"
    assert data[1]["department"] == "Design"
    assert data[0]["rate"] == "50"
    assert data[0]["hours_worked"] == "160"


def test_empty_files():
    # проверка на пустые файлы или пустые отчеты без данных
    empty_csv = "./empty.csv"
    with open(empty_csv, "w") as f:
        f.write("")

    salary = SalaryEmployees((empty_csv,))
    data = salary.get_data_from_report()
    print(data)
    assert len(data) == 0


def test_get_salary_report(get_csv_file):
    with open('../report_file.json', 'r') as f:
        assert type(json.load(f)) is dict

    pass
