from selenium import webdriver
from time import sleep


def open_dash():

    driver = webdriver.Chrome()
    driver.get("http://localhost:8050/")

    # Wait until dash is opened
    for _ in range(30):
        sleep(1)
        
        if 'Updating...' not in driver.title:
            return driver 
