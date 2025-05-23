import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reports.payout_report import PayoutReport
from reports import get_report


def test_get_report():
    assert get_report("payout") is PayoutReport


def test_invalid_report_type():
    assert get_report("invalid_report_type") is None
