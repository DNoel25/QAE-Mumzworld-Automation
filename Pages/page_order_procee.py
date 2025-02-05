import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderProcessAutomation:
    def __init__(self, driver):
        self.driver = driver

    def test_close_popup(self):
        try:
            # wait for shadow host
            shadow_host = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#wzrkImageOnlyDiv > ct-web-popup-imageonly"))
            )
            # Continuously retry getting the shadow DOM element (to prevent stale reference)
                # The element is removed/reloaded from the DOM before Selenium interacts with it.
                # The element is inside an iframe (and Selenium is not switched to it).
                # The Shadow DOM is being dynamically modified, and a previously found element is no longer valid.
            for _ in range(3):
                try:
                    # Get the shadow root using JavaScript
                    shadow_root = self.driver.execute_script("return arguments[0].shadowRoot;", shadow_host)

                    # Wait for the close button inside the shadow DOM
                    WebDriverWait(self.driver, 10).until(lambda d: shadow_root.find_element(By.ID, "close"))

                    # Locate the close button again to avoid stale reference
                    popup_close_button = self.driver.execute_script(
                        "return document.querySelector('#wzrkImageOnlyDiv > ct-web-popup-imageonly').shadowRoot.querySelector('#close');"
                    )
                    time.sleep(5)
                    # Click the close button using JavaScript
                    self.driver.execute_script("arguments[0].click();", popup_close_button)

                    print("Popup closed successfully!")
                    self.driver.refresh()
                    return  # Exit function if click is successful

                except Exception as inner_e:
                    print(f"Retrying due to stale element: {str(inner_e)}")

            pytest.fail("Popup could not be closed after multiple attempts.")

        except Exception as e:
            pytest.fail(f"Popup not found or could not be closed: {str(e)}")
            return True

    def is_element_present(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@id='mumz_logo_img']"))
            )
            print("successfully there the home page loaded with logo")
            return True
        except Exception as e:
            print(f"Error finding element: {e}")
            return False

    def search_a_product(self, phrase):
        try:
            #Wait for the search input box to be visible
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="search_textbox"]'))
            )

            # Clear any existing text and enter the product name
            search_box.clear()
            search_box.send_keys(phrase)
            search_box.send_keys(Keys.ENTER)  # Press Enter key to search

            # # Wait for search results to load
            # WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'search-results')]"))
            # )

            print(f"Search for '{phrase}' executed successfully.")
            time.sleep(5)
            # Locate all search result products
            products = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "ais-InfiniteHits-list"))
            )

            print(f"Type of 'products': {type(products)}")  # Debugging line
            return True

        except TimeoutException as e:
            print(f"Error to finding the search element")
            return False
        except Exception as e:
            print(f"Error is : {e}")

    def add_products_to_cart(self):
        """Click the 'Add to Cart' button for the first product in search results."""
        try:
            # Wait for search result products to be present
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ais-InfiniteHits-list"))
            )

            if not products:
                print("No products found on the search results page!")
                return False
            first_product = products[0]  # Get the first product
            print("Found first product:", first_product.text)  # Debugging

            # Locate and click the "Add to Cart" button inside the first product
            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//button[@id='add_cart_button'])[1]"))
            )

            # Scroll into view to ensure it's clickable
            self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)

            # Click the button using JavaScript (in case of overlay issues)
            self.driver.execute_script("arguments[0].click();", add_to_cart_button)

            print("Product added to cart successfully!")
            time.sleep(2)
            return True

        except Exception as e:
            print(f"Error adding product to cart: {e}")
            return False

    def nav_to_cart(self):
        try:
            cart_btn = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='cart_button' and contains(@title, 'Cart')]"))
            )
            # Scroll into view to ensure it's clickable
            self.driver.execute_script("arguments[0].scrollIntoView();", cart_btn)
            cart_btn.click()
            time.sleep(4)
        except Exception as e:
            print(f"Error in redirecting to cart page")
            return False

    def update_the_qty(self):
        try:
            qty = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='qty' and @type='number' and contains(@class, 'text-lg')]"))
            )
            # Scroll into view to ensure it's clickable
            # self.driver.execute_script("arguments[0].scrollIntoView();", cart_btn)
            qty.clear()
            qty.send_keys("5")
            time.sleep(6)
        except Exception as e:
            print(f"Error in updating the qty")
            return False

    def click_proceed_to_checkout(self):
        try:
            proceed_to_Checout_btn = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Proceed to Checkout']   "))
            )
            # Scroll into view to ensure it's clickable
            self.driver.execute_script("arguments[0].scrollIntoView();", proceed_to_Checout_btn)
            proceed_to_Checout_btn.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error in updating the qty")
            return False

    # def fill_all_required_field_