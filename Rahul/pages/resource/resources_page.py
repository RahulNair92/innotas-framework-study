import utilities.custom_logger as cl
from pages.home.nav import nav_bar
import logging
from base.basepage import BasePage
from tests.Resources.resource_csv_data import resourceData as RD
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

    _newResource_btn ="//div[contains(@id,'resourcenavigationview')]//following::span[contains(text(),'New')]"
    _resourceTab_ = "//a[@aria-label='Resources' and @href='home.pa#%5BT7%5D']"
    _newResourcepageTitle_="Create a new Resource"


    def fillDetails(self):
        _first_name = "//form[@name='Resources']//td//following::input[@name='firstName']"
        fname= self.getElement(locator=_first_name,locatorType="xpath")
        self.sendKeys(data="Rahul",element=fname)

    def navigateResources(self):
        self.log.info("reached navigate to resource function")
        element= self.waitForElement(locator= self._resourceTab_ , locatorType="xpath")
        self.elementClick(element=element)



    def resourceCreate(self):
        """
        Used for Resource Creation

        """
        self.log.info("#"*20)
        self.log.info("Reached def resourceCreate")
        self.navigateResources()

        #clck new btn
        element= self.waitForElement(locatorType="xpath", locator=self._newResource_btn, timeout=20)
        list= self.driver.find_elements_by_xpath("//div[contains(@id,'resourcenavigationview')]//following::span[contains(text(),'New')]")
        length= str(len(list))
        self.log.info("no of elements found with new button xpath " + length)
        self.clickButton(element)
        self.driver.implicitly_wait(5)

        #handle windows
        handles = self.driver.window_handles
        self.log.info("window handles " + handles[0] + " " + handles[1])

        for item in handles:
            if self._newResourcepageTitle_ in self.driver.title :
                self.log.info("Found window with this title")
                self.log.infp(str(item))
                break
            else:
                self.log.info("unable to find window with this title " + self.driver.title)
            self.driver.switch_to_window(item)

        RD.test_enterdata()









