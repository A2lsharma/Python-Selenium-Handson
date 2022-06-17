import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# constants
url = 'https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html'


# @pytest.mark.jquery
def test_search_box():
    driver = webdriver.Chrome()
    driver.get(url)
    select_country = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[2]/span/span[1]/span')
    select_country.click()
    select_country_text = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    select_country_text.clear()
    select_country_text.send_keys('Australia')
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    select_country.click()
    select_country_text.clear()
    india = driver.find_element_by_xpath('//*[@id="country"]/option[6]')
    india.click()


# @pytest.mark.jquery
def test_multi_select():
    driver = webdriver.Chrome()
    driver.get(url)
    select_state = driver.find/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li/input_element_by_xpath(
        '')
    select_state.click()
    select_state_text = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li/input')
    select_state_text.clear()
    select_state_text.send_keys('California')
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    select_state_text.send_keys('nor')
    ActionChains(driver).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_up(
        Keys.ARROW_UP).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(3)
    north_dakota = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li[2]')
    assert '×North Dakota' == north_dakota.text
    north_dakota_cancel = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/span/span[1]/span/ul/li[2]/span')
    north_dakota_cancel.click()
    sleep(3)
    select_state_text.send_keys('nor')
    ActionChains(driver).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_up(
        Keys.ARROW_UP).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    select_state.click()
    ga = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/select/option[11]')
    ga.click()
    sleep(3)


# @pytest.mark.jquery
def test_disabled():
    driver = webdriver.Chrome()
    driver.get(url)
    dropdown = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/span')
    dropdown.click()
    dropdown_text = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
    dropdown_text.clear()
    dropdown_text.send_keys('American Samoa')
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    dropdown.click()
    dropdown_text.send_keys('Guam')
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


@pytest.mark.jquery
def test_category():
    driver = webdriver.Chrome()
    driver.get(url)
    dropdown = driver.find_element_by_id('files')
    dropdown.click()
    php = driver.find_element_by_xpath('//*[@id="files"]/optgroup[1]/option[2]')
    php.click()
    assert 'PHP' == php.text
