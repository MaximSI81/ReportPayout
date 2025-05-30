Проект подсчёта зарплаты сотрудников

## 📌 Возможности

- Чтение данных сотрудников из CSV-файлов
- Формирование отчёта по зарплатам (`payout`)
- Возможность добавления новых типов отчётов

## ⚙️ Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MaximSI81/ReportPayout.git
   cd ReportPayout   

2. Убедитесь, что у вас установлен Python 3.8+:

bash
python --version

🚀 Использование
Базовый запуск
bash
python payout.py data1.csv data2.csv data3.csv --report payout


Формат входных данных (CSV)
Пример файла data.csv:

id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40


Доступные отчёты
Параметр	Описание
payout	Отчёт по зарплатам

🧪 Тестирование
Проект включает unit-тесты:

bash
pytest test_payout.py -v
Тесты проверяют:
Чтение данных из CSV
проверка на пустые файлы или пустые отчеты без данных
проверка записи в формате json
проверка записи в txt файл

📂 Структура проекта
ReportPayout/
├── src/
    ├── employee.py             # Основной скрипт
├── tests/
    ├── test_payout.py          # Тесты
├── reports/                    
    ├── data.csv1.csv           # Примеры CSV-файлов
    ├── data.csv2.csv
    ├── data.csv3.csv
├── reports_result/
    ├── report_file.json        # json с данными
    ├── report_res.txt          # txt с отчетом
└── README.md             # Этот файл
