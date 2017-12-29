from pages.resource import resources_page
from pages.home.nav import nav_bar
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from base.basepage import BasePage
import time

@ddt
class resourceData(BasePage):

    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_enterdata(self, fname, lname, unit, tsAp, exAp, pRole):

        _first_name = "//form[@name='Resources']//td//following::input[@name='firstName']"
        fname_element= self.getElement(locator=_first_name,locatorType="xpath")
        self.sendKeys(data=fname, element=fname_element )
