Feature: Testing main google page

  As a user
  In order to find information about object
  I want to enter object's name in searching field
  and page will display the results of searching

  Scenario Outline: Searching field tests

    Given user is on page "https://www.google.ru"
    When user enters "<object>" in search field
    And click on enter button
    Then page displays search results

    Examples:
      | object          |
      | Авиабилеты      |
      | Отели в г.Сочи  |
      | Видеоигры       |
