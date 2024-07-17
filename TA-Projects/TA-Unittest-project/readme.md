# Unittest Project

## Description

This project contains automated test suites for the BebeTei website. The tests are written using Python's unittest framework and are organized to cover different functionalities of the site, including new user and registered user authentication, and shopping cart functionality testing.

## Project Structure

- **tests/**: This folder contains all the automated tests.
  - **tests/login_new_user.py**: Tests the login process for new users.
  - **tests/login_registered_user_positive.py**: Tests the login process for already registered users.
  - **tests/cart_test.py**: Tests the shopping cart functionality.
- **test_runner.py**: Script to run all tests and generate the report in HTML format.
    
## Test Results

To view my test results, download the HTML file: [test report](https://github.com/Dragosne/TA-Unittest-project/blob/main/Test%20Result_2024-05-21_15-43-58.html) locally and open it using Chrome.

## Environment
- **Python Version**: 3.x
- **Required Packages**: Listed in requirements.txt
- **Operating System:** Should work on Windows, macOS, and Linux
- **Browser**: Tests were performed using Google Chrome
  - **Version**: 126.0.6478.62 (Official Build) (x86_64)

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

## Running Tests

To run all tests and generate a report in HTML format, execute the `test_runner.py` script:

```bash
python test_runner.py
```
This README provides an overview of my project, installation and test running instructions, and details about the test structure and results. You can adjust it according to your specific needs and preferences.
