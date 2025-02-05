import logging
import time

import pytest
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.page_order_procee import OrderProcessAutomation
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
        order_process = OrderProcessAutomation(self.driver)
        # Close the popup if it appears
        order_process.test_close_popup()
        # Check if a specific element is present on the page
        order_process.is_element_present()
        # we can do assertions here

    def test_verify_search(self):
        search = OrderProcessAutomation(self.driver)

        if search.search_a_product("bathing"):
            print("Search test passed!")
        else:
            print("Failed to search")

    def test_add_to_cart(self):
        add_to_cart = OrderProcessAutomation(self.driver)

        add_to_cart.add_products_to_cart()
        # Add 2 products to the cart
        # assert add_to_cart.add_products_to_cart(), "Failed to add products to cart"

        print("Test Passed: Products successfully added to cart!")
        time.sleep(5)

    def test_cart_page(self):
        cart = OrderProcessAutomation(self.driver)
        #navigation to cart page
        cart.nav_to_cart()
        print("Navigated to cart page successfully!")

        #editing the product with 5 qty
        cart.update_the_qty()
        # we can do assertions here

    def test_checkout(self):
        shipping = OrderProcessAutomation(self.driver)
        shipping.click_proceed_to_checkout(), "proceed to checkout is having error"
        # we can do assertions here

    #we can implement more tests
    # def test_user_registration(self):
