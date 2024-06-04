Feature: Авторизация на сайте

  @foo.one
  Scenario: Авторизация на сайте с verify параметрами

    Given  Пользователь на странице "https://petfriends.skillfactory.ru/login"
    When Пользователь вводит в поле 'Электронная почта' свой "egorik@rambler.ru"
    And вводит в поле 'Пароль' свой "12345"
    And нажимает кнопку 'Войти'
    Then система адресует Пользователя на страницу path=/all_pets


  @foo.two
  Scenario Outline: Авторизация с non-verify параметрами

    Given  Пользователь на странице "https://petfriends.skillfactory.ru/login"
    When Пользователь вводит в поле 'Электронная почта' свой "<user_email>"
    And вводит в поле 'Пароль' свой "<user_password>"
    And нажимает кнопку 'Войти'
    Then система отказывает Пользователю в авторизации

    Examples:
      | user_email     | user_password |
      | '123456678'    | !@#~~~123     |
      | qwert@mail.ru  | qserty        |
      | alex@yandex.ru | alex12        |