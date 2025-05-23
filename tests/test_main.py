import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import main_func


def test_main_func_invalid_report_type(monkeypatch):
    monkeypatch.setattr(
        "sys.argv", ["main.py", "input_file.csv", "--report", "invalid_report_type"]
    )

    with pytest.raises(ValueError, match="Invalid report type: invalid_report_type"):
        main_func()


def test_main_func_success(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "input_file.csv", "--report", "payout"])

    import main

    class CSVParserSuccess:
        def parse_csv_files(self, _):
            return [{"name": "Max"}]

    class PayoutReportSuccess:
        def __init__(self, _):
            pass

        def __str__(self):
            return "MOCK REPORT"

    monkeypatch.setattr(main, "CSVParser", CSVParserSuccess)
    monkeypatch.setattr(main, "get_report", lambda _: PayoutReportSuccess)

    result = main_func()

    assert str(result) == "MOCK REPORT"


def test_main_func_error_parsing_csv_files(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "input_file.csv", "--report", "payout"])

    import main

    class CSVParserError:
        def parse_csv_files(self, _):
            raise Exception("Parsing failed")

    monkeypatch.setattr(main, "CSVParser", CSVParserError)

    with pytest.raises(
        ValueError, match="Error while parsing CSV files: Parsing failed"
    ):
        main_func()


def test_main_func_error_generating_report(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "input_file.csv", "--report", "payout"])

    import main

    class CSVParserError:
        def parse_csv_files(self, _):
            return [{"name": "Max"}]

    class PayoutReportError:
        def __init__(self, _):
            raise Exception("Error generating report")

    monkeypatch.setattr(main, "CSVParser", CSVParserError)
    monkeypatch.setattr(main, "get_report", lambda _: PayoutReportError)

    with pytest.raises(
        ValueError, match="Error while generating report: Error generating report"
    ):
        main_func()


def test_main_print(monkeypatch, capsys):
    import main

    class PayoutReportSuccess:
        def __init__(self):
            pass

        def __str__(self):
            return "MOCK REPORT"

        def __getattr__(self, name):
            if name == "json":
                return "MOCK JSON"

    monkeypatch.setattr(main, "main_func", lambda: PayoutReportSuccess())

    result = main.main()

    assert result == "MOCK JSON"
    assert "MOCK REPORT" in capsys.readouterr().out
