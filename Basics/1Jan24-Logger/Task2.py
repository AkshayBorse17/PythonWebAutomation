import logging
from selenium import webdriver
def test_login():

    driver=webdriver.Chrome()
    driver.get("https://google.com")

    logger = logging.getLogger(__name__)
    logger.info(driver.title)
    logger.error(driver.title)