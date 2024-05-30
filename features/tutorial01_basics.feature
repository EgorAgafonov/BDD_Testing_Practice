
Feature: testing google

Scenario: visit google and check
  When we visit "https://www.google.com"
  Then it should have a title "Google"