import unittest
import webbrowser

import pytest
import time
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.pages.Booking import BookingPage
import SeleniumFrameWork.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class BookingPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.bps = BookingPage(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_bookingPage(self):
        self.bps.clickClinicsLink()
        time.sleep(2)
        self.bps.clickOnRootCanalLink()




