# from selenium.webdriver import ActionChains
# from selenium.webdriver import Keys
# from pages.base_page import BasePage
# from pages.locators import HomePageLocators
#
#
# class HomePage(BasePage):
#     """"""
#
#     def __init__(self, driver, timeout=10):
#         super().__init__(driver, timeout)
#
#         self.driver = driver
#
#     def enter_searching_address(self, text: str):
#         """"""
#
#         search_field = self.driver.find_element(*HomePageLocators.SEARCH_FIELD)
#         ActionChains(self.driver).send_keys_to_element(search_field, text).pause(1).perform()
