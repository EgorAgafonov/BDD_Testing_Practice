
Feature: testing google

  As a user
  In order to find information about object
  I want to enter object's name wright in search field

Given user is on page https://www.google.ru/
  When user enters "Авиабилеты" in search field
   And click on enter button
  Then page displays search results