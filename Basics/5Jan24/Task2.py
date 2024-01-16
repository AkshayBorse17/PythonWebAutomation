import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Task1 import driver


class TestLogin:

    def test_login_passed(self,driver):
        driver.get("https://app.vwo.com/")
        element = driver.find_element(By.ID, 'login-username')
        element.clear()
        element.send_keys('contact+atb5x@thetestingacademy.com')
        element = driver.find_element(By.ID, 'login-password')
        element.clear()
        element.send_keys('ATBx@1234')
        element = driver.find_element(By.ID, 'js-login-btn')
        element.click()
        time.sleep(10)
        element = driver.find_element(By.XPATH, '//p[@data-qa = "page-sub-title"]')
        assert element.is_displayed(), 'Welcome message is not displayed'
        print(element.text)