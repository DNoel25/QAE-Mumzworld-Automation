from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

class BaseTest:
    driver = None

    @classmethod
    def setup_class(cls):
        driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (2)\chromedriver-win64\chromedriver.exe"
        service = Service(driver_path)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://demoapi2.recomdo.ai/client-admin")
        cls.driver.maximize_window()
