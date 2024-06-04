import unittest
from api_requests.groceryApiRequests import GroceryStoreApi



class OrdersOperations(unittest.TestCase):

    access_token = None

    def setUp(self):
        # using predefined api methods
        self.api_method = GroceryStoreApi()
        # get token
        if not self.access_token:
            self.access_token = self.api_method.post_auth_and_get_token()

    def test01_post_create_and_get_anOrder_positive(self):
        # create a new cart and add multiple items
        new_cart_response = self.api_method.post_create_newCart()
        cartId = new_cart_response.json()['cartId']

        # add products to cart
        product_to_add = self.api_method.post_add_items_to_cart_positive_entries()

        for product in product_to_add:
            response = self.api_method.post_add_product_in_Cart(cartId, json=product)

        # Get orders to check if any order already exist for this API client
        response = self.api_method.get_orders(self.access_token)

        # Response
        actual_status = response.status_code
        actual_get_all_orders_response = response.json()

        # Verify that get all orders succeeded and are no orders
        self.assertEqual(actual_status, 200, f"Get all orders failed. Status code is {actual_status} not 200")
        self.assertEqual(len(actual_get_all_orders_response), 0, f"No orders created for this API client. Response should be an Empty List, but actual is: {actual_get_all_orders_response} ")

        # Create a new order
        response = self.api_method.post_create_order(self.access_token, cartId, "Tom Smith", comment="Breakfast meal")

        actual_status = response.status_code
        self.assertEqual(actual_status, 201, f"Create a new cart: Actual status code is {actual_status} not 201")

        # Take the created order response
        created_order_response = response.json()

        # verify if the response is a dictionary, if the key are created, orderId are present and the created is True and OrderId is not Empty
        self.assertIsInstance(created_order_response, dict, f"The response for creating a new order should be a dictionary")
        self.assertIn('created', created_order_response, f"The response for creating a new order should have 'created'. Actual: {created_order_response}")
        self.assertIn('orderId', created_order_response, f"The response for creating a new order should have 'orderId'. Actual: {created_order_response}")
        self.assertEqual(created_order_response['created'], True, "Created value should be True")
        self.assertIsNotNone(created_order_response['orderId'], "The orderId value should not be None or Empty")


        # Store the order ID
        orderId = created_order_response["orderId"]

        # Check if the cart is deleted after the order placed
        cart_check_response = self.api_method.get_a_cart_by_cartId(cartId)
        self.assertEqual(cart_check_response.status_code, 404, "Cart should be deleted after creating the order")

        # Get the created order by orderId
        response = self.api_method.get_an_order_by_orderId(self.access_token, orderId)

        actual_status = response.status_code
        actual_response = response.json()

        self.assertEqual(actual_status, 200, f" Get a sigle order action failed. The status code is {actual_status} not 200")
        self.assertEqual(actual_response["id"], orderId, f"The created orderId {orderId} is not found. The actual response is: {actual_response['id']}")

        # verify if the customer name and the comment are correct

        expected_customer_name = 'Tom Smith'
        actual_customer_name = actual_response['customerName']
        expected_comment = 'Breakfast meal'
        actual_comment = actual_response['comment']

        self.assertEqual(actual_customer_name, expected_customer_name, f"The customer name not corresponding. Expected name: {expected_customer_name}. Actual name: {actual_customer_name}")
        self.assertEqual(actual_comment, expected_comment, f'The comment not corresponding. Expected comment: {expected_comment}. Actual comment: {actual_comment}')


        # verify if there are items in the cart and all the added products in the cart are in the created order
        self.assertIn('items', actual_response, "Response does not contain 'items'")

        expected_added_items = 3
        actual_items_inOrder = len(actual_response['items'])

        self.assertEqual(actual_items_inOrder, expected_added_items, f"Expected {expected_added_items} products in the cart but actual found: {actual_items_inOrder} products")

        # verify each item
        expected_products = {
            4875: 1,
            4641: 2,
            8554: 3
        }

        for product in actual_response['items']:
            product_id = product['productId']
            quantity = product['quantity']
            self.assertIn(product_id, expected_products, f"The product with ID {product_id} is not expected")
            expected_quantity = expected_products[product_id]
            self.assertEqual(quantity, expected_quantity, f"The quantity for product {product_id} is not as expected")

        # Delete the order
        delete = self.api_method.delete_by_orderId(self.access_token, orderId)
        self.assertEqual(delete.status_code, 204, f"Delete order fail. Expected 204")

    def test02_modify_customerName_anOrder(self):
        # create a new cart
        new_cart_response = self.api_method.post_create_newCart()
        cartId = new_cart_response.json()['cartId']

        # add products to cart
        product_to_add = self.api_method.post_add_items_to_cart_positive_entries()
        for product in product_to_add:
            response = self.api_method.post_add_product_in_Cart(cartId, json=product)

        # Create a new order
        response = self.api_method.post_create_order(self.access_token, cartId, "Tom & Jerry", comment="Dinner food")

        # Check if the order have been created
        actual_status = response.status_code
        self.assertEqual(actual_status, 201, f"Create a new cart: Actual status code is {actual_status} not 201")

        # Take the orderId
        orderId = response.json()['orderId']

        # Modify the customer name
        new_customerName = "Robert Crest"
        response = self.api_method.patch_an_order(self.access_token, orderId, customerName=new_customerName)

        # Verify that the modification was successful
        actual_code = response.status_code
        expected_code = 204
        self.assertEqual(expected_code, actual_code,
                         f"Modify item failed: Expected status code {expected_code}, but found Actual status code: {actual_code}")

        # Get the modified order
        response = self.api_method.get_an_order_by_orderId(self.access_token, orderId)

        # Verify that get a single order action worked
        actual_code = response.status_code
        expected_code = 200
        self.assertEqual(expected_code, actual_code,
                         f"Modify item failed: Expected status code {expected_code}, but found Actual status code: {actual_code}")

        expected_name = new_customerName
        actual_name = response.json()["customerName"]
        old_name = "Tom & Jerry"
        actual_response = response.json()

        self.assertEqual(actual_name, expected_name, f"The expected name {expected_name} not found after oreder patch. Actual: {actual_name}.")
        self.assertNotIn(old_name, actual_response, f"The old customer name: {old_name} still found in {actual_response}. Should be deleted after oreder patch.")

        # verify if the order contains all the products after the name changing
        expected_products = {
            4875: 1,
            4641: 2,
            8554: 3
        }

        for product in actual_response['items']:
            product_id = product['productId']
            quantity = product['quantity']
            self.assertIn(product_id, expected_products, f"The product with ID {product_id} is not expected")
            expected_quantity = expected_products[product_id]
            self.assertEqual(quantity, expected_quantity, f"The quantity for product {product_id} is not as expected")

        delete = self.api_method.delete_by_orderId(self.access_token, orderId)
        self.assertEqual(delete.status_code, 204, f"Delete order fail.")

    def test03_delete_anOrder(self):
        # create a new cart and add multiple items
        new_cart_response = self.api_method.post_create_newCart()
        cartId = new_cart_response.json()['cartId']

        # choose a product by category and add the second product id in the cart
        list_products = self.api_method.get_products_by_category('fresh-produce')
        choose_second_listed_product = list_products.json()[1]['id']
        product_json = {'productId': choose_second_listed_product}

        add_an_item_to_cart = self.api_method.post_add_product_in_Cart(cartId, json=product_json)

        # create a new order and store the orderId
        create_new_order = self.api_method.post_create_order(self.access_token, cartId, "Sandy")
        orderId = create_new_order.json()['orderId']

        # get the order and check if not empty
        get_the_order = self.api_method.get_an_order_by_orderId(self.access_token, orderId)
        self.assertEqual(get_the_order.status_code, 200, f"Get order failed. Actual status code: {get_the_order.status_code}")
        self.assertTrue(len(get_the_order.json()['items']) == 1, f'get order is empty')

        # Delete the order
        delete_order = self.api_method.delete_by_orderId(self.access_token, orderId)

        # verify the status
        self.assertEqual(delete_order.status_code, 204, f"Delete order fail.")

        # get the order by orderId and check if is deleted
        get_the_order = self.api_method.get_an_order_by_orderId(self.access_token, orderId)

        # verify the response message
        self.assertEqual(f'No order with id {orderId}.', get_the_order.json()['error'], f'Delete order fail')

    def test04_test_methods_unauthorised_401(self):

        # GET orders
        response = self.api_method.get_orders(access_token=None)

        # verify the status code
        actual_status = response.status_code
        expected_status = 401
        self.assertEqual(actual_status, expected_status, f'response for unauthorised user is not 401, actual: {actual_status}')

        # verify the response message
        expected_error_message = "Invalid bearer token."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message, f'Wrong error massage for unauthorised action: get orders. Expected: {expected_error_message}, Actual: {actual_status}')

        # GET order by orderId
        response = self.api_method.get_an_order_by_orderId(access_token=None, orderId=None)

        # verify the status code
        actual_status = response.status_code
        expected_status = 401
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 401, actual: {actual_status}')

        # verify the response message
        expected_error_message = "Invalid bearer token."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for unauthorised action: get order by orderId. Expected: {expected_error_message}, Actual: {actual_status}')

        # POST order by cartId
        response = self.api_method.post_create_order(access_token=None, cartId=None, customerName="John")

        # verify the status code
        actual_status = response.status_code
        expected_status = 401
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 401, actual: {actual_status}')

        # verify the response message
        expected_error_message = "Invalid bearer token."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for unauthorised post action: create new order. Expected: {expected_error_message}, Actual: {actual_status}')

        # PATCH order by orderId
        response = self.api_method.patch_an_order(access_token=None, orderId=None, customerName="Ron")

        # verify the status code
        actual_status = response.status_code
        expected_status = 401
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 401, actual: {actual_status}')

        # verify the response message
        expected_error_message = "Invalid bearer token."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for unauthorised action: patch order. Expected: {expected_error_message}, Actual: {actual_status}')

        # DELETE order by orderId

        response = self.api_method.delete_by_orderId(access_token=None, orderId=None)

        # verify the status code
        actual_status = response.status_code
        expected_status = 401
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 401, actual: {actual_status}')

        # verify the response message
        expected_error_message = "Invalid bearer token."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for unauthorised action: delete order. Expected: {expected_error_message}, Actual: {actual_status}')

    def test05_test_invalid_data(self):

        orderId = 'invalid_orderId'

        # GET order by orderId
        response = self.api_method.get_an_order_by_orderId(self.access_token, orderId=orderId)

        # verify the status code
        actual_status = response.status_code
        expected_status = 404
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 404, actual: {actual_status}')

        # verify the response message
        actual_error_message = response.json()['error']
        expected_error_message = f"No order with id {orderId}."
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for get an order with invalid orderId. Expected: {expected_error_message}, Actual: {actual_status}')

        # POST order by cartId
        response = self.api_method.post_create_order(self.access_token, cartId="invalid_cartId", customerName="John")

        # verify the status code
        actual_status = response.status_code
        expected_status = 400
        self.assertEqual(actual_status, expected_status,
                         f'response for create a new order with invalid cartId, actual: {actual_status}')

        # verify the response message
        expected_post_error_message = "Invalid or missing cartId."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_post_error_message,
                         f'Wrong error massage for create a new order with invalid cartId. Expected: {expected_post_error_message}, Actual: {actual_status}')

        # PATCH order by orderId
        response = self.api_method.patch_an_order(self.access_token, orderId=orderId, customerName="Ron")

        actual_status = response.status_code
        expected_status = 404
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 404, actual: {actual_status}')

        # verify the response message
        expected_error_message = f"No order with id {orderId}."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for patch order with invalid orderId. Expected: {expected_error_message}, Actual: {actual_status}')

        # DELETE order by orderId

        response = self.api_method.delete_by_orderId(self.access_token, orderId=orderId)

        actual_status = response.status_code
        expected_status = 404
        self.assertEqual(actual_status, expected_status,
                         f'response for unauthorised user is not 404, actual: {actual_status}')

        expected_error_message = f"No order with id {orderId}."
        actual_error_message = response.json()['error']
        self.assertEqual(actual_error_message, expected_error_message,
                         f'Wrong error massage for delete order with invalid orderId. Expected: {expected_error_message}, Actual: {actual_status}')
