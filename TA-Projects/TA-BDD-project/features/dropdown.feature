Feature: Dropdown testing on the herokuapp webpage
@dropdown
  Scenario: Checking Dropdown functionality using Select class
    Given Navigate to the Dropdown webpage
    When Switch to first dropdown option by visible text "Option 1"
    Then After the first selection dropdown displays "Option 1" and his value is "1"
    When Switch to second dropdown option by visible text "Option 2"
    Then After the second selection dropdown displays "Option 2" and his value is "2"