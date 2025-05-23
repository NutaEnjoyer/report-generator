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

    monkeypatch.setattr(main, "parse_csv_files", lambda _: [{"name": "Max"}])
    monkeypatch.setattr(main, "get_report", lambda _: lambda _: "MOCK REPORT")

    result = main_func()

    assert result == "MOCK REPORT"


def test_main_func_error_parsing_csv_files(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "input_file.csv", "--report", "payout"])

    import main

    def raise_parse_error(_):
        raise Exception("Parsing failed")

    monkeypatch.setattr(main, "parse_csv_files", raise_parse_error)

    with pytest.raises(
        ValueError, match="Error while parsing CSV files: Parsing failed"
    ):
        main_func()


def test_main_func_error_generating_report(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "input_file.csv", "--report", "payout"])

    import main

    def raise_error_get_report(_):
        def raise_generate_report_error(_):
            raise Exception("Error generating report")

        return raise_generate_report_error

    monkeypatch.setattr(main, "parse_csv_files", lambda _: [{"name": "Max"}])
    monkeypatch.setattr(main, "get_report", raise_error_get_report)

    with pytest.raises(
        ValueError, match="Error while generating report: Error generating report"
    ):
        main_func()


def test_main_print(monkeypatch, capsys):
    import main

    monkeypatch.setattr(main, "main_func", lambda: "MOCK REPORT")

    result = main.main()

    assert result == None
    assert "MOCK REPORT" in capsys.readouterr().out
