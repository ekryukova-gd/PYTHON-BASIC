import pytest

from practice.python_part_2.task_classes_solved import *



@pytest.fixture
def homework():
    return Homework('homework_text_1', 5)

@pytest.fixture
def teacher():
    return Teacher('Ivanov', 'Petr')

@pytest.fixture
def student():
    return Student('Sidorov', 'Ivan')


