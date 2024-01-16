import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from Task3 import driver
# from Task1 import driver

class TestLogin:

    @pytest.fixture(scope='None')
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options)
        return driver

    @pytest.mark.negative
    def test_login_negative(self,driver):
        # drivers=TestLoginN.drivers(self)
        driver.get("https://app.vwo.com/")
        # driver.maximize_window()

        username = driver.find_element(By.ID, "login-username")
        username.send_keys("admin")

        password = driver.find_element(By.ID, "login-password")
        password.send_keys("admin")

        submit = driver.find_element(By.ID, "js-login-btn")
        submit.click()

        time.sleep(5)

        msg = driver.find_element(By.ID, "js-notification-box-msg")

        assert msg.text == "Your email, password, IP address or location did not match", "TC1 failed"
        # time.sleep(5)
        print(msg.text)



    @pytest.mark.Positive
    def test_login_positive(self,driver):

        driver.get("https://app.vwo.com/")
        # driver.maximize_window()
        print(driver.title)

        username = driver.find_element(By.ID, "login-username")
        username.send_keys("contact+atb5x@thetestingacademy.com")

        password = driver.find_element(By.ID, "login-password")
        password.send_keys("ATBx@1234")

        submit = driver.find_element(By.ID, "js-login-btn")
        submit.click()

        time.sleep(10)
        msg = driver.find_element(By.XPATH, "//p[@data-qa = 'page-sub-title']")
        assert msg.text=="Hi Aman, here's an overview of your experience optimization journey","TC2 failed"
        print(msg.text)
