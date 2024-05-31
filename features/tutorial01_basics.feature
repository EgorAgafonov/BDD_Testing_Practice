Feature: Testing google

  Scenario: Searching field tests

    Given user is on page "https://www.google.ru"
    When user enters "Авиабилеты" in search field
    And click on enter button
    Then page displays search results