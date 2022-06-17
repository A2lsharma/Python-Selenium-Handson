from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

'''test_input_forms


Constants used in Both Tests'''

url = 'https://www.seleniumeasy.com/test/input-form-demo.html'
first_name_link = 'first_name'   # Search by name
last_name_link = 'last_name'   # Search by name
email_link = 'email'    # Search by name
phone_link = 'phone'   # Search by name
address_link = 'address'   # Search by name
city_link = 'city'   # Search by name
state_link =  'state'   # Search by name
zip_link = 'zip'   # Search by name
website_link = 'website'    # Search by name
yes_link = '//*[@id="contact_form"]/fieldset/div[10]/div/div[1]/label'    # Search by xpath
no_link = '//*[@id="contact_form"]/fieldset/div[10]/div/div[2]/label'     # Search by xpath
comment_link = 'comment'   # Search by name
button_link = '//*[@id="contact_form"]/fieldset/div[13]/div/button'   # Search by xpath
fname_message_link = '//*[@id="contact_form"]/fieldset/div[1]/div/small[2]'   # Search by xpath
lname_message_link = '//*[@id="contact_form"]/fieldset/div[2]/div/small[2]'
email_message_link = '//*[@id="contact_form"]/fieldset/div[3]/div/small[1]'
phone_message_link = '//*[@id="contact_form"]/fieldset/div[4]/div/small[1]'
address_message_link = '//*[@id="contact_form"]/fieldset/div[5]/div/small[2]'
city_message_link = '//*[@id="contact_form"]/fieldset/div[6]/div/small[2]'
state_message_link = '//*[@id="contact_form"]/fieldset/div[7]/div/small'
zip_message_link = '//*[@id="contact_form"]/fieldset/div[8]/div/small[1]'
comment_message_link = '//*[@id="contact_form"]/fieldset/div[11]/div/small[2]'


@pytest.mark.inputforms
def test_no_input():
    driver = webdriver.Chrome()
    driver.get(url)
    send = driver.find_element_by_xpath(button_link)
    send.click()
    fname_message = driver.find_element_by_xpath(fname_message_link)
    assert fname_message.text == 'Please supply your first name'
    lname_message = driver.find_element_by_xpath(lname_message_link)
    assert lname_message.text == 'Please supply your last name'
    email_message = driver.find_element_by_xpath(email_message_link)
    assert email_message.text == 'Please supply your email address'
    phone_message = driver.find_element_by_xpath(phone_message_link)
    assert phone_message.text == 'Please supply your phone number'
    address_message = driver.find_element_by_xpath(address_message_link)
    assert address_message.text == 'Please supply your street address'
    city_message = driver.find_element_by_xpath(city_message_link)
    assert city_message.text == 'Please supply your city'
    state_message = driver.find_element_by_xpath(state_message_link)
    assert state_message.text == 'Please select your state'
    zip_message = driver.find_element_by_xpath(zip_message_link)
    assert zip_message.text == 'Please supply your zip code'
    comment_message = driver.find_element_by_xpath(comment_message_link)
    assert comment_message.text == 'Please supply a description of your project'

@pytest.mark.inputforms
def test_inputs():
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_xpath(button_link)

    fname = driver.find_element_by_name(first_name_link)
    fname.clear()
    fname.send_keys('fname')
    sleep(2)
    lname = driver.find_element_by_name(last_name_link)
    lname.clear()
    lname.send_keys('lname')
    sleep(2)
    email = driver.find_element_by_name(email_link)
    email.clear()
    email.send_keys('test@gmail.com')
    sleep(2)
    phone = driver.find_element_by_name(phone_link)
    phone.clear()
    phone.send_keys('(845)-1555555')
    sleep(2)
    address = driver.find_element_by_name(address_link)
    address.clear()
    address.send_keys('Home address')
    sleep(2)
    city = driver.find_element_by_name(city_link)
    city.clear()
    city.send_keys('Vatican City')
    sleep(2)
    state = driver.find_element_by_name(state_link)
    state.click()
    florida = driver.find_element_by_xpath('//*[@id="contact_form"]/fieldset/div[7]/div/div/select/option[11]')
    florida.click()
    sleep(2)
    zip = driver.find_element_by_name(zip_link)
    zip.clear()
    zip.send_keys('19000')
    sleep(2)
    comment = driver.find_element_by_name(comment_link)
    comment.clear()
    comment.send_keys('It\'s a Comment')
    sleep(2)
    yes = driver.find_element_by_xpath(yes_link)
    yes.click()
    sleep(2)
    no = driver.find_element_by_xpath(no_link)
    button.click()
