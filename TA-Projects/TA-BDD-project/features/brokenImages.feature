Feature: Looking for Broken Images on herokuapp webpage
@brokenImages
  Scenario: Are any broken images on the webpage?
    Given Navigate to the webpage
    When The page is loaded
    Then Check if there are broken images