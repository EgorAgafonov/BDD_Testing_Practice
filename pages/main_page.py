from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import MapPageLocators


class MainPage(BasePage):
    """Наследованный класс с атрибутами и методами для управления элементами на главной странице веб-приложения
    "Яндекс.Карты" (поисково-информационная картографическая служба Яндекса) в рамках проектирования UI-тестов по
    паттерну Page Object Model."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def enter_searching_address(self, driver, value: str):
        """Поиск топонима на веб-платформе Яндекс.Карты. Передает в поле поиска название(адрес) искомого объекта и
        подтверждает действие."""

        address_field = driver.find_element(*MapPageLocators.MAP_SEARCH_FIELD)
        ActionChains(driver).send_keys_to_element(address_field, value).pause(3).send_keys(Keys.DOWN)\
            .send_keys(Keys.ENTER) \
            .perform()

    def clear_searching_field(self, driver):
        """Метод очищает поле поиска от текста после ввода названия искомого топонима посредством воздействия на элемент
         'Закрыть' (крестик)."""

        clear_search_field = driver.find_element(*MapPageLocators.MAP_CLEAR_FIELD_BTN)
        clear_search_field.click()
