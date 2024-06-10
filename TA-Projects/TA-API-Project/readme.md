# API Project

This project is designed to test the functionalities of Simple Grocery Store API. The structure includes API routes, input data, methods, and automated tests and reports.

### Application Under Test

- **Webpage**: [GroceryStore](https://github.com/vdespa/Postman-Complete-Guide-API-Testing/blob/main/simple-grocery-store-api.md)

## Project Structure

- **api_request/groceryapirequest.py:**
  - Contains the API routes, input data, and methods used in the grocery API.

- **reports/report.html:**
  - HTML report generated after running the tests, summarizing the test results.

- **tests/cart/test_cart.py:**
  - Contains tests related to cart operations such as creating a cart, adding items, modifying items, and deleting items.

- **tests/orders/test_orders.py:**
  - Contains tests related to order operations such as creating, modifying, and deleting orders.

- **tests/products/test_products.py:**
  - Contains tests related to product operations such as fetching all products, fetching by category, and handling invalid parameters.

- **requirements.txt:**
  - Lists the dependencies required to run the project.

- **test_runner.py:**
  - Script to execute all tests and generate the HTML report.
 
### Directory Structure

API_Project/ <br />
|─ api_request/ <br />
|&emsp;&emsp;|── groceryApiRequests.py <br />
|─ reports/ <br />
|&emsp;&emsp;|── GroceryStore API Test Result_2024-05-30_17-16-00.html <br />
|─ tests/ <br />
|&emsp;&emsp;|── cart.py <br />
|&emsp;&emsp;|── orders.py <br />
|&emsp;&emsp;|── products.py <br />
|─ requirements.txt/ <br />
|─ test_runner.py /<br />

## Test Results

To view my test results, download the HTL file [test report](https://github.com/Dragosne/TA-API-Project/blob/main/reports/GroceryStore%20API%20Test%20Result_2024-05-30_17-16-00.html) locally and open it using Chrome.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Dragosne/TA-API-Project
    cd API_Project
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Tests

1. **Run the tests using the test runner:**
    ```sh
    python test_runner.py
    ```

2. **View the HTML report:**
    - After running the tests, an HTML report is generated in the `reports/` folder. Open `report.html` in a web browser to view the test results.
  
This README provides an overview of my project, installation and test running instructions, and details about the test structure and results. You can adjust it according to your specific needs and preferences.
