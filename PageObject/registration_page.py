from selenium.webdriver.common.by import By


class RegistrationPage:
    Re_button = (By.XPATH,"//a[contains(text(),'Register')]")
    FirstName = (By.ID,"input-firstname")
    LastName = (By.ID,"input-lastname")
    Eid = (By.ID, "input-email")
    Telephone = (By.ID, "input-telephone")
    Password = (By.ID,"input-password")
    PasswordConfirm = (By.ID,"input-confirm")
    RButton = (By.XPATH,"//label[normalize-space()='No']")
    Checkbox = (By.XPATH,"//label[@for='input-agree']")
    ConButton = (By.XPATH,"//input[@value='Continue']")

    def __init__(self,driver):
        self.driver = driver

    def Click_Rebutton(self):
        self.driver.find_element(*RegistrationPage.Re_button).click()

    def Enter_Firstname(self,firstname):
        self.driver.find_element(*RegistrationPage. FirstName).send_keys(firstname)

    def Enter_Lastname(self,lastname):
        self.driver.find_element(*RegistrationPage. LastName).send_keys(lastname)

    def Enter_Emailid(self,emailid):
        self.driver.find_element(*RegistrationPage.Eid).send_keys(emailid)

    def Enter_TeleNum(self,telnum):
        self.driver.find_element(*RegistrationPage.Telephone).send_keys(telnum)

    def Enter_Password(self,password):
        self.driver.find_element(*RegistrationPage.Password).send_keys(password)

    def Enter_ConfirmPassword(self,conpassword):
        self.driver.find_element(*RegistrationPage.PasswordConfirm).send_keys(conpassword)

    def Click_Radiobutton(self):
        self.driver.find_element(*RegistrationPage.RButton).click()

    def Click_Checkbox(self):
        self.driver.find_element(*RegistrationPage.Checkbox).click()

    def Click_Conbutton(self):
        self.driver.find_element(*RegistrationPage. ConButton).click()







