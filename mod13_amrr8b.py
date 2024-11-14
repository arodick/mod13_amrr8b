Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import unittest
import re
from datetime import datetime

def validate_symbol(symbol):
    return bool(re.match(r'^[A-Z]{1,7}$', symbol))

def validate_chart_type(chart_type):
    return chart_type in ["1", "2"]

def validate_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_end_date(start_date, end_date):
...     start = datetime.strptime(start_date, '%Y-%m-%d')
...     end = datetime.strptime(end_date, '%Y-%m-%d')
...     return end >= start
... 
... class TestStockDataInputs(unittest.TestCase):
...     
...     def test_symbol(self):
...         self.assertTrue(validate_symbol("AAPL"))
...         self.assertTrue(validate_symbol("GOOG"))
...         self.assertFalse(validate_symbol("apple"))
...         self.assertFalse(validate_symbol("AAPL123"))
...         self.assertFalse(validate_symbol("A"))
... 
...     def test_chart_type(self):
...         self.assertTrue(validate_chart_type("1"))
...         self.assertTrue(validate_chart_type("2"))
...         self.assertFalse(validate_chart_type("3"))
...         self.assertFalse(validate_chart_type("0"))
...         self.assertFalse(validate_chart_type("12"))
... 
...     def test_time_series(self):
...         self.assertTrue(validate_time_series("1"))
...         self.assertTrue(validate_time_series("4"))
...         self.assertFalse(validate_time_series("5"))
...         self.assertFalse(validate_time_series("0"))
...         self.assertFalse(validate_time_series("12"))
... 
...     def test_start_date(self):
...         self.assertTrue(validate_date("2024-11-14"))
...         self.assertFalse(validate_date("14-11-2024"))
...         self.assertFalse(validate_date("2024/11/14"))
... 
...     def test_end_date(self):
...         self.assertTrue(validate_end_date("2024-11-14", "2024-11-15"))
...         self.assertTrue(validate_end_date("2024-11-14", "2024-11-14"))
...         self.assertFalse(validate_end_date("2024-11-14", "2024-11-13"))
... 
... if __name__ == '__main__':
...     unittest.main()
