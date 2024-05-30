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


@when(u'we visit "{text}"')
def step(context, text):
    context.browser.get(text)
    time.sleep(3)


@then('it should have a title "Google"')
def step(context):
    assert context.browser.title == "Google"
