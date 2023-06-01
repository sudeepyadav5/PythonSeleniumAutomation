from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import SeleniumFrameWork.utilities.CustomLogger as cl


class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            service_obj = Service("C:/Users/3Embed/Python_Ast/WebDriver/chromedriver")
            driver = webdriver.Chrome(service=service_obj)
            self.log.info("Chrome Driver is Initializing")

        elif browserName == "firefox":
            service_obj = Service("C:/Users/3Embed/Python_Ast/WebDriver/geckodriver")
            driver = webdriver.Firefox(service=service_obj)
            self.log.info("Firefox Driver is Initializing")

        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is Initializing")

        return driver
