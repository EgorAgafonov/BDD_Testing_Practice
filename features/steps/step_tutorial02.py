# from behave import *
# from selenium import webdriver
# from selenium.webdriver.chrome.options import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionBuilder
# from selenium.webdriver import Keys
#
#
# options = Options()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=options)
#
#
# @given('website "{url}"')
# def step(url):
#     driver.get(url)
#
#
# # Теперь нажмем на кнопку "Найти"
# @when('enter in the search field "{text}"')
# def step(text):
#     driver.implicitly_wait(5)
#     search_field = driver.find_element(By.CSS_SELECTOR, "input[id='text']")
#     ActionChains(driver).send_keys_to_element(search_field, text).pause(2).perform()
#
#
# @when('click on "{text}" button')
# def step():
#     search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     search_button.click()
#
#
#
# # # Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
# # @then("page include text '{text}'")
# # def step(context, text):
# #     WebDriverWait(context.browser, 120).until(
# #         EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
# #     )
# #     assert context.browser.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
# #     context.browser.quit()
