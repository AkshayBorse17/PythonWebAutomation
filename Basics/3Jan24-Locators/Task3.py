import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_positive():
    options=webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver=webdriver.Chrome(options)
    driver.get("https://app.vwo.com/")
    # driver.maximize_window()
    print(driver.title)

    username=driver.find_element(By.ID,"login-username")
    username.send_keys("contact+atb5x@thetestingacademy.com")

    password=driver.find_element(By.ID,"login-password")
    password.send_keys("ATBx@1234")

    submit=driver.find_element(By.ID,"js-login-btn")
    submit.click()

    element = driver.find_element(By.XPATH, '//p[@data-qa = "page-sub-title"]/span')
    assert element.is_displayed(), 'Welcome message is not displayed'

    # msgg = driver.find_element(By.CLASS_NAME, "//span[@class='Fw(semi-bold).ng-binding']")

    time.sleep(10)

