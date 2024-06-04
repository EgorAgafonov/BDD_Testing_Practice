from selenium.webdriver import ActionChains
from behave import *
from locators import PetFriendsLocators
from features.steps.settings import valid_password, valid_email


@given('Пользователь на странице "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@when('Пользователь вводит в поле \'Электронная почта\' свой "{email}"')
def step_impl(context, email=valid_email):
    context.browser.implicitly_wait(5)
    email_field = context.browser.find_element(*PetFriendsLocators.FIELD_EMAIL)
    ActionChains(context.browser).send_keys_to_element(email_field, email).pause(1).perform()


@when('вводит в поле \'Пароль\' свой "{password}"')
def step_impl(context, password=valid_password):
    context.browser.implicitly_wait(5)
    pass_field = context.browser.find_element(*PetFriendsLocators.FIELD_PASSWORD)
    ActionChains(context.browser).send_keys_to_element(pass_field, password).pause(1).perform()


@when('нажимает кнопку \'Войти\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    enter_btn = context.browser.find_element(*PetFriendsLocators.BUTTON_ENTER)
    enter_btn.click()


@then(u'система адресует Пользователя на страницу path=/all_pets')
def step_impl(context):
    context.browser.implicitly_wait(5)
    current_url = context.browser.current_url

    assert current_url == '/all_pets', "\nTest Failed! Current URL's path is not /all_pets."
