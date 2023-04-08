from employee import Employee
import pytest

@pytest.fixture
def employee_instance():
    return Employee('Juan', 'Camaney', 5000)

def test_give_default_raise(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 10_000

def test_give_custom_raise(employee_instance):
    employee_instance.give_raise(1000)
    assert employee_instance.annual_salary == 6000