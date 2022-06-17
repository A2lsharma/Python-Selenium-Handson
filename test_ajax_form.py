from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest

#   Constants
url = 'https://www.seleniumeasy.com/test/ajax-form-submit-demo.html'
name_link = 'title'  # search by name
description_link = 'textarea' # search by name
button_link = 'btn-submit' # search by name
message_link = '//*[@id="submit-control"]'

@pytest.mark.ajax
def test_ajax_form():
    driver = webdriver.Chrome()
    driver.get(url)
    name = driver.find_element_by_name(name_link)
    name.clear()
    name.send_keys('Test_Name')
    description = driver.find_element_by_tag_name(description_link)
    description.clear()
    description.send_keys('Description')
    button = driver.find_element_by_name(button_link)
    button.click()
    message = driver.find_element_by_xpath(message_link)
    assert 'Ajax Request is Processing!' == message.text
    sleep(5)
    assert 'Form submited Successfully!' == message.text
