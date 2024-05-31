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
    time.sleep(3)


@when(u'user enters "{text}" in search field')
def step_2(context, text):




@then('it should have a title "Google"')
def step(context):
    assert context.browser.title == "Google"
