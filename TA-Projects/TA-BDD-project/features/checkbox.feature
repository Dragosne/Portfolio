Feature: Checkboxes Testing on herokuapp webpage

  @checkboxes
  Scenario: Click on the Checkboxes and check the functionality
    Given Navigate to the Checkboxes webpage
    Then Check the initial state of the Checkboxes
    When Click on the Checkbox_1
    Then Check the Checkboxes state after clicking on Checkbox_1
    When Click on the Checkbox_2
    Then Check the Checkboxes state after clicking on Checkbox_2
    When Click on both Checkboxes
    Then Check the Checkboxes state after clicking on both Checkboxes

