import time

from selenium.webdriver import ActionChains
from behave import *
from locators import PetFriendsLocators
from urllib.parse import urlparse
import os


@given('Пользователь на странице "{url}"')
def step_impl(context, url):
    context.browser.get(url)


@when('Пользователь вводит в поле \'Электронная почта\' свой "{email}"')
def step_impl(context, email):
    context.browser.implicitly_wait(5)
    email_field = context.browser.find_element(*PetFriendsLocators.FIELD_EMAIL)
    ActionChains(context.browser).send_keys_to_element(email_field, email).pause(1).perform()


@when('вводит в поле \'Пароль\' свой "{password}"')
def step_impl(context, password):
    context.browser.implicitly_wait(5)
    pass_field = context.browser.find_element(*PetFriendsLocators.FIELD_PASSWORD)
    ActionChains(context.browser).send_keys_to_element(pass_field, password).pause(1).perform()


@when('нажимает кнопку \'Войти\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    enter_btn = context.browser.find_element(*PetFriendsLocators.BUTTON_ENTER)
    enter_btn.click()
    time.sleep(1)


@then('система адресует Пользователя на страницу path=/all_pets')
def step_impl(context):
    context.browser.implicitly_wait(5)
    current_url = urlparse(context.browser.current_url)

    assert current_url.path == '/all_pets', "\nTest Failed! Current URL's path is not /all_pets."


@then('система отказывает Пользователю в авторизации')
def step_impl(context):
    context.browser.implicitly_wait(5)
    current_url = urlparse(context.browser.current_url)

    assert current_url.path != '/all_pets', "\nTest Failed! Current URL's path is /all_pets."


@given(u'Пользователь находится в личном кабинете (Мои питомцы)')
def step_impl(context):
    context.browser.implicitly_wait(5)
    mypets_btn = context.browser.find_element(*PetFriendsLocators.BUTTON_MY_PETS)
    mypets_btn.click()


@when(u'Пользователь нажимает на кнопку \'Добавить питомца\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    addpet_btn = context.browser.find_element(*PetFriendsLocators.BUTTON_ADD_CARD)
    addpet_btn.click()
    time.sleep(1)


@when(u'указывает фото питомца')
def step_impl(context):
    context.browser.implicitly_wait(5)
    input_field = context.browser.find_element(*PetFriendsLocators.FIELD_PET_PHOTO)
    pet_photo = os.path.abspath('cat_1.jpg')
    input_field.send_keys(pet_photo)


@when(u'вводит в форму карточки имя питомца "{name}"')
def step_impl(context, name):
    context.browser.implicitly_wait(5)
    name_field = context.browser.find_element(*PetFriendsLocators.FIELD_PET_NAME)
    ActionChains(context.browser).send_keys_to_element(name_field, name).pause(1).perform()


@when(u'название породы "{breed}"')
def step_impl(context, breed):
    context.browser.implicitly_wait(5)
    breed_field = context.browser.find_element(*PetFriendsLocators.FIELD_PET_BREED)
    ActionChains(context.browser).send_keys_to_element(breed_field, breed).pause(1).perform()


@when(u'значение возраста "{age}"')
def step_impl(context, age):
    context.browser.implicitly_wait(5)
    age_field = context.browser.find_element(*PetFriendsLocators.FIELD_PET_AGE)
    ActionChains(context.browser).send_keys_to_element(age_field, age).pause(1).perform()


@when(u'нажимает кнопку \'Добавить\'')
def step_impl(context):
    context.browser.implicitly_wait(5)
    submit_btn = context.browser.find_element(*PetFriendsLocators.BUTTON_SUBMIT_CARD)
    submit_btn.click()
    time.sleep(1)


@then(u'созданная карточка отображается в стеке питомцев Пользователя')
def step_impl(context):
    context.browser.implicitly_wait(5)
    results = context.browser.find_elements(*PetFriendsLocators.STACK_CARDS)
    assert len(results) != 0
