import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utelities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        #log.info("First name is "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.sendEmail().send_keys(getData["lastname"])
        homePage.selectHomePageCheckBox().click()
        self.selectOptionByText(homePage.selectGender(), getData["gender"])
        homePage.submitForm().click()
        alertText = homePage.verifySuccessMessage().text
        assert "success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param