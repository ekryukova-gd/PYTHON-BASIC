import pytest
from collections import namedtuple

from practice.python_part_2.task_classes_solved import *


# ----------------- fixtures for test_task_classes -------------------
# @pytest.fixture
# def homework():
#     return Homework('homework_text_1', 5)
#
# @pytest.fixture
# def teacher():
#     return Teacher('Ivanov', 'Petr')
#
# @pytest.fixture
# def student():
#     return Student('Sidorov', 'Ivan')


homeworks = [
    ['homework1', 5],
    ['homework2', 0],
#    ['homework3', -1]
]

homework_output = [5, 0]


@pytest.fixture(scope='session', params=(homeworks, homework_output))
def homework(request):
    return Homework(*request.param), *homework_output


teachers = [
    ('Ivanov', 'Ivan'),
    ('', ''),
#    (1231, 4312)
]

teacher_output = namedtuple('teachers_output', ['last_name', 'first_name'])
output_teachers = [
    teacher_output('Ivanov', 'Ivan'),
    teacher_output('', '')]


@pytest.fixture(scope='session', params=(teachers, teacher_output))
def teacher(request):
    return Teacher(*request.param), *teacher_output


students = [
    ('Markova', 'Irina'),
    ('', ''),
    (789, 987)
]

student_output = namedtuple('student_output', ['last_name', 'first_name'])
output_students = [
    student_output('Markova', 'Irina'),
    student_output('', '')]


@pytest.fixture(scope='session', params=(students, student_output))
def student(request):
    return Student(*request.param), *student_output