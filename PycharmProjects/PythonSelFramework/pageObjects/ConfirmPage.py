from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    successButton = (By.XPATH, "//button[contains(@class, 'btn-success')]")
    countryName = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    selectCheckbox = (By.XPATH, "//div[contains(@class, 'checkbox-primary')]")
    finalSubmit = (By.CSS_SELECTOR, "input[type ='submit']")
    successPayment = (By.XPATH, "//div[contains(@class,'alert-dismissible')]")

    def clickSuccessButton(self):
        return self.driver.find_element(*ConfirmPage.successButton)

    def sendCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def selectCountryName(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def selectCheckboxOption(self):
        return self.driver.find_element(*ConfirmPage.selectCheckbox)

    def finalSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.finalSubmit)

    def successPaymentText(self):
        return self.driver.find_element(*ConfirmPage.successPayment)