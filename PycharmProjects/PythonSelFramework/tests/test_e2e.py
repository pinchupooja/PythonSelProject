from pageObjects.HomePage import HomePage
from utelities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == 'Blackberry':
                checkOutPage.getCardFooter()[i].click()

        confirmPage = checkOutPage.clickOnPrimaryButton()
        confirmPage.clickSuccessButton().click()
        log.info("Entering country name India")
        confirmPage.sendCountryName().send_keys("ind")
        self.verifyLinkPresnce("India")
        confirmPage.selectCountryName().click()
        confirmPage.selectCheckboxOption().click()
        confirmPage.finalSubmitButton().click()
        successText = confirmPage.successPaymentText().text
        log.info("Text received from application is "+successText)
        assert 'Success' in successText
        #to verify text
