
## __results from 2023-06-28__ testing -> main ![Static Badge](https://img.shields.io/badge/test-fail-red)

EEEEEEEEEF                                                               [100%]
==================================== ERRORS ====================================
_________________________ ERROR at setup of test_init __________________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
_______________________ ERROR at setup of test_forename ________________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
________________________ ERROR at setup of test_surname ________________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
______________________ ERROR at setup of test_no_surname _______________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
____________________ ERROR at setup of test_birthday_party _____________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
__________________ ERROR at setup of test_invalid_short_email __________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
__________________ ERROR at setup of test_invalid_no_at_email __________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
_____________________ ERROR at setup of test_salary_raise ______________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
_________________ ERROR at setup of test_negative_salary_raise _________________

    @pytest.fixture()
    def employee():
>       return Employee("Ori Aviad", 17, 5000, "oriaviad2006@gmail.com")
E       TypeError: 'module' object is not callable

test_employee.py:8: TypeError
=================================== FAILURES ===================================
____________________________ test_intentional_fail _____________________________

    def test_intentional_fail():
>       pytest.fail()
E       Failed

test_employee.py:71: Failed
=========================== short test summary info ============================
FAILED test_employee.py::test_intentional_fail - Failed
ERROR test_employee.py::test_init - TypeError: 'module' object is not callable
ERROR test_employee.py::test_forename - TypeError: 'module' object is not callable
ERROR test_employee.py::test_surname - TypeError: 'module' object is not callable
ERROR test_employee.py::test_no_surname - TypeError: 'module' object is not callable
ERROR test_employee.py::test_birthday_party - TypeError: 'module' object is not callable
ERROR test_employee.py::test_invalid_short_email - TypeError: 'module' object is not callable
ERROR test_employee.py::test_invalid_no_at_email - TypeError: 'module' object is not callable
ERROR test_employee.py::test_salary_raise - TypeError: 'module' object is not callable
ERROR test_employee.py::test_negative_salary_raise - TypeError: 'module' object is not callable
1 failed, 9 errors in 0.05s
