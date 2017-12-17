
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
class nav_bar(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _resourceTab_="//a[@aria-label='Resources']"
    _projectTab_= "//a[@aria-label='Projects:']"
    _userIcon_="//img[contains(@alt,'Admin testing User')]"

    #functions to navigate to common grids in nav bar
    def navigateToResources(self):
        self.elementClick(locator=self._resourceTab_, locatorType="xpath")

    def navigateToResources(self):
        self.elementClick(locator=self._projectTab_, locatorType="xpath")

