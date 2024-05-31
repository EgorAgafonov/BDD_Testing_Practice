from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver import Keys
import time


@given(u'user is on page "{url}"')
def step_1(context, url):
    context.browser.get(url)


@when(u'user enters "{text}" in search field')
def step_2(context, text):
    context.browser.implicitly_wait(5)
    search_field = context.browser.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
    ActionChains(context.browser).send_keys_to_element(search_field, text).pause(1).perform()


@when('click on enter button')
def step_3(context):
    search_field = context.browser.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
    ActionChains(context.browser).send_keys_to_element(search_field).send_keys(Keys.ENTER).perform()


@then('page displays search results')
def step_4(context):
    context.browser.implicitly_wait(5)
    results = context.browser.find_elements(By.CSS_SELECTOR, 'div[class="MjjYud"]')
    print(f"\nПо запросу найдено: {len(results)} сайтов (01 страница).")
