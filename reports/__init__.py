from reports.payout_report import generate_payout_report_to_cmd


REPORT_TYPES = {
    'payout': generate_payout_report_to_cmd,
}

def get_report(name: str):
    return REPORT_TYPES.get(name)

