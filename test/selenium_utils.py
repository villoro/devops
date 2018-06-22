from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def get_chrome_webdriver(headless):
    """
        Get a chrome webdriver.

        Args:
            headless:	bool to allow headless mode

        Returns:		chrome web driver
    """

    if headless:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox") #This make Chromium reachable
        options.add_argument("--no-default-browser-check") #Overrides default choices
        options.add_argument("--no-first-run")
        options.add_argument("--disable-default-apps") 
        options.add_argument("--window-size=1920x1080")

        return webdriver.Chrome('/home/travis/virtualenv/python3.6/chromedriver', chrome_options=options)

    else:
        return webdriver.Chrome('/home/travis/virtualenv/python3.6/chromedriver')


def open_dash(headless=True):
    """
        Starts a chrome web driver and opens the dash app. Then it waits until the app is loaded

        Args:
            headless:	bool to allow headless mode

        Returns:		chrome web driver
    """

    driver = get_chrome_webdriver(headless)

    # Open dash app
    driver.get("http://localhost:8050/")

    # Wait until dash is opened
    for _ in range(30):
        sleep(1)
        
        if 'Updating...' not in driver.title:
            return driver 
