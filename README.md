# UnitTestingExercise
## __results from 2023-06-28__ testing -> master ![Static Badge](https://img.shields.io/badge/test-fail-red)


==================================== ERRORS ====================================
___________________ ERROR collecting tests/test_employee.py ____________________
ImportError while importing test module '/home/runner/work/UnitTestingExercise/UnitTestingExercise/tests/test_employee.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests/test_employee.py:3: in <module>
    from Employee import Employee
E   ModuleNotFoundError: No module named 'Employee'
=========================== short test summary info ============================
ERROR tests/test_employee.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.07s
.....xxx                                                                 [100%]
5 passed, 3 xfailed in 0.03s

## __results from 2023-06-28__ testing -> master ![Static Badge](https://img.shields.io/badge/test-pass-green)

.....xxFxF                                                               [100%]
=================================== FAILURES ===================================
______________________________ test_salary_raise _______________________________

employee = <Employee.Employee object at 0x7f5bf70d26b0>

    def test_salary_raise(employee: Employee, ):
        amount = 100
        salary = employee.salary
        employee.raise_salary(amount)
        salary += amount
>       assert employee.salary == salary
E       assert 500000 == 5100
E        +  where 500000 = <Employee.Employee object at 0x7f5bf70d26b0>.salary

test_employee.py:60: AssertionError
____________________________ test_intentional_fail _____________________________

    def test_intentional_fail():
>       pytest.fail()
E       Failed

test_employee.py:71: Failed
=========================== short test summary info ============================
FAILED test_employee.py::test_salary_raise - assert 500000 == 5100
 +  where 500000 = <Employee.Employee object at 0x7f5bf70d26b0>.salary
FAILED test_employee.py::test_intentional_fail - Failed
2 failed, 5 passed, 3 xfailed in 0.04s

## __results from 2023-06-28__ testing -> master ![Static Badge](https://img.shields.io/badge/test-fail-red)

