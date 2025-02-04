import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuestUserAutomation:
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
                    return  # Exit function if click is successful

                except Exception as inner_e:
                    print(f"Retrying due to stale element: {str(inner_e)}")

            pytest.fail("Popup could not be closed after multiple attempts.")

        except Exception as e:
            pytest.fail(f"Popup not found or could not be closed: {str(e)}")

    def is_element_present(self):
        try:
            WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="mumz_logo_img"]/svg/use'))
            )
            return True
        except Exception as e:
            print(f"Error finding element: {e}")
            return False
