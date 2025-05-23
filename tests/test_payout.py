import json
import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reports.payout_report import PayoutReport


@pytest.fixture
def payout_report_data():
    return [
        {
            "department": "HR",
            "id": "101",
            "email": "grace@example.com",
            "name": "Grace Lee",
            "hours_worked": "160",
            "rate": "45",
        },
        {
            "department": "Marketing",
            "id": "102",
            "email": "henry@example.com",
            "name": "Henry Martin",
            "hours_worked": "150",
            "rate": "35",
        },
        {
            "department": "HR",
            "id": "103",
            "email": "ivy@example.com",
            "name": "Ivy Clark",
            "hours_worked": "158",
            "rate": "38",
        },
    ]


def test_generate_payout_report_str(payout_report_data):
    result = PayoutReport(payout_report_data)
    str_result = str(result)

    assert "HR" in str_result
    assert "Grace Lee" in str_result
    assert "$7200" in str_result
    assert "Henry Martin" in str_result
    assert "Marketing" in str_result
    assert "$5250" in str_result
    assert "Ivy Clark" in str_result
    assert "$6004" in str_result


def test_generate_payout_report_json(payout_report_data):
    result = PayoutReport(payout_report_data)
    json_result = json.loads(result.json)

    assert isinstance(json_result, list)
    assert len(json_result) == 2

    person = next(
        (
            item
            for dep in json_result
            for item in dep["employees"]
            if item["name"] == "Grace Lee"
        ),
        None,
    )

    assert person is not None
    assert person["hours_worked"] == 160
    assert person["rate"] == 45
    assert person["payout"] == 160 * 45
