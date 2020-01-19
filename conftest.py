import os
import tempfile
import pytest
from datetime import datetime

@pytest.fixture()
def file_data():
    yield '2020-01-18T13:49:47,text'


@pytest.fixture()
def existing_file():
    with tempfile.NamedTemporaryFile("w") as tmp_file:
        file_name = tmp_file.name

    with open(file_name, 'w') as f:
        f.write('2020-01-18T13:49:47,text')

    yield file_name

    os.remove(file_name)


@pytest.fixture()
def writable_file():
    with tempfile.NamedTemporaryFile("w") as tmp_file:
        file_name = tmp_file.name

    yield file_name

    os.remove(file_name)
