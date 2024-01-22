from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:
    text_username = (By.XPATH,"//input[@id='input-email']")
    text_password = (By.ID,"input-password")
    click_login = (By.XPATH,"//input[@value='Login']")
    status_check = (By.XPATH, "//a[@role='button']//span[@class='title'][normalize-space()='My account']")

    def __init__(self,driver):
        self.driver = driver

    def Enter_UserName(self, username):
        self.driver.find_element(*LoginPage.text_username).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*LoginPage.text_password).send_keys(password)

    def Click_LoginButton(self):
        self.driver.find_element(*LoginPage.click_login).click()

    def status(self):
        try:
            self.driver.find_element(*LoginPage.status_check).is_displayed()
            return True
        except NoSuchElementException:
            return False



