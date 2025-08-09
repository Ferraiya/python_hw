import os
import pytest

from count_lines import count_lines
from file_creating import create_new_file

class TestLines:

    def __init__(self):
        pass

@pytest.fixture
def new_file():
    create_new_file()
    yield
    if os.path.exists('b_file.txt'):
        os.remove('b_file.txt')

def test_lines_0(new_file):

    count = count_lines('b_file.txt')
    assert count == 0

def test_lines_1(new_file):
    f = open('b_file.txt', 'w')
    f.write("11111")
    f.close()

    count = count_lines('b_file.txt')
    assert count == 1

def test_lines_more_than_1(new_file):
    f = open("b_file.txt", "w")
    l = ['1', '23', '532234', 'dfewsdf', (34,2,4,2)]
    for elem in l:
        f.write(f"{elem}\n")
    f.close()

    count = count_lines('b_file.txt')
    assert count == 5




