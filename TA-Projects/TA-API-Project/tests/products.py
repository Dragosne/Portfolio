import unittest
from api_requests.groceryApiRequests import GroceryStoreApi


class GetProducts(unittest.TestCase):
    def setUp(self):
        # using predefined api methods
        self.api_method = GroceryStoreApi()

    def test01_get_all_products(self):
        # Make GET all products request
        response = self.api_method.get_all_products()

        # # Expected and actual status code assertions
        expected_status_code = 200
        actual_status_code = response.status_code
        self.assertEqual(actual_status_code,
                         expected_status_code,
                         f"Returning the inventory Actual status code is {actual_status_code}, "
                         f"Expected status code: {expected_status_code}"
                         )

        # assertion: response should be a list and should have 20 products
        actual_response = response.json()
        expected_products_displayed = 20
        actual_products_displayed = len(actual_response)
        self.assertIsInstance(actual_response, list, "Grocery Products should be a list")
        self.assertEqual(actual_products_displayed, expected_products_displayed,
                         f"Returning products number is Actual: {actual_products_displayed}. Expected: {expected_products_displayed}")

        # for each product assert:
        for product in actual_response:
            # each product response is a dict
            self.assertIsInstance(product, dict, f"Each product should be a dictionary")

            # each dict should have id, category, name and inStock
            self.assertIn('id', product, "Product should have an 'id'")
            self.assertIn('category', product, "Product should have a 'category'")
            self.assertIn('name', product, "Product should have a 'name'")
            self.assertIn('inStock', product, "Product should have 'inStock'")

            # id value should be not none or empty, should be a positive number
            product_id = product['id']
            self.assertIsNotNone(product_id, f"The Product ID should not be None/Empty. Actual result is: {product_id}")
            self.assertIsInstance(product_id, int, f'The Product ID should be a number. Actual result is: {product_id}')
            self.assertTrue(int(product_id) >= 0, f'The Product ID should not be negative. Actual result is: {product_id}')

            # category value should be not none or empty, should be a string
            product_category = product['category']
            self.assertIsNotNone(product_category,f"The Product Category should not be None. Actual result is: {product_category}")
            self.assertIsInstance(product_category, str,f'The Product Category should be a string. Actual result is: {product_category}')

            # name value should be not none or empty, should be a string
            product_name = product['name']
            self.assertIsNotNone(product_name, f"The Product Name should not be None. Actual result is: {product_name}")
            self.assertIsInstance(product_name, str, f'The Product Name should be a string. Actual result is: {product_name}')

            # inStock value should be not none or empty, should be boolean
            product_inStock = product['inStock']
            self.assertIsNotNone(product_inStock, f"The Product Stock should not be None. Actual result is: {product_inStock}")
            self.assertIsInstance(product_inStock, bool, f'The Product Stock should be boolean. Actual result is: {product_inStock}')

            # Extract product IDs
            product_ids = [product['id'] for product in actual_response]

            # Check for unique IDs using a set and find duplicates
            unique_ids = set()
            duplicate_ids = set()
            for product_id in product_ids:
                if product_id in unique_ids:
                    duplicate_ids.add(product_id)
                unique_ids.add(product_id)

            # Assert no duplicates
            self.assertEqual(len(duplicate_ids), 0, f"The product ID should be Unique. Duplicate product IDs found: {duplicate_ids}")

    def test02_get_products_by_category_positive(self):
        # Get categories and responses
        category_responses = self.api_method.get_products_by_category_positive_entries()

        # Send request to API providing positive category parameter
        for category, response in category_responses.items():
            with self.subTest(category=category):

                # Verify that the API returns a successful response (status code 200)
                expected_status_code = 200
                actual_status_code = response.status_code
                self.assertEqual(expected_status_code, actual_status_code, f"'Get products by category' status code for category '{category}' is: Actual {actual_status_code}, Expected: {expected_status_code}")

                # Verify that the response contains a list of products
                products = response.json()
                self.assertIsInstance(products, list, f"Products should be a list for category '{category}'")

                # Verify that either response contains a dict of products with id, category, name and inStock field
                for product in products:
                    self.assertIsInstance(product, dict, "Each product should be a dictionary")
                    self.assertIn('id', product, "Product should have an 'id'")
                    self.assertIn('category', product, "Product should have a 'category'")
                    self.assertIn('name', product, "Product should have a 'name'")
                    self.assertIn('inStock', product, "Product should have 'inStock'")

                    # Verify that the response contains just products with selected category
                    actual_product_category = product['category']
                    expected_product_category = category
                    self.assertEqual(actual_product_category, expected_product_category,
                                     f"The Product Category should be expected: '{expected_product_category}' for actual category '{actual_product_category}'")

    def test03_get_product_by_category_negative(self):
        invalid_categories = self.api_method.get_invalid_categories()

        # Send request to API providing invalid category parameter
        for category, response in invalid_categories.items():
            with self.subTest(category=category):

                # Verify that the API returns a successful response (status code 400)
                expected_status_code = 400
                actual_status_code = response.status_code
                self.assertEqual(actual_status_code, expected_status_code, f"Expected status code {expected_status_code} for invalid category value '{category}'. Actual status code: {actual_status_code}")

    def test04_get_products_by_results_positive(self):
        valid_entries = self.api_method.get_products_by_results_positive_entries()

        # Send request to API providing positive results parameter
        for results, response in valid_entries.items():
            with self.subTest(num_results=results):

                # Verify that the API returns a successful response (status code 200)
                expected_status_code = 200
                actual_status_dode = response.status_code
                self.assertEqual(actual_status_dode, expected_status_code, f"Failed to get products with {results} results")

                # Verify that the response contains a list of products
                products = response.json()
                self.assertIsInstance(products, list, f"The response should be a list of products")

                # Verify that the response displays expected number of products
                actual_num_results = len(products)
                self.assertEqual(actual_num_results, results, f"Wrong number of products Expected: {results}. Actual: {actual_num_results}")

    def test05_get_products_by_results_negative(self):
        invalid_results = self.api_method.get_invalid_results()

        # Send request to API providing negative results parameter
        for num_results, response in invalid_results.items():
            with self.subTest(num_results=num_results):

                expected_response_code = 400
                actual_response_code = response.status_code
                # Verify that the API returns a successful response (status code 400)
                self.assertEqual(actual_response_code, expected_response_code,
                                 f"Expected status code {expected_response_code} for invalid results value '{num_results}'. Actual = {actual_response_code}")


    def test06_get_products_by_available_positive(self):
        available_positive_values = self.api_method.get_products_by_available_positive_entries()

        # send requests providing valid entries
        for available, response in available_positive_values.items():
            with self.subTest(available=available):

                # verify the status code
                expected_response_code = 200
                actual_response_code = response.status_code
                self.assertEqual(actual_response_code, expected_response_code,
                                 f"The Product list in stock {available}: should have the expected status code: '{expected_response_code}' but actual is: '{actual_response_code}'")

                # Verify that the response contains a list of products
                products = response.json()
                self.assertIsInstance(products, list, f"The response should be a list of products")

                # Verify that the response contains just product with selected availability
                # Convert 'true'/'false' strings to actual boolean values
                expected_product_availability = available.lower() == 'true'

                for product in products:
                    actual_product_availability = product['inStock']
                    self.assertEqual(actual_product_availability, expected_product_availability,
                                     f"The Product: {product} Availability: {available} Expected: '{expected_product_availability}' but actual is: '{actual_product_availability}'")

    def test07_get_products_by_available_negative(self):
        invalid_available_values = self.api_method.get_invalid_available()

        # Send request to API providing invalid entries
        for available, response in invalid_available_values.items():
            with self.subTest(available=available):

                expected_status_code = 400
                actual_status_code = response.status_code
                self.assertEqual(actual_status_code, expected_status_code,
                                 f"Expected status code {expected_status_code} for invalid available value '{available}. Actual status code: {actual_status_code}'")

    def test08_get_products_invalid_parameter(self):
        invalid_parameters = self.api_method.get_invalid_parameters()
        # check each negative entry
        for key, value in invalid_parameters.items():
            with self.subTest(param={key: value}):
                params = {key: value}
                response = self.api_method.get_products_by_parameters(params=params)
                # Verify that the API returns a successful response (status code 400)
                expected_status_code = 400
                actual_status_code = response.status_code
                self.assertEqual(expected_status_code, actual_status_code, f"Expected status code {expected_status_code} for invalid parameter '{params}'. Actual status code: {actual_status_code}'")

    def test09_get_status(self):
        # Make a GET status request
        response = self.api_method.get_status()

        # Expected and actual status code assertions
        expected_status_code = 200
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code,
                         f"'Get status' status code is: Actual{actual_status_code}, Expected: {expected_status_code}")

        # Expected and actual response message
        actual_response = response.json()["status"]
        expected_response = "UP"
        self.assertEqual(expected_response, actual_response,
                         f"The expected response for 'Get status' is {expected_response} but actual is: {actual_response}")
