from collections import defaultdict


def generate_payout_report_to_cmd(data: list[dict]) -> str:
    departments = defaultdict(list)
    lines: list[str] = []

    for person in data:
        payout: int = int(person['rate']) * int(person['hours_worked'])
        person["payout"] = payout
        departments[person['department']].append(person)
    
    lines.append(f"{'':<16} {'name':<20} {'hours':<6} {'rate':<5} {'payout'}")

    for department, people in departments.items():
        lines.append(department)
        total = 0
        total_hours = 0

        for p in people:
            total += p['payout']
            total_hours += int(p['hours_worked'])
            lines.append(f"{'':<16} {p['name']:<20} {p['hours_worked']:<6} {p['rate']:<5} ${p['payout']}")

        lines.append(f"{'':<16} {'':<20} {total_hours:<6} {'':<5} ${total}")
        lines.append("")

    return "\n".join(lines)
