from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from behave import *
from locators import GoogleLocators


@given('user is on page "{url}"')
def step_1(context, url):
    context.browser.get(url)


@when('user enters "{text}" in search field')
def step_2(context, text):
    context.browser.implicitly_wait(5)
    search_field = context.browser.find_element(*GoogleLocators.SEARCH_FIELD)
    ActionChains(context.browser).send_keys_to_element(search_field, text).pause(1).perform()


@when('click on enter button')
def step_3(context):
    search_field = context.browser.find_element(*GoogleLocators.SEARCH_FIELD)
    ActionChains(context.browser).send_keys_to_element(search_field).send_keys(Keys.ENTER).perform()


@then('page displays search results')
def step_4(context):
    context.browser.implicitly_wait(5)
    results = context.browser.find_elements(By.CSS_SELECTOR, 'div[class="MjjYud"]')
    for i in results:
        assert i.is_displayed() is not False
