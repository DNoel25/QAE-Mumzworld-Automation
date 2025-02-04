import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuestUserAutomation:
    def __init__(self, driver):
        self.driver = driver

    def test_close_popup(self):
        try:
            # Wait for the parent div of the popup to be visible
            popup_div = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "wzrkImageOnlyDiv"))
            )
            print(popup_div.is_displayed())
            # Find the close button inside the popup (update selector based on your HTML)
            close_button = popup_div.find_element(By.CLASS_NAME, "close-button")  # Update with actual class

            # Click the close button
            close_button.click()

            # Verify the popup is closed
            assert len(self.driver.find_elements(By.ID, "wzrkImageOnlyDiv")) == 0

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
