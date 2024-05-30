from selenium import webdriver
from selenium.webdriver.chrome.options import *


def before_all(context):
    options = Options()
    options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(options=options)


def after_all(context):
    context.browser.quit()
