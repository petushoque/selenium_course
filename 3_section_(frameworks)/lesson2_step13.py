import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_registration_page_1(self):
        
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements_by_tag_name("input")
        for element in elements:
            element.send_keys("Привет, мир")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        
    def test_registration_page(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_block_first = browser.find_element_by_css_selector(".first_block .first")
        first_block_first.send_keys("Test first name")
        first_block_second = browser.find_element_by_css_selector(".first_block .second")
        first_block_second.send_keys("Test last name")
        first_block_third = browser.find_element_by_css_selector(".first_block .third")
        first_block_third.send_keys("Test email")
        button = browser.find_element_by_css_selector("button.btn")
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
