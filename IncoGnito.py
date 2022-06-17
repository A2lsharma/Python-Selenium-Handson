from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep

@pytest.mark.browser
def test_incognito():
    driver = webdriver.Chrome()
    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys("n").key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()
    sleep(3)
    driver.get("https://www.google.com")
    sleep(3)
    driver.close()
