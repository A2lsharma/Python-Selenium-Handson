import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# common constants
url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'

# Select List Demo Constants
dropdown = 'select-demo'  # Search by ID
result_link = 'selected-value'  # Search by Class

# Multi Select List Demo
first_selected_button_link = 'printMe'  # Search by ID
get_all_button_link= 'printAll'  # Search by ID
result_link_multple = 'getall-selected'  # Search by Class


@pytest.mark.singleselect
def test_select_list():
    driver = webdriver.Chrome()
    driver.get(url)
    options = driver.find_element_by_id(dropdown)
    options.click()
    sunday = driver.find_element_by_xpath('//*[@id="select-demo"]/option[2]')
    sunday.click()
    message = driver.find_element_by_class_name(result_link)
    assert 'Day selected :- Sunday' == message.text
    driver.close()


@pytest.mark.multipleselect
def test_multi_select_noselect():
    driver = webdriver.Chrome()
    driver.get(url)
    first_selected_button = driver.find_element_by_id(first_selected_button_link)
    first_selected_button.click()
    message = driver.find_element_by_class_name(result_link_multple)
    assert 'First selected option is : undefined' == message.text

@pytest.mark.multipleselect
def test_multi_select_singleselect() :
    driver = webdriver.Chrome()
    driver.get(url)
    first_selected_button = driver.find_element_by_id(first_selected_button_link)
    pennsylvania = driver.find_element_by_xpath('//*[@id="multi-select"]/option[7]')
    pennsylvania.click()
    first_selected_button.click()
    message = driver.find_element_by_class_name(result_link_multple)
    assert 'First selected option is : Pennsylvania' == message.text

@pytest.mark.multipleselect
def test_multi_select_multipleselect() :
    driver = webdriver.Chrome()
    driver.get(url)
    get_all_button = driver.find_element_by_id(get_all_button_link)
    ohio = driver.find_element_by_xpath('//*[@id="multi-select"]/option[5]')
    pennsylvania = driver.find_element_by_xpath('//*[@id="multi-select"]/option[7]')
    ActionChains(driver).key_down(Keys.CONTROL).click(ohio).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(pennsylvania).key_up(Keys.CONTROL).perform()
    get_all_button.click()