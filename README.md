
## __results from 2023-07-02__ yaml -> main ![Static Badge](https://img.shields.io/badge/test-fail-red)

.F...xx.x                                                                [100%]
=================================== FAILURES ===================================
________________________________ test_forename _________________________________

employee = <Employee.Employee object at 0x7fb5c2029840>

    def test_forename(employee: Employee):
>       assert employee.forename == "Oi"
E       AssertionError: assert 'Ori' == 'Oi'
E         - Oi
E         + Ori
E         ?  +

test_employee.py:20: AssertionError
=========================== short test summary info ============================
FAILED test_employee.py::test_forename - AssertionError: assert 'Ori' == 'Oi'
  - Oi
  + Ori
  ?  +
1 failed, 5 passed, 3 xfailed in 0.04s
