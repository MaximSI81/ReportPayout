## 📝 Пример выходных данных
![Screenshot_1](https://github.com/user-attachments/assets/a7799a55-5351-4321-bf57-a1d54f74f515)
# Проект подсчёта зарплаты сотрудников

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

   ```bash
   python --version

## 🚀 Использование

Базовый запуск
   ```bash
   python src/employee.py ./reports/data1.csv ./reports/data2.csv ./reports/data3.csv --report payout
   ```
## Формат входных данных (CSV)
Пример файла data.csv:

```
   id,email,name,department,hours_worked,hourly_rate
   1,alice@example.com,Элис Джонсон,Маркетинг,160,50
   2,bob@example.com,Боб Смит,Дизайн,150,40
```
## Доступные отчёты
 - payout -	Отчёт по зарплатам

## 🧪 Тестирование

Проект включает unit-тесты:
   ```bash
   pytest ./tests/test_main.py -v
   ```

## Тесты проверяют:
 - Чтение данных из CSV
 - проверка на пустые файлы или пустые отчеты без данных
 - проверка записи в формате json
 - проверка записи в txt файл

## 📂 Структура проекта
```
   ReportPayout/
   ├── src/
   │   └── employee.py            # Основной скрипт
   ├── tests/
   │   ├── empty.csv              # тестовые файлы
   │   ├── data.csv
   │   ├── test_report.txt             
   │   └── test_main.py           # Скрипт тесты
   ├── data/
   │   ├── data1.csv              # Пример данных
   │   ├── data2.csv
   │   └── data3.csv
   ├── report_result/
   │   ├── report_file.json       # Результат в JSON
   │   └── report_res.txt         # Текстовый отчет
   └── README.md                  # Этот файл





   


