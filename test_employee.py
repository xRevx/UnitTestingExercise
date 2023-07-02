import pytest

from Employee import Employee


@pytest.fixture()
def employee():
    return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")


def test_init(employee: Employee):
    assert employee.name == "Ori Aviad"
    assert employee.age == 17
    assert employee.salary == 5000
    assert employee.email == "oriaviad2006@gmail.com"


# forename needs to be the first word in the full name
def test_forename(employee: Employee):
    assert employee.forename == "Ori"


# surname is the second word in the full name
def test_surname(employee: Employee):
    assert employee.surname == "Aviad"


# employee can have no surname check if surname is none
def test_no_surname(employee: Employee):
    employee.name = "Ori"
    assert not employee.surname


# birthday party +1 employee age
def test_birthday_party(employee: Employee):
    employee.birthday_party()
    assert employee.age == 18


# length before @ in the email must be >=6
@pytest.mark.xfail(raises=ValueError)
def test_invalid_short_email(employee: Employee):
    employee.email = "ori@"
    employee.is_valid_email()


# email must include @
@pytest.mark.xfail(raises=ValueError)
def test_invalid_no_at_email(employee: Employee):
    employee.email = "ori"
    employee.is_valid_email()


# salary raise should add the amount given
def test_salary_raise(employee: Employee, ):
    amount = 100
    salary = employee.salary
    employee.raise_salary(amount)
    salary += amount
    assert employee.salary == salary


# salary raise must be more than 0
@pytest.mark.xfail(raises=ValueError)
def test_negative_salary_raise(employee: Employee, ):
    amount = -100
    employee.raise_salary(amount)
