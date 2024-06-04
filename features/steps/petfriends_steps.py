from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from behave import *
from locators import PetFriendsLocators
from dotenv import load_dotenv
import os

load_dotenv()


@given('Пользователь на странице "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@when('Пользователь вводит в поле \'Электронная почта\' свой "{email}"')
def step_impl(context, email=os.getenv("EMAIL")):
    context.browser.implicitly_wait(5)
    email_field= context.browser.find_element(*PetFriendsLocators.FIELD_EMAIL)
    ActionChains(context.browser).send_keys_to_element(email_field, email).pause(1).perform()


@when('вводит в поле \'Пароль\' свой "{password}"')
def step_impl(context, password=os.getenv("PASSWORD")):
    context.browser.implicitly_wait(5)
    pass_field = context.browser.find_element(*PetFriendsLocators.FIELD_PASSWORD)
    ActionChains(context.browser).send_keys_to_element(pass_field, password).pause(1).perform()


@when(u'нажимает кнопку \'Войти\'')
def step_impl(context):


@then(u'система адресует Пользователя на страницу path=/all_pets')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then система адресует Пользователя на страницу path=/all_pets')