Feature: Login testing on the herokuapp webpage
@negative
  Scenario: Negative scenario: input wrong credentials
    Given I am on the login page
    When I insert an username "dragos"
    When I insert a password "parolatmta19"
    When I click on the login button
    Then The "unsuccessful logged in" banner is displayed
    Then The message is "Your username is invalid!"

@positive
  Scenario: Positive scenario: input correct credentials
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The "successful logged in" banner is displayed
    Then The message is "You logged into a secure area!"
