from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ScrollOrigin
from behave import *
from locators import KinoPoiskLocators
import time
import selenium


@given(u'браузер на странице "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@when(u'я ввожу название фильма "{film_name}" в строку поиска')
def step_impl(context, film_name):
    context.browser.implicitly_wait(5)
    search_field = context.browser.find_element(*KinoPoiskLocators.SEARCH_FIELD)
    ActionChains(context.browser).send_keys_to_element(search_field, film_name).pause(1).perform()


@when(u'и нажимаю элемент \'Поиск\'')
def step_impl(context):
    search_button = context.browser.find_element(*KinoPoiskLocators.SEARCH_BUTTON)
    search_button.click()


@then(u'на странице отображаются результаты поиска')
def step_impl(context):
    context.browser.implicitly_wait(5)
    results = context.browser.find_element(*KinoPoiskLocators.STACK_RESULTS).is_displayed()

    assert results is not False


@when(u'Пользователь нажимает на элемент \'Расширенный поиск\'')
def step_impl(context):
    advncd_srch_bttn = context.browser.find_element(*KinoPoiskLocators.BUTTON_ADVANCED_SEARCH)
    advncd_srch_bttn.click()


@when(u'в разделе \'Премьера\' выбирает месяц \'Июнь\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    premier_field = context.browser.find_element(*KinoPoiskLocators.FIELD_PREMIER)
    context.browser.execute_script('window.scrollTo(0, 500);')
    premier_field.click()
    premier_field.send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN) \
        .send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()


@when(u'год \'2024\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    year_field = context.browser.find_element(*KinoPoiskLocators.FIELD_PREMIER)
    year_field.click()
    year_field.send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()


@when(u'страну премьеры \'США\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    country_field = context.browser.find_element(*KinoPoiskLocators.FIELD_PREMIER)
    country_field.click()
    country_field.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(2)


@when(u'нажимает кнопку \'Поиск\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    submit_btn = context.browser.find_element(*KinoPoiskLocators.BUTTON_SUBMIT_SEARCH)
    submit_btn.click()
    time.sleep(4)


@then(u'на странице отображается список всех премьер фильмов за указанный период')
def step_impl(context):
    context.browser.implicitly_wait(5)
    results = context.browser.find_element(*KinoPoiskLocators.PREMIERS_RESULTS).is_displayed()

    assert results is not False
