import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class TestLogin:

    @pytest.fixture
    def driver(self):
       options=webdriver.ChromeOptions()
       options.add_argument("--start-maximized")
       driver = webdriver.Chrome(options)
       return driver


    def test_login_passed(self,driver):
        driver.get("https://katalon-demo-cura.herokuapp.com/")

        #exact full match
        mkapp=driver.find_element(By.XPATH,"//a[text()='Make Appointment']")

        #partial macth
        # mkapp=driver.find_element(By.XPATH,"//a[contains(text(),'Make')]")

        # mkapp = driver.find_element(By.XPATH, "//a[contains(@id,'btn-make-appointment')]")

        # mkapp = driver.find_element(By.XPATH, "//a[end-with(text(),'Make Appointment')]")

        # mkapp = driver.find_element(By.XPATH, "//a[starts-with(text(),'Make')]")

        mkapp.click()

        assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
        time.sleep(5)




