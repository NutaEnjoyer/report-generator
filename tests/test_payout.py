import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reports.payout_report import generate_payout_report
from reports import get_report


def test_get_report():
    assert get_report("payout") is generate_payout_report


def test_invalid_report_type():
    assert get_report("invalid_report_type") is None


def test_generate_payout_report_to_cmd():
    data = [
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

    result = generate_payout_report(data)

    assert "HR" in result
    assert "Grace Lee" in result
    assert "160" in result
    assert "45" in result
    assert "$7200" in result  # 160 * 45
