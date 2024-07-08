import pytest

from practice.python_part_2.task_classes_solved import *



@pytest.fixture
def homework(text, days_to_complete):
    return Homework(text, days_to_complete)

@pytest.fixture
def teacher(last_name, first_name):
    return Teacher(last_name, first_name)

@pytest.fixture
def student(last_name, first_name):
    return Student(last_name, first_name)


