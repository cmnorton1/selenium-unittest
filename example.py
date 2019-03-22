import unittest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()

class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com")

    def test_page_load(self):
        self.assertIn("Google", self.driver.title)

    def test_search_post(self):
        driver = self.driver
        query = "dog"
        send_search(driver, query)
        time.sleep(2)
        self.assertIn(query, driver.title)

    def test_relevant_results(self):
        driver = self.driver
        query = "dog"
        send_search(driver, query)
        time.sleep(2)
        results = driver.find_elements_by_class_name("g")
        self.assertIn(query, results[0].text)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


#utility function
def send_search(driver, query):
    search_field = driver.find_element_by_name("q")
    search_field.clear()
    search_field.send_keys(query)
    search_field.send_keys(Keys.RETURN)
