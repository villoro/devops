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

    chromepath = os.path.join(os.getcwd(), "chromedriver")

    if headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        return webdriver.Chrome(chrome_options=chrome_options, executable_path=chromepath)

    else:
        return webdriver.Chrome(executable_path=chromepath)


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
