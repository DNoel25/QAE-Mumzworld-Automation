from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


class MainTestRunner:
    driver = None

    @classmethod
    def setup(cls):
        """ Initialize WebDriver and login once """
        if cls.driver is None:
            #Please change the driver path as your chromedriver's file locations
            driver_path = r"C:\Users\SINGER\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            service = Service(driver_path)
            cls.driver = webdriver.Chrome(service=service)
            cls.driver.get("https://mumzworld.com/")
            cls.driver.maximize_window()


    @classmethod
    def teardown(cls):
        """ Quit WebDriver after all tests """
        if cls.driver:
            cls.driver.quit()
            print("Browser closed.")

    @classmethod
    def get_driver(cls):
        """ Return the active WebDriver instance """
        return cls.driver