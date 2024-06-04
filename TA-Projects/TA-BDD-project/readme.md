# BDD-tmta19 Project

## Description

The "BDD-tmta19" project is an automation testing suite written in Python using Selenium WebDriver and `behave`. This BDD (Behavior-Driven Development) framework is used for automated testing of various modules/features or functionalities of the web application.

### Application Under Test

- **Webpage**: [the-internet](https://the-internet.herokuapp.com/)

## Project Structure

### Features

- **features/**: Contains the feature files that define scenarios for each test.
  - `alerts.feature`
  - `brokenImages.feature`
  - `challengingDOM.feature`
  - `checkbox.feature`
  - `drag_and_drop.feature`
  - `dropdown.feature`
  - `jqueryUI_menu.feature`
  - `login.feature`
  - `logout.feature`

### Pages

- **pages/**: Contains the Python files with classes, selectors, and methods used for tests.
  - `base_page.py`: Defines common methods for all test page files.
  - `alerts_page.py`: Testing JavaScript Alerts.
  - `brokenImages_page.py`: Testing for the presence of broken images.
  - `challengingDOM_page.py`: Exercising and testing different selectors, buttons, and a canvas.
  - `checkbox_page.py`: Testing checkboxes.
  - `drag_and_drop_page.py`: Testing drag and drop functionality.
  - `dropdown_page.py`: Testing a dropdown.
  - `jqueryUI_menu_page.py`: Testing a jQuery UI menu.
  - `login_page.py`: Testing positive and negative account login scenarios and the corresponding messages.
  - `logout_page.py`: Testing account logout.

### Steps

- **steps/**: Contains the Python files with step definitions for the defined scenarios using the corresponding page files.
  - `alerts_steps.py`
  - `brokenImages_steps.py`
  - `challengingDOM_steps.py`
  - `checkbox_steps.py`
  - `drag_and_drop_steps.py`
  - `dropdown_steps.py`
  - `jqueryUI_menu_steps.py`
  - `login_steps.py`
  - `logout_steps.py`

### Configuration and Setup

- **behave.ini**: Defines the setup for HTML report format.
- **BddHerokuappTestResults.html**: HTML test results report.
- **driver.py**: Defines setup and teardown methods used for running tests.
- **environment.py**: Defines the hooks used for setup and teardown operations for steps files.
- **requirements.txt**: Used for manual management of the development environment and installation of dependencies.
  - To install the packages, run in a terminal:
    ```bash
    pip install -r requirements.txt
    ```
- **setup.py**: Defines the metadata for the Python project and specifies the required dependencies to install to run these tests.
  - To install the dependencies, run in terminal:
    ```bash
    pip install .
    ```

### Directory Structure

BDD-tmta/ <br />
|─ features/ <br />
|&emsp;&emsp;|── alerts.feature <br />
|&emsp;&emsp;|── brokenImages.feature <br />
|&emsp;&emsp;|── challengingDOM.feature<br />
|&emsp;&emsp;|── checkbox.feature<br />
|&emsp;&emsp;|── drag_and_drop.feature<br />
|&emsp;&emsp;|── dropdown.feature<br />
|&emsp;&emsp;|── jqueryUI_menu.feature<br />
|&emsp;&emsp;|── login.feature<br />
|&emsp;&emsp;|── logout.feature<br />
|─ pages/<br />
|&emsp;&emsp;|── alerts_page.py<br />
|&emsp;&emsp;|── base_page.py<br />
|&emsp;&emsp;|── brokenImages_page.py<br />
|&emsp;&emsp;|── challengingDOM_page.py<br />
|&emsp;&emsp;|── checkbox_page.py<br />
|&emsp;&emsp;|── drag_and_drop_page.py<br />
|&emsp;&emsp;|── dropdown_page.py<br />
|&emsp;&emsp;|── jqueryUI_menu_page.py<br />
|&emsp;&emsp;|── login_page.py<br />
|&emsp;&emsp;|── logout_page.py<br />
|─ steps/
|&emsp;&emsp;|── alerts_steps.py<br />
|&emsp;&emsp;|── brokenImages_steps.py<br />
|&emsp;&emsp;|── challengingDOM_steps.py<br />
|&emsp;&emsp;|── checkbox_steps.py<br />
|&emsp;&emsp;|── drag_and_drop_steps.py<br />
|&emsp;&emsp;|── dropdown_steps.py<br />
|&emsp;&emsp;|── jqueryUI_menu_steps.py<br />
|&emsp;&emsp;|── login_steps.py<br />
|&emsp;&emsp;|── logout_steps.py<br />
|─ BddHerokuappTestResults.html<br />
|─ behave.ini<br />
|─ driver.py<br />
|─ environment.py<br />
|─ readme.md<br />
|─ requirements.txt<br />
|─ setup.py<br />

## Test Results

To view my test results, download the HTL file [test report](https://github.com/Dragosne/TA-BDD-project/blob/main/BddHerokuappTestResults.html) locally and open it using Chrome.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Dragosne/TA-BDD-project.git
    cd TA-BDD-project
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt # or pip install . 
    ```

## Running Tests

### Tagnames used:

- alerts: @javascript_alerts
- broken images: @brokenImages
- challenging DOM: @challengingDOM & @buttons
- checkboxes: @checkboxes
- drag and drop: @drag_and_drop
- dropdown: @dropdown
- jquery UI: @jquery
- login: @login_negative @login_positive
- logout: @logout

To install the dependencies and run the tests, execute the following commands:

```bash
behave
```
or
```bash
behave --tags=(tagname)
```

This README provides an overview of my project, installation and test running instructions, and details about the test structure and results. You can adjust it according to your specific needs and preferences.
