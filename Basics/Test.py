import time

from selenium import webdriver

def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options)

    driver.get("https://www.cricbuzz.com/")

    driver.maximize_window()
    print(driver.title)