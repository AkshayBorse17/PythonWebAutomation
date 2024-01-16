import time
from selenium import webdriver

def test_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    driver.maximize_window()
    driver.minimize_window()
    print(driver.current_url)
    print(driver.title)
    print(driver.page_source)
    time.sleep(5)

    # driver.close()
    # time.sleep(100)

    driver.quit()
    time.sleep(100)





