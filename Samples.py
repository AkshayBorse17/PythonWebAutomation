import time
from selenium import webdriver

def test_login():
    options=webdriver.ChromeOptions()

    #Run browser continously without time.sleep
    options.add_experimental_option("detach",True)

    #Run silent without browser
    # options.add_argument("--headless")

    #run by default maximize
    options.add_argument("--start-maximized")

    #javascript exccuter
    # driver.execute_script("arguments[0].click();", element)

    #add extension
    path1="C:/Users/aksha/OneDrive/Desktop/PythonWebAutomation/CRX/EditThisCookie.crx"
    path2 ="C:/Users/aksha/OneDrive/Desktop/PythonWebAutomation/CRX/Selenium-IDE.crx"
    options.add_extension(path1)
    options.add_extension(path2)

    driver=webdriver.Chrome(options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.current_url)

    driver.get("https://app.vwo.com/")
    print(driver.current_url)

    driver.back()
    print(driver.current_url)

    driver.forward()
    print(driver.current_url)

    driver.refresh()


