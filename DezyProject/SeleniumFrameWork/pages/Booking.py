import time
from SeleniumFrameWork.base.BasePage import BaseClass
import SeleniumFrameWork.utilities.CustomLogger as cl


class BookingPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locator Value in Booking Page

    _clinicsLink = "//div[@class='mx-4 text-white md:mx-6'][3]"  # xpath
    _rootcanalLink = '//*[@id="test-service-item-0"]/div/div/span/img'  # xpath

    def clickClinicsLink(self):
        self.clickOnElement(self._clinicsLink, "xpath")

    def clickOnRootCanalLink(self):
        self.scrollTo(self._rootcanalLink, "xpath")
        self.clickOnElement(self._rootcanalLink, "xpath")

