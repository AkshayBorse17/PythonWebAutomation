import time
from selenium import webdriver

def test_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    driver.minimize_window()
    print(driver.current_url)

    driver.get("https://app.vwo.com/")
    print(driver.current_url)
    print(driver.title)

    driver.back()
    print(driver.current_url)
    print(driver.title)

    driver.forward()
    print(driver.current_url)
    print(driver.title)

    driver.refresh()
    time.sleep(5)

