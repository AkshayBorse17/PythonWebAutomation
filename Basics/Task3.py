import time
from selenium import webdriver

def test_login():
    options = webdriver.ChromeOptions()

    # Run browser continously without time.sleep
    options.add_experimental_option("detach", True)

    # Run silent without browser
    options.add_argument("--headless")

    # add extension
    # path = "C:/Users/aksha/OneDrive/Desktop/PythonWebAutomation/EditThisCookie.crx"
    # options.add_extension(path)

    driver=webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    print(driver.current_url)

    driver.get("https://app.vwo.com/")
    print(driver.current_url)

    driver.back()
    print(driver.current_url)

    driver.forward()
    print(driver.current_url)

    driver.refresh()


