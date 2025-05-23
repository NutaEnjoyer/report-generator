import argparse
from typing import Callable

from reports import get_report
from parsers.csv_parser import parse_csv_files


def main_func() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_files", nargs="+", type=str, help="input files")
    parser.add_argument("--report", required=True, help="report type")
    args = parser.parse_args()

    report_type: str = args.report.lower()
    report_func: Callable | None = get_report(report_type)

    if report_func is None:
        raise ValueError(f"Invalid report type: {report_type}")

    try:
        data: list[dict] = parse_csv_files(args.input_files)
    except Exception as e:
        raise ValueError(f"Error while parsing CSV files: {e}")

    try:
        report: str = report_func(data)
    except Exception as e:
        raise ValueError(f"Error while generating report: {e}")

    return report


def main():
    report: str = main_func()
    print(report)


if __name__ == "__main__":  # pragma: no cover
    main()
