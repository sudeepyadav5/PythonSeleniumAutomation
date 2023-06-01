from traceback import print_stack
from allure.constants import AttachmentType
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import SeleniumFrameWork.utilities.CustomLogger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import allure


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web Page Launched with URL : " + url)
        except:
            self.log.info("Web Page Not Launched with URL : " + url)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type :" + locatorType + "entered is not found")
            return False

    def getElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info(
                "Element Found with Locator Type:" + locatorByType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Element Not Found with Locator Type: " + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()
        return webElement

    def waitForElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # webElement = self.driver.find_element(locatorByType, locatorValue)
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(
                "Element Found with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Element Not Found with Locator Type: " + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()
            self.takeScreenshot(locatorType)

        return webElement

    def clickOnElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info(
                "Click on WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Unable Click WebElement with Locator Type: " + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()

    def sendText(self, text, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info(
                "Send the text " + text + " in WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Unable to Send the text " + text + " in WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()
            self.takeScreenshot(locatorType)


    def getText(self, locatorValue, locatorType="id"):
        elementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementText = webElement.text
            self.log.info(
                "Got the text " + elementText + " from WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Unable to Send the text " + elementText + " in WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()

        return elementText


    def isElementDisplayed(self, locatorValue, locatorType="id"):
        elementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            elementDisplayed = webElement.text
            self.log.info(
                "WebElement is Displayed on web page with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "WebElement is not Displayed on web page with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()

        return elementDisplayed

    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                "Scroll to WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
        except:
            self.log.info(
                "Unable to scroll to WebElement with Locator Type:" + locatorType + " and with Locator Value :" + locatorValue)
            print_stack()

    # def takeScreenshot(self, text):
    #     allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
