import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    options=webdriver.ChromeOptions()
    # run by default maximize
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach",True)

    driver=webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_app=driver.find_element(By.ID,"btn-make-appointment")
    make_app.click()
    print(driver.current_url)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username=driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")

    password=driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")

    Login=driver.find_element(By.ID,"btn-login")
    Login.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(50)

    print(driver.current_url)

