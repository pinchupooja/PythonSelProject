from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href = '/angularpractice/shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    checkBox = (By.ID, "exampleCheck1")
    genderDropdown = (By.CSS_SELECTOR, "select#exampleFormControlSelect1")
    email = (By.NAME, "email")
    submitButton = (By.XPATH, "//input[@type = 'submit']")
    successMessage = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()  # * is used to treat this as tuple
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def selectHomePageCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def selectGender(self):
        return self.driver.find_element(*HomePage.genderDropdown)

    def sendEmail(self):
        return self.driver.find_element(*HomePage.email)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submitButton)

    def verifySuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
