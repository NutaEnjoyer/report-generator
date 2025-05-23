from collections import defaultdict
import json

from reports.base_report import BaseReport


class PayoutReport(BaseReport):
    def generate_report(self) -> str:

        departments = defaultdict(list)
        report: list[defaultdict] = []

        for person in self.data:
            payout: int = int(person["rate"]) * int(person["hours_worked"])
            person["payout"] = payout
            departments[person["department"]].append(person)

        # group by department
        for department, people in departments.items():
            department_report = {
                "department": department,
                "employees": [],
                "total_hours": 0,
                "total_payout": 0,
            }

            for p in people:
                department_report["employees"].append(
                    {
                        "name": p["name"],
                        "hours_worked": int(p["hours_worked"]),
                        "rate": int(p["rate"]),
                        "payout": p["payout"],
                    }
                )
                department_report["total_payout"] += p["payout"]
                department_report["total_hours"] += int(p["hours_worked"])

            report.append(department_report)

        return json.dumps(report)

    def __str__(self) -> str:
        data = json.loads(self.report_json)
        lines = []
        lines.append(f"{'':<16} {'name':<20} {'hours':<6} {'rate':<5} {'payout'}")

        for dept in data:
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
