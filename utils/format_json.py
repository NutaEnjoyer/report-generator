import json

def format_payout_report(json_data: str) -> str:
    data = json.loads(json_data)
    lines = []
    lines.append(f"{'':<16} {'name':<20} {'hours':<6} {'rate':<5} {'payout'}")

    for dept in data:
        print(dept)
        print(type(dept))
        lines.append(dept["department"])
        for emp in dept["employees"]:
            lines.append(
                f"{'':<16} {emp['name']:<20} {emp['hours_worked']:<6} {emp['rate']:<5} ${emp['payout']}"
            )
        lines.append(
            f"{'':<16} {'':<20} {dept['total_hours']:<6} {'':<5} ${dept['total_payout']}"
        )
        lines.append("")

    return "\n".join(lines)
