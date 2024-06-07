from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from behave import *
from locators import KinoPoiskLocators
import time


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
    search_button = context.browser.find_element(*KinoPoiskLocators.SEARCH_BUTTON)
    search_button.click()



@when(u'в разделе \'Премьера\' выбирает месяц \'Июнь\'')
def step_impl(context):



@when(u'год \'2024\'')
def step_impl(context):



@when(u'страну премьеры \'США\'')
def step_impl(context):



@then(u'на странице отображается список всех премьер фильмов за указанный период')
def step_impl(context):