import unittest
from api_requests.groceryApiRequests import GroceryStoreApi

class CartOperations(unittest.TestCase):

    def setUp(self):
        # using predefined api methods
        self.api_method = GroceryStoreApi()

    def test01_create_new_cart(self):
        # post: create a new cart
        response = self.api_method.post_create_newCart()

        # assertion: status code
        expected_status_code = 201
        actual_status_code = response.status_code
        self.assertEqual(actual_status_code,
                         expected_status_code,
                         f"Create a new cart: Actual status code is {actual_status_code}, "
                         f"Expected status code: {expected_status_code}"
                         )

        actual_response = response.json()

        # verify if the response is a dictionary
        self.assertIsInstance(actual_response, dict, "The response for creating a new cart should be a dictionary")

        # verify if the response contains the key 'created'
        self.assertIn('created', actual_response, f"The response for creating a cart should have 'created'. Actual: {actual_response}")

        # verify if the response contains the key 'cartId'
        self.assertIn('cartId', actual_response, f"The response for creating a cart should have. Actual result is:{actual_response}")

        actual_created_value = actual_response['created']
        expected_created_value = True

        # verify if the value "created" is True
        self.assertEqual(actual_created_value, expected_created_value, f'Created should be {expected_status_code}, actual is: {actual_created_value}')

        cartId_value = actual_response['cartId']

        # verify if the cartId is not none or empty
        self.assertIsNotNone(cartId_value, f"The Cart ID should not be None/Empty. Actual result is: {cartId_value}")

    def test02_add_items_to_cart(self):
        # Create a new cart
        create_newCart = self.api_method.post_create_newCart()
        cartId = create_newCart.json()['cartId']
        product_to_add = self.api_method.post_add_items_to_cart_positive_entries()

        # assertion: each product added to cart successfully
        for product in product_to_add:
            response = self.api_method.post_add_product_in_Cart(cartId, json=product)
            actual_status = response.status_code
            expected_status = 201
            self.assertEqual(actual_status, expected_status,
                             f"Failed to add in the cart the product {product}. Actual status: {actual_status}. Expected status: {expected_status}.")

        # get cart items
        cart_response = self.api_method.get_a_cart_by_cartId(cartId)

        # get cart success
        actual_status = cart_response.status_code
        expected_status = 200
        self.assertEqual(actual_status, expected_status,
                         f"Failed to get cart. Actual status: {actual_status}. Expected status: {expected_status}.")

        # check if the added products are in the cart after get cart
        cart_data = cart_response.json()['items']

        # expected products and quantities
        expected_products = {
            4875: 1,
            4641: 2,
            8554: 3
        }

        # verify if are 3 products in the cart
        expected_added_items = 3
        actual_items_inCart = len(cart_data)

        self.assertEqual(actual_items_inCart, expected_added_items, f"Expected {expected_added_items} products in the cart but actual found: {actual_items_inCart} products")

        # verify if the response is a list of products
        self.assertIsInstance(cart_data, list, "The response for multiple items added in the cart should be a list")

        # Verify each item
        for product in cart_data:
            product_id = product['productId']
            quantity = product['quantity']
            self.assertIn(product_id, expected_products, f"The product with ID {product_id} is not expected")
            expected_quantity = expected_products[product_id]
            self.assertEqual(quantity, expected_quantity, f"The quantity for product {product_id} is not as expected")

    def test03_modify_cartItem(self):
        # Create a new cart
        create_newCart = self.api_method.post_create_newCart()
        cartId = create_newCart.json()['cartId']
        product_to_add = self.api_method.post_add_items_to_cart_positive_entries()

        # add items to cart
        for product in product_to_add:
            response = self.api_method.post_add_product_in_Cart(cartId, json=product)

        # Retrieve the cart items
        get_cart_response = self.api_method.get_a_cart_by_cartId(cartId)
        cart_products = get_cart_response.json()

        # Store the initial state of the cart
        initial_cart_state = cart_products.copy()

        # Define the data for modifying an item
        new_data = {"productId": 4875, "quantity": 5}

        # Find the itemId for product 4875 to be modified
        itemId = None
        for item in cart_products['items']:
            if item['productId'] == new_data['productId']:
                itemId = item['id']
                break

        # Ensure that the itemId is found
        self.assertIsNotNone(itemId, f"Item ID for product {new_data['productId']} not found in the cart")

        # Modify the item

        modify_cart = self.api_method.patch_by_cartId_ItemId(cartId, itemId, json=new_data)

        # Verify that the modification was successful
        actual_code = modify_cart.status_code
        expected_code = 204
        self.assertEqual(expected_code, actual_code, f"Modify item failed: Expected status code {expected_code}, but found Aactual status code: {actual_code}")

        # Get the updated cart after modification
        modified_cart = self.api_method.get_a_cart_by_cartId(cartId)
        modified_products = modified_cart.json()

        # Verify the quantity of the modified item
        for item in modified_products['items']:
            if item['productId'] == new_data['productId']:
                expected_quantity = new_data['quantity']
                actual_quantity = item['quantity']
                self.assertEqual(actual_quantity, expected_quantity, f"Tha quantity for product: {item['productId']} should be {expected_quantity}, but found {actual_quantity}")
            # Verify that other products were not modified
            else:
                found = False
                for original_item in initial_cart_state['items']:
                    if original_item['productId'] == item['productId']:
                        found = True
                        self.assertEqual(item['quantity'], original_item['quantity'], f"Product {item['productId']} quantity changed unexpectedly.")
                        break
                self.assertTrue(found, f"Product {item['productId']} not found in initial cart state.")

    def test04_replace_cartItem(self):
        # Create a new cart
        create_newCart = self.api_method.post_create_newCart()
        cartId = create_newCart.json()['cartId']
        product_to_add = self.api_method.post_add_items_to_cart_positive_entries()

        # add items to cart
        for product in product_to_add:
            response = self.api_method.post_add_product_in_Cart(cartId, json=product)

        # Retrieve the cart items
        get_cart_response = self.api_method.get_a_cart_by_cartId(cartId)
        cart_products = get_cart_response.json()

        # Store the initial state of the cart
        initial_cart_state = cart_products.copy()

        # Define the data for the item should be replaced and for the new one
        replace_old_item_data = {"productId": 4875, "quantity": 1}
        new_item_data = {"productId": 2585, "quantity": 2}

        # Find the itemId for the product to be replaced
        old_itemId = None
        for item in cart_products['items']:
            if item['productId'] == replace_old_item_data['productId']:
                old_itemId = item['id']
                break

        # Ensure that the itemId is found
        self.assertIsNotNone(old_itemId, f"Item ID for product {replace_old_item_data['productId']} not found in the cart")

        # Replace the item
        replace_item = self.api_method.put_by_cartId_ItemId(cartId, itemId=old_itemId, json=new_item_data)

        # Verify that the replacement was successful
        actual_code = replace_item.status_code
        expected_code = 204
        self.assertEqual(expected_code, actual_code, f"Replace item failed: Expected status code {expected_code}, but found Aactual status code: {actual_code}")

        # Get the updated cart after replacement
        modified_cart = self.api_method.get_a_cart_by_cartId(cartId)
        modified_products = modified_cart.json()

        # Verify the new item and other items in the cart
        new_item_found = False
        for item in modified_products['items']:
            if item['productId'] == new_item_data['productId']:
                expected_quantity = new_item_data['quantity']
                actual_quantity = item['quantity']
                self.assertEqual(actual_quantity, expected_quantity, f"Tha quantity for product: {item['productId']} should be {expected_quantity}, but found {actual_quantity}")
                new_item_found = True
            # Verify that other products were not modified
            else:
                found = False
                for original_item in initial_cart_state['items']:
                    if original_item['productId'] == item['productId']:
                        found = True
                        self.assertEqual(item['quantity'], original_item['quantity'], f"Product {item['productId']} quantity changed unexpectedly.")
                        break
                self.assertTrue(found, f"Product {item['productId']} not found in initial cart state.")

        # Ensure that the new item is present in the cart
        self.assertTrue(new_item_found, f"New item {new_item_data['productId']} not found in the cart")

        # Ensure that the old item is not present in the cart
        for item in modified_products['items']:
            old_item_productId = replace_old_item_data['productId']
            actual_item_productId = item['productId']
            self.assertNotEqual(actual_item_productId, old_item_productId, f"Old product {replace_old_item_data['productId']} should not be in the cart")

    def test05_delete_cartItem(self):
        # Create a new cart
        create_newCart = self.api_method.post_create_newCart()
        cartId = create_newCart.json()['cartId']
        product_to_add = self.api_method.post_add_items_to_cart_positive_entries()

        # add items to cart
        for product in product_to_add:
            response = self.api_method.post_add_product_in_Cart(cartId, json=product)

        # Retrieve the cart items
        get_cart_response = self.api_method.get_a_cart_by_cartId(cartId)
        cart_products = get_cart_response.json()

        # Store the initial state of the cart
        initial_cart_state = cart_products.copy()

        # Choose the item to be deleted
        delete_item_data = {"productId": 8554, "quantity": 3}

        # Find the itemId for the product to be deleted
        itemId = None
        for item in cart_products['items']:
            if item['productId'] == delete_item_data['productId']:
                itemId = item['id']
                break

        # Ensure that the itemId is found
        self.assertIsNotNone(itemId, f"Item ID for product {delete_item_data['productId']} not found in the cart")

        # Delete the item
        delete_item = self.api_method.delete_by_cartId_ItemId(cartId, itemId, json=delete_item_data)

        # Verify that the deletion was successful
        actual_code = delete_item.status_code
        expected_code = 204
        self.assertEqual(expected_code, actual_code, f"Delete item failed: Expected status code {expected_code}, but found Aactual status code: {actual_code}")

        # Get the updated cart after deletion
        modified_cart = self.api_method.get_a_cart_by_cartId(cartId)
        modified_products = modified_cart.json()

        # Verify that the deleted item is not present in the cart
        for item in modified_products['items']:
            if item['productId'] == delete_item_data['productId']:
                self.assertNotEqual(item['quantity'], delete_item_data['quantity'],
                                    f"Deleted product {delete_item_data['productId']} should not be in the cart")
            else:
                # Verify that other products in the cart remain unchanged
                found = False
                for original_item in initial_cart_state['items']:
                    if original_item['productId'] == item['productId']:
                        found = True
                        self.assertEqual(item['quantity'], original_item['quantity'],
                                         f"Product {item['productId']} quantity changed unexpectedly.")
                        break
                self.assertTrue(found, f"Product {item['productId']} not found in initial cart state.")

    def test06_negative_modify_cartItem_missing_parameters(self):
        # Attempt to modify an item in the cart with invalid cartId and ItemId/no json
        modify_response = self.api_method.patch_by_cartId_ItemId(cartId="invalidCartId", itemId="invalidItemId")

        # Verify that the response status code is 404 Not found
        expected_status = 404
        actual_status = modify_response.status_code

        self.assertEqual(actual_status, expected_status,f"Attempt to modify a cart item with invalid cartId and ItemId/no json. Expected status code {expected_status}. Actual: {actual_status}")

        # Verify that the response contains error message
        error_message = modify_response.json()['error']
        self.assertIn("No cart with id invalidCartId.", error_message, "Expected error message for The cart or the item could not be found in modify item request")

    def test07_negative_replace_cartItem_invalid_parameters(self):
        # Attempt to replace an item in the cart with invalid parameters
        replace_response = self.api_method.put_by_cartId_ItemId(cartId="invalidCartId", itemId="invalidItemId")

        # Verify that the response status code is 404 Not found
        expected_status = 404
        actual_status = replace_response.status_code
        self.assertEqual(actual_status, expected_status,
                         f"Expected status code {expected_status} for invalid parameters in The cart or the item could not be found in replace item request. Actual: {actual_status}")

        # Verify that the response contains an error message indicating invalid parameters
        error_message = replace_response.json()['error']
        self.assertIn("No cart with id invalidCartId", error_message,"Expected error message for The cart or the item could not be found in replace item request")

    def test08_negative_delete_cartItem_invalid_cartId(self):
        # Attempt to delete an item in the cart with an invalid cartId
        delete_response = self.api_method.delete_by_cartId_ItemId(cartId="invalidCartId", itemId="invalidItemId")

        # Verify that the response status code is 404 Not found
        expected_status = 404
        actual_status = delete_response.status_code
        self.assertEqual(actual_status, expected_status, f"Expected status code {expected_status} for The cart or the item could not be found in delete item request. Actual: {actual_status}")

        # Verify that the response contains an error message
        error_message = delete_response.json()['error']
        self.assertIn("No cart with id invalidCartId", error_message,
                      "Expected error message for iThe cart or the item could not be found in delete item request")
