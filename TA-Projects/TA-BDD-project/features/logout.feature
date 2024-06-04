
Feature: Logout testing on the herokuapp webpage
  @logout
  Scenario: Successful logout and return to the login page
    Given The user is logged in
    When The user clicks on the Logout button
    Then The text banner is displayed
    Then The displayed message is "You logged out of the secure area!"
    Then The user is redirected to the "Login Page"
