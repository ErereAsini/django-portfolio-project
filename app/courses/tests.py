# pylint: disable=E0401
# pylint: disable=E1101
from django.test import TestCase
from django.urls import reverse
import pytest
from courses.models import Course

# Create your tests here.


def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_course():
    course = Course.objects.create(
        title='Pytest',
        course_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Course on how to apply pytest to a Django application',
        published=True
    )
    assert course.title == "Pytest"

@pytest.fixture
def new_course(db):
    course = Course.objects.create(
        title='Pytest',
        course_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Course on how to apply pytest to a Django application',
        published=True
    )
    return course

def test_search_courses(new_course):
    assert Course.objects.filter(title='Pytest').exists()

def test_update_course(new_course):
    new_course.title = 'Pytest-Django'
    new_course.save()
    assert Course.objects.filter(title='Pytest-Django').exists()

@pytest.fixture
def another_course(db):
    course = Course.objects.create(
        title='More-Pytest',
        course_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Course on how to apply pytest to a Django application',
        published=True
    )
    return course

def test_compare_courses(new_course, another_course):
    assert new_course.pk != another_course.pk