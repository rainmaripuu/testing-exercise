from datetime import datetime
from unittest.mock import Mock

import pytest

from prog import read_from_file, read_line, write_to_file


def test_file_operations(file_data):
    assert read_line(file_data) == (datetime(2020, 1, 18, 13, 49, 47), "text")



def test_read_from_file(existing_file):
    buffer, parsed = read_from_file(existing_file)

    assert parsed == [
        (
            datetime(2020, 1, 18, 13, 49, 47),
            'text'
        )
    ]


def test_write_to_file(writable_file):
    mock_datetime = Mock()
    # mock_datetime.now = Mock(return_value=datetime(2020, 1, 19, 9, 0, 0))
    mock_datetime.now().isoformat = Mock(return_value=datetime(2020, 1, 19, 9, 0, 0).isoformat())
    write_to_file("test data", writable_file, datetime=mock_datetime)
    with open(writable_file, 'r') as f:
        date, text = f.read().split(',', 1)
        assert text.strip() == "test data"
        assert date == datetime(2020, 1, 19, 9, 0, 0).isoformat()

    # assert mock_datetime.now.call_count == 1
    # assert mock_datetime.now().isoformat.call_count == 1
