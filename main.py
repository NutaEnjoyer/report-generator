from reports import get_report
from parsers.csv_parser import CSVParser
from utils.get_args import get_args


def main_func():
    args = get_args()
    report_type: str = args.get("report_type")
    input_files: list[str] = args.get("input_files")
    report_class = get_report(report_type)
    csv_parser = CSVParser()

    if report_class is None:
        raise ValueError(f"Invalid report type: {report_type}")

    try:
        data: list[dict] = csv_parser.parse_csv_files(input_files)
    except Exception as e:
        raise ValueError(f"Error while parsing CSV files: {e}")

    try:
        report = report_class(data)
    except Exception as e:
        raise ValueError(f"Error while generating report: {e}")

    return report


def main():
    report = main_func()
    print(report)

    json_output = report.json
    return json_output


if __name__ == "__main__":  # pragma: no cover
    main()
