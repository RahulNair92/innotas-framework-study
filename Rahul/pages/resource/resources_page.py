import utilities.custom_logger as cl
from pages.home.nav import nav_bar
import logging
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver as SD
from selenium.webdriver.common.action_chains import ActionChains


class ResourcePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = nav_bar(driver)

    #my Tests begins

    # locators

    _newResource_btn ="//div[contains(@id, 'resourcenavigationview')]//following::span[contains(text(), 'New')]"
    _resourceTab_ = "//a[@aria-label='Resources' and @href='home.pa#%5BT7%5D']"


    def fillDetails(self):
        _first_name = "//form[@name='Resources']//td//following::input[@name='firstName']"
        SD.sendKeys(data="Rahul",element=_first_name)

    def navigateResources(self):
        self.log.info("reached navigate to resource function")
        element=SD.waitForElement(locator= self._resourceTab_ , locatorType="xpath")
        self.elementClick(element=element)



    def resourceCreate(self):
        """
        Used for Resource Creation

        """
        self.log.info("#"*20)
        self.log.info("Reached def resourceCreate")
        self.navigateResources()

        #clck new btn
        element= SD.waitForElement(locatorType="xpath", locator=self._newResource_btn)
        SD.elementClick(element)

        #handle windows
        handles = self.driver.window_handles
        for item in handles:
            if "Create a new Resource" in self.driver.title():
                self.driver.switch_to(item)
                break
            else:
                self.log.info("unable to find window with this title")
        self.fillDetails()








