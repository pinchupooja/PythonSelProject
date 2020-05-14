from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    primaryButton = (By.XPATH, "//a[contains(@class, 'btn-primary')]")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def clickOnPrimaryButton(self):
        self.driver.find_element(*CheckOutPage.primaryButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage