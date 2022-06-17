import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


@pytest.mark.title
def test_title():
    driver = webdriver.Chrome()
    driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
    assert driver.title == 'Selenium Easy - Checkbox demo for automation using selenium'


@pytest.mark.checkbox
def test_title_checkbox():
    driver = webdriver.Chrome()
    driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
    tick = driver.find_element_by_id('isAgeSelected')
    tick.click()
    assert tick.is_selected()
    textage = driver.find_element_by_id('txtAge')
    assert textage.text == 'Success - Check box is checked'

@pytest.mark.mcheckbox
def test_title_multiple_checkbox():
    driver = webdriver.Chrome()
    driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
    driver.maximize_window()
    # For first Checkbox
    option1 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label/input')
    option1.click()
    assert option1.is_selected()
    sleep(2)
    option1.click()
    assert not option1.is_selected()

    # For Second Checkbox
    option2 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label/input')
    option2.click()
    assert option2.is_selected()
    sleep(2)
    option2.click()
    assert not option2.is_selected()

    # For Third Checkbox
    option3 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input')
    option3.click()
    assert option3.is_selected()
    sleep(2)
    option3.click()
    assert not option3.is_selected()

    # For Fourth Checkbox
    option4 = driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[4]/label/input')
    option4.click()
    assert option4.is_selected()
    sleep(2)
    option4.click()
    assert not option4.is_selected()

    # CheckAll Button
    checkall = driver.find_element_by_id('check1')
    checkall.click()
    assert 'Uncheck All' == checkall.get_attribute('value')
    assert option1.is_selected()
    assert option2.is_selected()
    assert option3.is_selected()
    assert option4.is_selected()
    sleep(3)
    checkall.click()
    assert 'Check All' == checkall.get_attribute('value')
    assert not option1.is_selected()
    assert not option2.is_selected()
    assert not option3.is_selected()
    assert not option4.is_selected()
    sleep(3)
