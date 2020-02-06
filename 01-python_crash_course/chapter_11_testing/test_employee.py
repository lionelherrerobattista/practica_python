import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for class Employee"""
    def setUp(self):
        """
        Create an Employee for use in test cases
        """
        self.new_employee = Employee('Juan', 'Pérez', 15000)
        
    def test_give_default_raise(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.annual_salary, 15000 + 5000)
    
    def test_give_custom_raise(self):
        self.new_employee.give_raise(6000)
        self.assertEqual(self.new_employee.annual_salary, 15000 + 6000)
        
unittest.main()
