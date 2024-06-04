from selenium.webdriver.common.by import By


class GoogleLocators:
    """Класс переменных для определения локаторов элементов на странице "https://google.com"""
    SEARCH_FIELD = (By.CSS_SELECTOR, 'textarea[name="q"]')


class KinoPoiskLocators:
    """Класс переменных для определения локаторов элементов на странице "https://kinopoisk.ru"""

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[aria-label="Фильмы, сериалы, персоны"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    PROMO_VIDEO = (By.CSS_SELECTOR, 'div[aria-label="Промо"]')
    PROFILE_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Меню профиля"]')
    STACK_RESULTS = (By.CSS_SELECTOR, 'div[class="search_results"]')


class PetFriendsLocators:
    """Класс переменных для определения локаторов элементов на странице 'https://petfriends.skillfactory.ru/login'"""

    FIELD_EMAIL = (By.ID, 'email')
    FIELD_PASSWORD = (By.ID, 'pass')
    BUTTON_ENTER = (By.XPATH, '//button[@type="submit"]')
    DECK_CARD = (By.CSS_SELECTOR, 'div[class="card"]')

