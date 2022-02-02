import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
s =  Service("/Applications/Firefox.app/Contents/MacOS/firefox")


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path="/Users/daniloribeirosoares/Documents/projetos/superlists/geckodriver"
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_ad_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000")

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()