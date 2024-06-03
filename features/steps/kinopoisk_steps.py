from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from behave import *


@given(u'браузер на странице "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@when('я ввожу название фильма "{film_name}" в строку поиска')
def step_impl(context, film_name):
    context.browser.implicitly_wait(5)
    search_field = context.browser.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')
    ActionChains(context.browser).send_keys_to_element(search_field, film_name).pause(1).perform()


@when(u'и нажимаю элемент \'Поиск\'')
def step_impl(context):
    search_field = context.browser.find_element(By.CSS_SELECTOR, 'textarea[name="q"]')


@then(u'на странице отображаются результаты поиска')
def step_impl(context):
    context.browser.implicitly_wait(5)
    result = context.browser.find_elements(By.CSS_SELECTOR, 'div[class="MjjYud"]').is_displayed()
    assert result is True

