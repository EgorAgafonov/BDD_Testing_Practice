from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import *
from behave import fixture, use_fixture


@fixture
def browser_chrome(context):
    options = Options()
    options.add_argument("--start-maximized")
    context.browser = Chrome(options=options)
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser_chrome, context)
