import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEcommerceAutomation:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("mumzworld.com")  # Update with actual URL
        yield
        self.driver.quit()

    def test_close_popup(self):
        try:
            shadow_host = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#wzrkImageOnlyDiv > ct-web-popup-imageonly"))
            )
            for _ in range(3):
                try:
                    shadow_root = self.driver.execute_script("return arguments[0].shadowRoot;", shadow_host)
                    WebDriverWait(self.driver, 10).until(lambda d: shadow_root.find_element(By.ID, "close"))
                    popup_close_button = self.driver.execute_script(
                        "return document.querySelector('#wzrkImageOnlyDiv > ct-web-popup-imageonly').shadowRoot.querySelector('#close');"
                    )
                    time.sleep(2)
                    self.driver.execute_script("arguments[0].click();", popup_close_button)
                    self.driver.refresh()
                    return
                except:
                    pass
            pytest.fail("Popup could not be closed after multiple attempts.")
        except Exception as e:
            pytest.fail(f"Popup not found or could not be closed: {str(e)}")

    def test_search_product(self):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search_textbox"]'))
            )
            search_box.clear()
            search_box.send_keys("Baby Stroller")
            search_box.send_keys(Keys.ENTER)
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "ais-InfiniteHits-list"))
            )
        except Exception as e:
            pytest.fail(f"Error searching product: {str(e)}")

    def test_add_product_to_cart(self):
        try:
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ais-InfiniteHits-list"))
            )
            if not products:
                pytest.fail("No products found.")
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//button[@id='add_cart_button'])[1]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
            self.driver.execute_script("arguments[0].click();", add_to_cart_button)
            time.sleep(2)
        except Exception as e:
            pytest.fail(f"Error adding product to cart: {str(e)}")

    def test_navigate_to_cart(self):
        try:
            cart_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='cart_button' and contains(@title, 'Cart')]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", cart_btn)
            cart_btn.click()
            time.sleep(3)
        except Exception as e:
            pytest.fail(f"Error navigating to cart: {str(e)}")

    def test_update_quantity(self):
        try:
            qty = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@name='qty' and @type='number' and contains(@class, 'text-lg')]"))
            )
            qty.clear()
            qty.send_keys("5")
            time.sleep(3)
        except Exception as e:
            pytest.fail(f"Error updating quantity: {str(e)}")

    def test_proceed_to_checkout(self):
        try:
            proceed_to_checkout_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Proceed to Checkout']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", proceed_to_checkout_btn)
            proceed_to_checkout_btn.click()
            time.sleep(3)
        except Exception as e:
            pytest.fail(f"Error proceeding to checkout: {str(e)}")
