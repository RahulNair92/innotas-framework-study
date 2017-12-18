import utilities.custom_logger as cl
from pages.home.nav import nav_bar
import logging
from base.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = nav_bar(driver)

    # Locators
    _login_ = "//*[@id='login']"
    _password_ = "//*[@id='password']"
    _login_button = "//button[contains(text(), 'Log in to Innotas')]"



    def enterLogin(self, login):
        self.sendKeys(login, self._login_, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, login="", password=""):
        self.clearFields()
        self.enterLogin(login)
        self.enterPassword(password)
        self.clickLoginButton()

    def clearFields(self):
        """
        to clear fields login and password
        """
        loginField= self.getElement(locator=self._login_, locatorType="xpath")
        loginField.clear()
        passwordField = self.getElement(locator=self._password_, locatorType="xpath")
        passwordField.clear()

    def verifyLoginSuccessful(self):
        self.waitForElement(locator=nav_bar._userIcon_, locatorType="xpath")
        result = self.isElementPresent(locator=nav_bar._userIcon_,
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        self.waitForElement(locator=nav_bar._userIcon_, locatorType="xpath")
        result = self.isElementPresent(locator=nav_bar._userIcon_,
                                       locatorType="xpath")
        return result



############refined up to this point####################################################################
    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        # self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//*[@id='splitbutton-1069-btnWrap']/following::span[1]",
                          locatorType="xpath", pollFrequency=1)
        action1= ActionChains(self.driver)
        # action1.send_keys_to_element(logoutLinkElement, Keys.ARROW_DOWN).perform()
        action1.move_to_element(logoutLinkElement).click(logoutLinkElement).perform()
        logout= self.getElement(locator="//*[@id='menuitem-1075-textEl' and contains(text(),'Logout')]", locatorType="xpath")
        logout.click()
        self.log.info("logout from application")
