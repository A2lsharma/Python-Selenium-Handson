from selenium import webdriver
import time
import pytest
print('Test Cases Started Successfully')

@pytest.mark.title
def test_title():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="at-cv-lightbox-button-holder"]/a[2]').click()
    assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' == driver.title
    driver.close()

@pytest.mark.usermessage
def test_usermessage():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="at-cv-lightbox-button-holder"]/a[2]').click()
    usermessage = driver.find_element_by_id('user-message')
    usermessage.clear()
    usermessage.send_keys('Hi')
    get_input = driver.find_element_by_xpath('//*[@id="get-input"]/button')
    get_input.click()
    c = driver.find_element_by_xpath('//*[@id="display"]')
    assert 'Hi' == c.text
    driver.close()

@pytest.mark.usermessage
def  test_two_input_fields():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="at-cv-lightbox-button-holder"]/a[2]').click()
    first_number = driver.find_element_by_id('sum1')
    first_number.clear()
    first_number.send_keys('5')
    second_number = driver.find_element_by_id('sum2')
    second_number.clear()
    second_number.send_keys('10')
    driver.find_element_by_xpath('//*[@id="gettotal"]/button').click()
    c = driver.find_element_by_xpath('//*[@id="displayvalue"]')
    assert '15' == c.text
    driver.close()




