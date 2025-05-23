# 📊 Report Generator

Скрипт для генерации отчётов по заработной плате сотрудников из CSV-файлов.

## 🖥 Пример использования

```bash
python3 main.py data1.csv data2.csv data3.csv --report payout
```

## ➕ Как добавить новый отчёт

1 Создайте новый модуль в ```reports/```.<br><br>
2 Создайте класс отчета, наследующийся от ```reports.base_report.BaseReport```. Реализуйте в нем метод ```generate_report```:
```python
class ExampleReport(BaseReport):
    def generate_report(self) -> str:
      # report generation logic
      return json.dumps(report)
```
3 Зарегистрируйте отчет в ```reports/__init__.py```, добавив в словарь ```REPORT_TYPES``` новую запись. <br>
Например:
```python
REPORT_TYPES = {
    ...,
    "example_report": ExampleReport
}
```

Отчет добавлен. Теперь можно запустить скрипт с новым типом отчета:
```bash
python3 main.py data1.csv data2.csv data3.csv --report example_report
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
parsers\csv_parser.py         26      0   100%
reports\__init__.py            4      0   100%
reports\base_report.py        12      0   100%
reports\payout_report.py      30      0   100%
tests\test_csv_parser.py      27      0   100%
tests\test_get_report.py      10      0   100%
tests\test_main.py            60      0   100%
tests\test_payout.py          30      0   100%
utils\get_args.py              9      0   100%
----------------------------------------------
TOTAL                        233      0   100%
```

