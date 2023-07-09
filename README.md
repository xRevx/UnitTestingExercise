2023-07-09-10-34-21 

![Tests](https://github.com/xRevx/UnitTestingExercise/actions/workflows/main.yml/badge.svg) 


## Test Results
<?xml version="1.0" encoding="utf-8"?><testsuites><testsuite name="pytest" errors="0" failures="1" skipped="3" tests="10" time="0.064" timestamp="2023-07-09T10:34:09.502021" hostname="fv-az1250-48"><testcase classname="test_employee" name="test_init" time="0.001" /><testcase classname="test_employee" name="test_forename" time="0.001" /><testcase classname="test_employee" name="test_surname" time="0.001" /><testcase classname="test_employee" name="test_no_surname" time="0.001" /><testcase classname="test_employee" name="test_birthday_party" time="0.001" /><testcase classname="test_employee" name="test_invalid_short_email" time="0.001"><skipped type="pytest.xfail" message="" /></testcase><testcase classname="test_employee" name="test_invalid_no_at_email" time="0.001"><skipped type="pytest.xfail" message="" /></testcase><testcase classname="test_employee" name="test_salary_raise" time="0.001" /><testcase classname="test_employee" name="test_negative_salary_raise" time="0.001"><skipped type="pytest.xfail" message="" /></testcase><testcase classname="test_employee" name="test_fail" time="0.001"><failure message="Failed">def test_fail():
&gt;       pytest.fail()
E       Failed

test_employee.py:70: Failed</failure></testcase></testsuite></testsuites>