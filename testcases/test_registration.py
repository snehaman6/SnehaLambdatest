from PageObject.login_page import LoginPage
from PageObject.registration_page import RegistrationPage
from testcases.base_test import BaseTest
from utilities.ReadConfigFile import ReadConfig
from utilities.logger import loggen


class TestRegistration(BaseTest):
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_registration_02(self):
        logger = loggen()

        logger.info("Testcase test_registration_02  is started")
        self.rp = RegistrationPage(self.driver)
        logger.info("Click on Register button")
        self.rp.Click_Rebutton()
        logger.info("Enter First name")
        self.rp.Enter_Firstname("Selenium")
        logger.info("Enter Last name")
        self.rp.Enter_Lastname("Python")
        logger.info("Entering Email--->" + self.username)
        #self.rp.Enter_Emailid("Selenium_python@gmail.com")
        logger.info("Enter Mobile Number")
        self.rp.Enter_TeleNum(96665218682)
        logger.info("Entering Password--->" + self.password)
        #self.rp.Enter_Password("@1234")
        self.rp.Enter_ConfirmPassword("@1234")
        logger.info("Click on Radio button")
        self.rp.Click_Radiobutton()
        logger.info("Click on Checkbox")
        self.rp.Click_Checkbox()
        logger.info("Click on Continue button")
        self.rp.Click_Conbutton()
        self.lp = LoginPage(self.driver)
        if self.lp.status() == True:
            logger.info("Testcase test_registration_02  is Passed")
            self.driver.save_screenshot("G:\\PytestFramework\\Screenshots\\test_login_01_passed.png")

        else:
            logger.info("Testcase test_registration_02  is Failed")
            self.driver.save_screenshot("G:\\PytestFramework\\Screenshots\\test_login_01_failed.png")

