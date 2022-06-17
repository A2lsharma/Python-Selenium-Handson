import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#common constants
url = 'https://www.seleniumeasy.com/test/basic-radiobutton-demo.html'  # url

# Constants used in singleradio mark
buttoncheck = 'buttoncheck'  # using id
radiobutton = 'radiobutton'  # using class
male_link = '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input'  # using xpath
female_link = '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]/input'  # using xpath
button_text = 'Get Checked value'  # text on button
only_click = 'Radio button is Not checked'  # text displayed after first click
male_click = "Radio button 'Male' is checked"  # text displayed after male click
female_click = "Radio button 'Female' is checked"  # text displayed after male click

# constants used in multipleradio mark
get_values_button = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button' # Address of button
button2_text_link = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]' # Link of generated after button click
button2_text = 'Get values' # Text displayed on button
button2_text_generated = 'Sex :\nAge group:' # text generated after no radio selected
male2_link = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[1]'
fenale2_link = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[2]'
Age_0_5 = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[1]'
Age_5_15 = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[2]'
Age_15_50 = '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[3]'

# Test Cases for Single Button Radio
@pytest.mark.singleradio
def test_check_value_button_displayed():
    driver = webdriver.Chrome()
    driver.get(url)
    check_value_button = driver.find_element_by_id(buttoncheck)
    assert check_value_button.is_displayed()  # Check whether button is displayed or not
    driver.close()


@pytest.mark.singleradio
def test_check_value_button_text():
    driver = webdriver.Chrome()
    driver.get(url)
    check_value_button = driver.find_element_by_id(buttoncheck)
    assert button_text == check_value_button.text  # Check whether button text displayed is correct or not
    driver.close()


@pytest.mark.singleradio
def test_check_value_click_display_general():  # Radio Buttons Assertions
    driver = webdriver.Chrome()
    driver.get(url)
    check_value_button = driver.find_element_by_id(buttoncheck)
    check_value_button.click()
    radiobutton_text = driver.find_element_by_class_name(radiobutton)
    assert only_click == radiobutton_text.text
    male = driver.find_element_by_xpath(male_link)
    assert not male.is_selected()
    female = driver.find_element_by_xpath(female_link)
    assert not female.is_selected()
    sleep(3)
    driver.close()


@pytest.mark.singleradio
def test_check_value_click_male_display():  # for male radio button - test cases
    driver = webdriver.Chrome()
    driver.get(url)

    check_value_button = driver.find_element_by_id(buttoncheck)
    radiobutton_text = driver.find_element_by_class_name(radiobutton)
    male = driver.find_element_by_xpath(male_link)
    female = driver.find_element_by_xpath(female_link)

    male.click()
    assert male.is_selected()
    check_value_button.click()
    assert male_click == radiobutton_text.text
    assert not female.is_selected()
    sleep(3)
    driver.close()


@pytest.mark.singleradio
def test_check_value_click_female_display():  # for female radio button test cases
    driver = webdriver.Chrome()
    driver.get(url)

    check_value_button = driver.find_element_by_id(buttoncheck)
    radiobutton_text = driver.find_element_by_class_name(radiobutton)
    male = driver.find_element_by_xpath(male_link)
    female = driver.find_element_by_xpath(female_link)

    female.click()
    assert female.is_selected()
    check_value_button.click()
    assert female_click == radiobutton_text.text
    assert not male.is_selected()
    driver.close()

@pytest.mark.multipleradio
def test_button_text_assertion():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    assert button.text == button2_text
    driver.close()

@pytest.mark.multipleradio
def test_button_click_no_value():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    button.click()
    link = driver.find_element_by_xpath(button2_text_link)
    assert button2_text_generated == link.text
    driver.close()

@pytest.mark.multipleradio
def test_button_click_only_male():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    male = driver.find_element_by_xpath(male2_link)
    male.click()
    button.click()
    link = driver.find_element_by_xpath(button2_text_link)
    assert 'Sex : Male\nAge group:' == link.text
    driver.close()

@pytest.mark.multipleradio
def test_button_click_only_female():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    female = driver.find_element_by_xpath(fenale2_link)
    female.click()
    button.click()
    link = driver.find_element_by_xpath(button2_text_link)
    assert 'Sex : Female\nAge group:' == link.text
    driver.close()

@pytest.mark.multipleradio
def test_button_click_only_0_5():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    option1 = driver.find_element_by_xpath(Age_0_5)
    option1.click()
    button.click()
    link = driver.find_element_by_xpath(button2_text_link)
    assert 'Sex :\nAge group: 0 - 5' == link.text
    driver.close()

@pytest.mark.multipleradio
def test_button_click_male_and_5_15():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    male = driver.find_element_by_xpath(male2_link)
    option2 = driver.find_element_by_xpath(Age_5_15)
    male.click()
    option2.click()
    button.click()
    link = driver.find_element_by_xpath(button2_text_link)
    assert 'Sex : Male\nAge group: 5 - 15' == link.text
    driver.close()

@pytest.mark.multipleradio
def test_button_click_female_and_15_50():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(get_values_button)
    female = driver.find_element_by_xpath(fenale2_link)
    option2 = driver.find_element_by_xpath(Age_15_50)
    female.click()
    option2.click()
    button.click()
    link = driver.find_element_by_xpath(button2_text_link)
    assert 'Sex : Female\nAge group: 15 - 50' == link.text
    driver.close()




