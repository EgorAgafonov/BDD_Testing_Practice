Feature: Авторизация на сайте



  Scenario: Авторизация на сайте с валидными параметрами

    Given  Пользователь на странице "https://petfriends.skillfactory.ru/login"
    When Пользователь вводит в поле 'Электронная почта' свой "email"
    And вводит в поле 'Пароль' свой "password"
    And нажимает кнопку 'Войти'
    Then система адресует Пользователя на страницу path=/all_pets