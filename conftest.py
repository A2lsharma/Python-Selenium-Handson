import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

@pytest.fixture
def radio_buttons():
    driver = webdriver.Chrome()
    driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
    check_value_button = driver.find_element_by_id('buttoncheck')
    radiobutton_text = driver.find_element_by_class_name('radiobutton')
    male = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input')
    female = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]/input')