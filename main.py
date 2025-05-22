import argparse
import sys
from typing import Callable

from reports import get_report
from parsers.csv_parser import parse_csv_files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_files', nargs="+", type=str, help='input files')
    parser.add_argument('--report', required=True, help='output file')
    args = parser.parse_args()

    report_type: str = args.report.lower()
    report_func: Callable | None = get_report(report_type)

    if report_func is None:
        print(f'Invalid report type: {report_type}', file=sys.stderr)
        return

    try:
        data: list[dict] = parse_csv_files(args.input_files)
    except Exception as e:
        print(f'Error while parsing files: {e}', file=sys.stderr)
        return


    try:
        report = report_func(data)
    except Exception as e:
        print(f'Error while generating report: {e}', file=sys.stderr)
        return

    print(report)


if __name__ == '__main__':
    main()
