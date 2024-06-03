from selenium.webdriver.common.by import By


class GoogleLocators:
    pass


class KinoPoiskLocators:
    """Класс переменных для определения локаторов элементов на странице "https://kinopoisk.ru"""

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[aria-label="Фильмы, сериалы, персоны"]')
