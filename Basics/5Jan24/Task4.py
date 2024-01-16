import time

import pytest

import os

import logging

from dotenv import load_dotenv

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

driver = webdriver.Chrome()

LOGGER = logging.info(__name__)


def waitForElement(waitInSeconds):
    wait = WebDriverWait(driver, waitInSeconds)

    return wait


def test_deviceNameListTest():
    driver.get(
        "https://www.flipkart.com/mobiles/google~brand/pr?sid=tyy,4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Google+Mobiles")

    # time.sleep(10)

    waitForElement(15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_4rR01T")))

    devicesList = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")

    for device in devicesList:
        # if device == ""

        print(device.text)

    driver.quit()