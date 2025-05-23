# 📊 Report Generator

Скрипт для генерации отчётов по заработной плате сотрудников из CSV-файлов.

## 🖥 Пример использования

```bash
python3 main.py data1.csv data2.csv data3.csv --report payout
```

## 🧪 Тестирование

```bash
pip install -r requirements.txt
pytest --cov=.
```

Отчёт покрытия:

```text
Name                       Stmts   Miss  Cover
----------------------------------------------
main.py                       25      0   100%
parsers\__init__.py            0      0   100%
parsers\csv_parser.py         25      0   100%
reports\__init__.py            4      0   100%
reports\payout_report.py      20      0   100%
tests\test_csv_parser.py      25      0   100%
tests\test_main.py            41      0   100%
tests\test_payout.py          18      0   100%
----------------------------------------------
TOTAL                        158      0   100%
```

## ➕ Как добавить новый отчёт

1 Создайте новый модуль в ```reports/```.<br><br>
2 Реализуйте функцию отчета:
```python
def generate(data: list[str]) -> str:
  # report generator's logic 
  return report
```
3 Зарегистрируйте отчет в ```reports/__init__.py```, добавив в словарь ```REPORT_TYPES``` новую запись. <br>
Например:
```python
REPORT_TYPES = {
    ...,
    "average_payout": generate_average_payout_report
}
```

Отчет добавлен. Теперь можно запустить скрипт с новым отчетом:
```bash
python3 main.py data1.csv data2.csv data3.csv --report average_payout
```
