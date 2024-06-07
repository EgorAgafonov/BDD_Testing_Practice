Feature: Поиск фильмов с расширенными параметрами

  Scenario: Поиск фильмов по месту и дате премьеры
    Given браузер на странице "https://www.kinopoisk.ru/"
    When Пользователь нажимает на элемент 'Расширенный поиск'
    And в разделе 'Премьера' выбирает месяц 'Июнь'
    And год '2024'
    And страну премьеры 'США'
    Then на странице отображается список всех премьер фильмов за указанный период

