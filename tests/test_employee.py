import pytest

from company.Employee import Employee


@pytest.fixture()
def employee():
    return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")


def test_init(employee: Employee):
    assert employee.name == "Ori Aviad"
    assert employee.age == 17
    assert employee.salary == 5000
    assert employee.email == "oriaviad2006@gmail.com"


def test_forename(employee: Employee):
    assert employee.forename == "Ori"


def test_surname(employee: Employee):
    assert employee.surname == "Aviad"


def test_no_surname(employee: Employee):
    employee.name = "Ori"
    assert not employee.surname


def test_birthday_party(employee: Employee):
    employee.birthday_party()
    assert employee.age == 18
