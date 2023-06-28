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
