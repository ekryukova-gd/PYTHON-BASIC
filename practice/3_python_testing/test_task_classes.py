"""
Write tests for classes in python_part_2/task_classes_solved.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import pytest
import datetime
from practice.python_part_2.task_classes_solved import *

# homeworks = [
#     ['homework1', 5],
#     ['homework2', 0],
#     ['homework3', -1]
# ]
#
# teachers = [
#     ('Ivanov', 'Ivan'),
#     ('', ''),
#     (1231, 4312)
# ]
@pytest.mark.classes
# @pytest.mark.parametrize(
#     'homework',
#     homeworks,
#     indirect=True
# )
def test_Homework(homework):
    assert homework.deadline.days == 5
    assert homework.created.date() == datetime.date.today()
    assert homework.is_active() is True

@pytest.mark.classes
# @pytest.mark.parametrize(
#     'teacher',
#     teachers,
#     indirect=True
# )
def test_Teacher(teacher):
    assert teacher.last_name == 'Ivanov'
    assert teacher.first_name == 'Petr'
    assert isinstance(teacher.create_homework('homework_text_2', 2), Homework)

@pytest.mark.classes
def test_Student(student, homework):
    assert student.last_name == 'Sidorov'
    assert student.first_name == 'Ivan'
    if homework.is_active():
        assert student.do_homework(homework) == homework
    else:
        assert student.do_homework(homework) is None
