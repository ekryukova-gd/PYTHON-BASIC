"""
Write tests for classes in python_part_2/task_classes_solved.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import pytest
import datetime
import practice.python_part_2.task_classes_solved as classes_solved


@pytest.fixture
def homework(task_text, days_to_complete):
    return classes_solved.Homework(task_text, days_to_complete)


@pytest.mark.parametrize('task_text, days_to_complete, expected_text, expected_days',
                         [("task_text_1", 5, "task_text_1", 5),
                         ("task_text_2", 0, "task_text_2", 0),
                          ("task_text_3", -1, "task_text_3", -1)])
def test_Homework(homework, task_text, days_to_complete, expected_text, expected_days):
    assert homework.deadline.days == expected_days
    assert homework.text == expected_text
    assert homework.created.date() == datetime.date.today()
    if days_to_complete > 0 :
        assert homework.is_active() is True
    else:
        assert homework.is_active() is False


@pytest.fixture
def teacher(last_name, first_name):
    return classes_solved.Teacher(last_name, first_name)


@pytest.mark.parametrize('last_name, first_name, expected_last_name, expected_first_name',
                         [('Ivanov', 'Ivan', 'Ivanov', 'Ivan'),
                         ('', 'Petr', '', 'Petr')])
def test_Teacher(teacher, last_name, first_name, expected_last_name, expected_first_name):
    assert teacher.last_name == expected_last_name
    assert teacher.first_name == expected_first_name
    assert isinstance(teacher.create_homework('test_task_text', 5), classes_solved.Homework)


@pytest.fixture
def student(last_name, first_name):
    return classes_solved.Student(last_name, first_name)
@pytest.mark.parametrize('last_name, first_name, expected_last_name, expected_first_name, task_text, days_to_complete',
                         [('Ivanov', 'Ivan', 'Ivanov', 'Ivan', 'task_text1', 5),
                         ('', 'Petr', '', 'Petr', 'task_text2', 0)])
def test_Student(homework, student, last_name, first_name, expected_last_name, expected_first_name):
    assert student.last_name == expected_last_name
    assert student.first_name == expected_first_name
    if homework.is_active():
        assert isinstance(student.do_homework(homework), classes_solved.Homework)
    else:
        assert student.do_homework(homework) is None

