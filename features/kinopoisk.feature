Feature: Поиск фильмов

  Scenario Outline: Ввод названия фильма с валидными параметрами

    Given браузер на странице "https://www.kinopoisk.ru/"
    When я ввожу название фильма "<Название_фильма>" в строку поиска
    And и нажимаю элемент 'Поиск'
    Then на странице отображаются результаты поиска

    Examples:
      | Название_фильма          |
      | Брат 2                   |
      | Охотники за привидениями |
      | Один дома 2              |
