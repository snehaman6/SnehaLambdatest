from PageObject.login_page import LoginPage
from PageObject.registration_page import RegistrationPage
from testcases.base_test import BaseTest


class TestRegistration(BaseTest):

    def test_registration_02(self):
        self.rp = RegistrationPage(self.driver)
        self.rp.Click_Rebutton()
        self.rp.Enter_Firstname("Selenium")
        self.rp.Enter_Lastname("Python")
        self.rp.Enter_Emailid("Selenium_python@gmail.com")
        self.rp.Enter_TeleNum(96665218682)
        self.rp.Enter_Password("@1234")
        self.rp.Enter_ConfirmPassword("@1234")
        self.rp.Click_Radiobutton()
        self.rp.Click_Checkbox()
        self.rp.Click_Conbutton()
        self.lp = LoginPage(self.driver)
        if self.lp.status() == True:
            self.driver.save_screenshot("G:\\PytestFramework\\Screenshots\\test_login_01_passed.png")
            return True
        else:
            self.driver.save_screenshot("G:\\PytestFramework\\Screenshots\\test_login_01_failed.png")
            return False
