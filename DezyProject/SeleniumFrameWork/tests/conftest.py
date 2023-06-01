import pytest
from SeleniumFrameWork.base.BasePage import BaseClass
from SeleniumFrameWork.base.DriverClass import WebDriverClass
import time


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print("Before Class")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    driver.maximize_window()
    bp = BaseClass(driver)
    bp.launchWebPage("https://www.dezy.com/in", "Best Dental Clinic & Dentist near me, Nearest Dental Clinic - Dezy")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(15)
    driver.minimize_window()
    driver.quit()
    print("After Class")


@pytest.yield_fixture()
def beforeMethod():
    print("Before Method")
    yield
    print("After Method")
