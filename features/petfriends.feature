Feature: Авторизация и создание карточек на сайте ""https://petfriends.skillfactory.ru"

  Background: Авторизация в личном кабинете

    Given  Пользователь на странице "https://petfriends.skillfactory.ru/login"
    When Пользователь вводит в поле 'Электронная почта' свой "egorik@rambler.ru"
    And вводит в поле 'Пароль' свой "12345"
    And нажимает кнопку 'Войти'
    Then система адресует Пользователя на страницу path=/all_pets


  @foo.one
  Scenario: Авторизация с verify параметрами

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


  @foo.three
  Scenario: Размещение карточки питомца с verify параметрами

    Given Пользователь находится в личном кабинете (Мои питомцы)
    When Пользователь нажимает на кнопку 'Добавить питомца'
    And указывает фото питомца
    And вводит в форму карточки имя питомца "Тимофей"
    And название породы "бенгали"
    And  значение возраста "9"
    And нажимает кнопку 'Добавить'
    Then созданная карточка отображается в стеке питомцев Пользователя