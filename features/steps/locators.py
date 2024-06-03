from selenium.webdriver.common.by import By


class GoogleLocators:
    """Класс переменных для определения локаторов элементов на странице "https://google.com"""
    SEARCH_FIELD = (By.CSS_SELECTOR, 'textarea[name="q"]')


class KinoPoiskLocators:
    """Класс переменных для определения локаторов элементов на странице "https://kinopoisk.ru"""

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[aria-label="Фильмы, сериалы, персоны"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

