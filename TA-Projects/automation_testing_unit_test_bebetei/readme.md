# Unittest Project

## Description

This project contains automated test suites for the BebeTei website, using Python's unittest framework. </br>
The tests cover various functionalities such as new user and registered user authentication, along with shopping cart functionality. </br>

## Project Structure

- **reports/**: Contains the test results HTML reports file
- **tests/**: Contains all automated tests.
  - **tests/login_new_user.py**: Tests the login process for new users.
  - **tests/login_registered_user_positive.py**: Tests the login process for already registered users.
  - **tests/cart_test.py**: Tests the shopping cart functionality.
- **test_runner.py**: Script to run all tests and generate an HTML report.
    
## Test Results

Download the HTML file to view my test results: [here](https://github.com/Dragosne/Portfolio/blob/main/TA-Projects/automation_testing_unit_test_bebetei/reports/Test%20Result_2024-05-21_15-43-58.html) and open it using Chrome.
For a quick view click on: [png test report](https://github.com/Dragosne/Portfolio/blob/main/TA-Projects/TA-Unittest-project/reports/report.png)

## Environment
- **Python Version**: 3.x
- **Required Packages**: Listed in `requirements.txt`
- **Operating System**: Compatible with Windows, macOS, and Linux
- **Browser**: Google Chrome
  - **Version**: 126.0.6478.62 (Official Build) (x86_64)

## Important Notes Before Running Tests

**Credentials Requirement**: Credentials used in the test scripts are not included in this repository for security reasons.

After cloning or downloading this project, you must update certain variables with your own credentials to ensure the test suites run correctly. </br>
These credentials are necessary for authenticating user sessions during the tests. </br>
Please create an account on the [BebeTei website](https://comenzi.bebetei.ro/) and update the test scripts with your email and password as needed.</br>

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Dragosne/TA-Unittest-project.git
    cd TA-Unittest-project
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Steps to Update Your Credentials:

1. **Open the project**: Navigate to **login_registered_user_positive.py** in the project directory.
2. **Edit the file**: Search for the following constants and replace them with your actual registered email, name and surname, and valid password:
   - `EMAIL_POSITIVE_INPUT = "<write here your registered email>"`
   - `USER_NAME = "<write here your account name and surname>"`
   - `PASSWORD_POSITIVE_INPUT = "<write here your valid password>"`
   - `SUCCESS_LOGIN_PAGE_EXPECTED_MESSAGE = 'Bun venit, <write here your account name and surname>!'`
3. **Save the file**: Ensure you save the changes before running the tests.

Ensure these credentials are stored securely and are not hard-coded in the scripts if they are to be shared publicly or within an insecure environment.

## Running Tests

To run all tests and generate a report in HTML format, execute the `test_runner.py` script:

```bash
python test_runner.py

