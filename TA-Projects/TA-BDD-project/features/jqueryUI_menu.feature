Feature: Testing JQuery Menu on herokuapp webpage
@jquery
  Scenario: Testing Enable -> Downloads -> PDF, CSV, Excel - menu functionality and file downloading
    Given Navigate to the JQuery Menu webpage
    When Move the mouse cursor to Enable -> Downloads -> PDF
    When Click on the first suboption "PDF"
    Then "PDF" file named "menu.pdf" is downloading

    When Move the mouse cursor to Enable -> Downloads -> CSV
    When Click on the second suboption "CSV"
    Then "CSV" file format: "menu.csv" is downloading

    When Move the mouse cursor to Enable -> Downloads -> Excel
    When Click on the third suboption "Excel"
    Then "Excel" file named "menu.xls" is downloading in computer
