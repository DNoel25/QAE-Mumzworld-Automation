import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure logging
logging.basicConfig(level=logging.INFO)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        try:
            # Locate and fill the username field
            username_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "id_username"))
            )
            username_field.clear()
            username_field.send_keys(username)

            # Locate and fill the password field
            password_field = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.ID, "id_password"))
            )
            password_field.clear()
            password_field.send_keys(password)

            # Locate and click the submit button
            login_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
            )
            login_button.click()

            # Check for success by looking for the expected <h2> tag on the dashboard
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.TAG_NAME, "h2"))
                )
                h2_element = self.driver.find_element(By.TAG_NAME, "h2")
                if h2_element.text == "Dashboard":  # Replace with the actual expected text
                    print("Login successful, Dashboard loaded")
                else:
                    print(f"Login failed, unexpected h2 text: {h2_element.text}")
            except Exception as e:
                print(f"Failed to find the h2 tag: {e}")

        except Exception as e:
            print(f"Exception occurred during login: {e}")

        except Exception as e:
            print(f"Exception occurred: {e}")