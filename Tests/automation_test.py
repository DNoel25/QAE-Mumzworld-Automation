import logging
import pytest
from selenium.webdriver.support.expected_conditions import element_to_be_selected

from Pages.page_automation import GuestUserAutomation
from Utils.base import BaseTest
from selenium.webdriver.common.by import By
from Utils.confest import MainTestRunner


# @pytest.mark.usefixtures("setup")
class TestAutomation(BaseTest):

    @classmethod
    def setup_class(cls):
        """ Use the shared WebDriver instance """
        MainTestRunner.setup()
        cls.driver = MainTestRunner.get_driver()


    def test_verify_the_site(self):
        order_process = GuestUserAutomation(self.driver)
        # Close the popup if it appears
        order_process.test_close_popup()
        print("hehe")
        # order_process.is_element_present(elem)
        # Check if a specific element is present on the page
        # element_locator = (By.XPATH, '//*[@id="mumz_logo_img"]/svg/use')  # Replace with an actual element ID
        # assert order_process.is_element_present(), "Landing page did not load successfully!"
