2023-07-08-19-28-27 

Test Status: failure 
 OS: ubuntu-latest and python version: 3.10 

.....xx.xF
=================================== FAILURES ===================================
__________________________________ test_fail ___________________________________

    def test_fail():
>       pytest.fail()
E       Failed

test_employee.py:71: Failed
=========================== short test summary info ============================
FAILED test_employee.py::test_fail - Failed
1 failed, 6 passed, 3 xfailed in 0.05s


Test Status: failure 
 OS: ubuntu-latest and python version: 3.11 

.....xx.xF
=================================== FAILURES ===================================
__________________________________ test_fail ___________________________________

    def test_fail():
>       pytest.fail()
E       Failed

test_employee.py:71: Failed
=========================== short test summary info ============================
FAILED test_employee.py::test_fail - Failed
1 failed, 6 passed, 3 xfailed in 0.06s


