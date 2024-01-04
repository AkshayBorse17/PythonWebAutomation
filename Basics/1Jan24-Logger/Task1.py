import logging
from selenium import webdriver
def test_login():
    logger=logging.getLogger(__name__)
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")