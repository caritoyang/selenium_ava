import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from ddt import ddt, file_data
import sys
import os

sys.path.append("D://Kinuko//selenium_ava")
from page_objects.careers_page import LoginPage

@ddt
class TestLogin(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.get("https://obdbqa64615.obfuscate.xcade.dev/en_US/careers/")
        cls.driver.maximize_window()
        cls.login_page = LoginPage(driver=cls.driver)

    def test_sign_in(self):
        self.login_page.sign_in()
        time.sleep(2)
        is_signin_successful = self.login_page.is_signin_successful()
        assert is_signin_successful is True

    @file_data(os.path.join("../data","careers_page.json"))
    def test_login(self, user_val, pass_val):
        self.login_page.login_in(username=user_val, password=pass_val)
        time.sleep(2)
        is_login_successful = self.login_page.is_login_successful()
        self.assertEqual(is_login_successful, "My Profile | Company", msg="The title is different.")

    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/Kinuko/selenium_ava/report"))