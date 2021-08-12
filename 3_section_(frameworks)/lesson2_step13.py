import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_registration_page_1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
