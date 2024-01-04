import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    print(driver.title)

    username=driver.find_element(By.ID,"login-username")
    username.send_keys("contact+atb5x@thetestingacademy.com")

    password=driver.find_element(By.ID,"login-password")
    password.send_keys("ATBx@1234")

    submit=driver.find_element(By.ID,"js-login-btn")
    submit.click()

    time.sleep(20)