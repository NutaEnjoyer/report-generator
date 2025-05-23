import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from parsers.csv_parser import CSVParser


@pytest.fixture
def csv_files(tmp_path):
    file1 = tmp_path / "test_data_1.csv"
    file1.write_text(
        """department,id,email,name,hours_worked,rate
                     HR,101,grace@example.com,Grace Lee,160,45
                    Marketing,102,henry@example.com,Henry Martin,150,35
                    HR,103,ivy@example.com,Ivy Clark,158,38"""
    )

    file2 = tmp_path / "test_data_2.csv"
    file2.write_text(
        """email,name,department,hours_worked,salary,id
                     karen@example.com,Karen White,Sales,165,50,201
                     liam@example.com,Liam Harris,HR,155,42,202"""
    )

    return [str(file1), str(file2)]


def test_parse_csv_files_row_count(csv_files):
    csv_parser = CSVParser()

    result = csv_parser.parse_csv_files(csv_files)
    assert len(result) == 5


def test_parse_csv_files_row_content(csv_files):
    csv_parser = CSVParser()

    result = csv_parser.parse_csv_files(csv_files)

    liam_row = next((row for row in result if row["name"] == "Liam Harris"), None)

    assert liam_row is not None
    assert liam_row["id"] == "202"
    assert liam_row["name"] == "Liam Harris"
    assert liam_row["email"] == "liam@example.com"
    assert liam_row["department"] == "HR"
    assert liam_row["hours_worked"] == "155"
    assert liam_row["rate"] == "42"
