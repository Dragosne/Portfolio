Feature: Deal with Challenging DOM: no helpful locators and a canvas element - herokuapp webpage

@challengingDOM
  Scenario: Finding elements on the table using different selectors
    Given Navigate to the Challenging DOM webpage
    Then I wish to find "Iuvaret1" element from the table using CSS and verify its text
    Then I wish to find "Iuvaret7" element from the table using CSS again and verify its text
    Then I wish to find "Definiebas5" element from the table using absolute XPATH and verify its text
    Then I wish to find "Adipisci5" element from the table using relative XPATH and verify its text
    Then I wish to find "Consequuntur5" element from the table using XPATH and verify its text
@buttons
  Scenario: Interact with the buttons and check if the canvas is changing
    Given Navigate to the Challenging DOM webpage
    Then I check & store the canvas initial state
    When I Click on the "1st" button (blue)
    Then I verify if the canvas changed after first action
    When Click on the "2nd" button (red)
    Then I verify if the canvas changed after second action
    When Click on the "3rd" button (green)
    Then I verify if the canvas changed after third action
