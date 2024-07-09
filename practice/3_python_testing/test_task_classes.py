"""
Write tests for classes in python_part_2/task_classes_solved.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import pytest
import datetime
from practice.python_part_2.task_classes_solved import *


@pytest.mark.classes
def test_Homework(homework):
    assert homework[0].deadline.days == homework[1]
    assert homework[0].created.date() == datetime.date.today()
 #   assert homework.is_active() is True


@pytest.mark.classes
def test_Teacher(teacher):
    assert teacher[0].last_name == teacher[1].last_name
    assert teacher[0].first_name == teacher[0].first_name
    assert isinstance(teacher.create_homework('homework_text_2', 2), Homework)


@pytest.mark.classes
def test_Student(student, homework):
    assert student[0].last_name == student[1].last_name
    assert student[0].first_name == student[1].first_name
    if homework.is_active():
        assert student.do_homework(homework) == homework
    else:
        assert student.do_homework(homework) is None
