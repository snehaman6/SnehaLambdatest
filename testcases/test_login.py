import logging

from PageObject.login_page import LoginPage
from testcases.base_test import BaseTest
from utilities.ReadConfigFile import ReadConfig

from utilities.logger import loggen


class TestLogin(BaseTest):
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_login_01(self):
        logger = loggen()

        logger.info("Testcase test_login_01 is started")
        logger.info("Invoking Browser")
        self.lp = LoginPage(self.driver)
        logger.info("Entering Email--->" + self.username)
        # self.lp.Enter_UserName("Selenium_python@gmail.com")
        self.lp.Enter_UserName(self.username)

        logger.info("Entering Password--->" + self.password)
        # self.lp.Enter_Password("@1234")
        self.lp.Enter_Password(self.password)

        logger.info("Clicking on Login button")
        self.lp.Click_LoginButton()
        if self.lp.status() == True:
            logger.info("Testcase test_login_01 is Passed")
            self.driver.save_screenshot("G:\\SnehaLambdatest\\Screenshots\\test_login_01_passed.png")
        else:
            logger.info("Testcase test_login_01 is Failed")
            self.driver.save_screenshot("G:\\SnehaLambdatest\\Screenshots\\test_login_01_failed.png")
