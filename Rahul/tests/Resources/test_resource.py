from pages.resource.resources_page import ResourcePage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class newResourceTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.rp = ResourcePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_newResource(self):
        self.log.info("#"*20)
        self.log.info("testcase for new Resources started")
        self.log.info("#" * 20)
        self.rp.resourceCreate(self)
