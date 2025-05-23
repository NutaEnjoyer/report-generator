import argparse


def get_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_files", nargs="+", type=str, help="input files")
    parser.add_argument("--report", required=True, help="report type")
    args = parser.parse_args()

    report_type: str = args.report.lower()
    input_files: list[str] = args.input_files

    return {"report_type": report_type, "input_files": input_files}
