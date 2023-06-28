
## __results from 2023-06-28__ testing -> master ![Static Badge](https://img.shields.io/badge/test-fail-red)

.....xxFxF                                                               [100%]
=================================== FAILURES ===================================
______________________________ test_salary_raise _______________________________

employee = <Employee.Employee object at 0x7fb463b6ee00>

    def test_salary_raise(employee: Employee, ):
        amount = 100
        salary = employee.salary
        employee.raise_salary(amount)
        salary += amount
>       assert employee.salary == salary
E       assert 500000 == 5100
E        +  where 500000 = <Employee.Employee object at 0x7fb463b6ee00>.salary

test_employee.py:60: AssertionError
____________________________ test_intentional_fail _____________________________

    def test_intentional_fail():
>       pytest.fail()
E       Failed

test_employee.py:71: Failed
=========================== short test summary info ============================
FAILED test_employee.py::test_salary_raise - assert 500000 == 5100
 +  where 500000 = <Employee.Employee object at 0x7fb463b6ee00>.salary
FAILED test_employee.py::test_intentional_fail - Failed
2 failed, 5 passed, 3 xfailed in 0.06s
