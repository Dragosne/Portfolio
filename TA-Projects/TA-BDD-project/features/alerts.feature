Feature: Testing JavaScript Alerts on herokuapp webpage

@javascript_alerts
  Scenario: Clicking JS Alerts button and check the alert
    Given I am on the alerts page
    When I click on JS alert button
    When I accept the JS alert
    Then The message on JavaScript Alerts page is "You successfully clicked an alert"

  Scenario: Clicking JS Confirm button and check the alert
    Given I am on the alerts page
    # clicking OKay - accept alert
    When I click on JS confirm button
    When I accept the JS confirm alert
    Then The message on JavaScript Alerts page if accept is "You clicked: Ok"
    # clicking CANCEL - dismiss alert
    When I click on JS confirm button again
    When I am CANCEL the JS confirm alert
    Then The message on JavaScript Alerts page if dismiss is "You clicked: Cancel"

  Scenario: Clicking JS Prompt button and check the alert
    Given I am on the alerts page
    # input text and click OKay - accept alert
    When I click on the JS prompt button
    When Input the text "JavaScript" in alert field
    When I click OK on the JS Prompt alert
    Then The message on JavaScript Alerts page after the input is "You entered: JavaScript"
    # no input and click CANCEL - dismiss alert
    When I click on the JS prompt button again
    When I am CANCEL the JS Prompt alert
    Then The message on JavaScript Alerts page if cancel is "You entered: null"





