from reports.payout_report import PayoutReport


REPORT_TYPES = {
    "payout": PayoutReport,
}


def get_report(name: str):
    return REPORT_TYPES.get(name)
