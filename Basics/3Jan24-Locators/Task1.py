import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# <a id="btn-make-appointment"
# href="./profile.php#login"
# class="btn btn-dark btn-lg">Make Appointment</a>

def test_login():

    # options=webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #by id :
    # button=driver.find_element(By.ID,"btn-make-appointment")
    # button.click()
    # print(driver.current_url)

    # #partial link text :
    # button=driver.find_element(By.PARTIAL_LINK_TEXT,"App")
    # button.click()
    # print(driver.current_url)

    #full link text :
    # button=driver.find_element(By.LINK_TEXT,"Make Appointment")
    # button.click()
    # print(driver.current_url)

    # By class name :
    button=driver.find_elements(By.CLASS_NAME,"btn.btn-dark.btn-lg")
    button[1].click()
    print(driver.current_url)
    # time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login","Error!! wrong URL"
