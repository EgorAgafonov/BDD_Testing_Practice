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
    BUTTON_ADVANCED_SEARCH = (By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]')
    FIELD_PREMIER = (By.ID, 'prem_month')
    BUTTON_SUBMIT_SEARCH = (By.XPATH, '//*[@id="formSearchMain"]/input[11]')


class PetFriendsLocators:
    """Класс переменных для определения локаторов элементов на странице 'https://petfriends.skillfactory.ru/login'"""

    FIELD_EMAIL = (By.ID, 'email')
    FIELD_PASSWORD = (By.ID, 'pass')
    BUTTON_ENTER = (By.XPATH, '//button[@type="submit"]')
    BUTTON_MY_PETS = (By.CSS_SELECTOR, 'a[href="/my_pets"]')
    BUTTON_ADD_CARD = (By.CSS_SELECTOR, 'button[data-target="#addPetsModal"]')
    FIELD_PET_PHOTO = (By.CSS_SELECTOR, 'input[name="photo"]')
    FIELD_PET_NAME = (By.ID, 'name')
    FIELD_PET_BREED = (By.ID, 'animal_type')
    FIELD_PET_AGE = (By.ID, 'age')
    BUTTON_SUBMIT_CARD = (By.CSS_SELECTOR, 'button[onclick="add_pet();"]')
    STACK_CARDS = (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    MY_PETS_QUANTITY = (By.XPATH, "//*[@id='all_my_pets']/table/tbody/tr")

