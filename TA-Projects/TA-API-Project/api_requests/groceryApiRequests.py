import requests
import random
import string

# API documentation: https://github.com/vdespa/Postman-Complete-Guide-API-Testing/blob/main/simple-grocery-store-api.md

class GroceryStoreApi:
    # base url
    __BASE_URL = "https://simple-grocery-store-api.glitch.me"

    # endpoints
    __API_CLIENT = "/api-clients"
    __STATUS_ENDPOINT = "/status"
    __PRODUCTS_ENDPOINT = "/products"

    __CARTS_ENDPOINT = "/carts"
    __ORDERS_ENDPOINT = "/orders"
    __ITEMS_ENDPOINT = "/items"

    # ROUTES

    def __status_route(self):
        return self.__BASE_URL + self.__STATUS_ENDPOINT
    def __api_client_route(self):
        return self.__BASE_URL + self.__API_CLIENT

    def __products_route(self):
        return self.__BASE_URL + self.__PRODUCTS_ENDPOINT

    def __products_productId_route(self, productId):
        return self.__BASE_URL + self.__PRODUCTS_ENDPOINT + f'/{productId}'

    def __carts_route(self):
        return self.__BASE_URL + self.__CARTS_ENDPOINT

    def __carts_cartId_route(self, cartId):
        return self.__carts_route() + f'/{cartId}'

    def __carts_cartId_items_route(self, cartId):
        return self.__carts_cartId_route(cartId) + self.__ITEMS_ENDPOINT

    def __carts_cartId_items_itemId_route(self, cartId, itemId):
        return self.__carts_cartId_items_route(cartId) + f'/{itemId}'

    def __orders_route(self):
        return self.__BASE_URL + self.__ORDERS_ENDPOINT

    def __orders_orderId_route(self, orderId):
        return self.__orders_route() + f'/{orderId}'

    # REQUESTS METHODS
    # products
    def get_status(self):
        URL = self.__status_route()
        return requests.get(URL)
    def get_all_products(self):
        URL = self.__products_route()
        return requests.get(URL)

    def get_products_by_category(self, category):
        URL = self.__products_route()
        params = {'category': category}
        return requests.get(URL, params=params)

    def get_products_by_results(self, results):
        URL = self.__products_route()
        params = {'results': results}
        return requests.get(URL, params=params)

    def get_products_by_available(self, available):
        URL = self.__products_route()
        params = {'available': available}
        return requests.get(URL, params=params)

    def get_products_by_parameters(self, params):
        URL = self.__products_route()
        params = {}
        return requests.get(URL, params=params)

    # REQUESTS
    # cart

    def post_create_newCart(self):
        URL = self.__carts_route()
        return requests.post(URL)

    def post_add_product_in_Cart(self, cartId, json=None):
        URL = self.__carts_cartId_items_route(cartId)
        return requests.post(URL, json=json)

    def get_cart_items_by_cartId(self, cartId):
        URL = self.__carts_cartId_items_route(cartId)
        return requests.get(URL)

    def get_a_cart_by_cartId(self, cartId):
        URL = self.__carts_cartId_route(cartId)
        return requests.get(URL)

    def patch_by_cartId_ItemId(self, cartId, itemId, json=None):
        URL = self.__carts_cartId_items_itemId_route(cartId, itemId)
        return requests.patch(URL, json=json)

    def put_by_cartId_ItemId(self, cartId, itemId, json=None):
        URL = self.__carts_cartId_items_itemId_route(cartId, itemId)
        return requests.put(URL, json=json)

    def delete_by_cartId_ItemId(self, cartId, itemId, json=None):
        URL = self.__carts_cartId_items_itemId_route(cartId, itemId)
        return requests.delete(URL, json=json)

    # REQUESTS
    # orders & api
    def post_auth_and_get_token(self):
        URL = self.__api_client_route()

        random_string = ''.join(random.choices(string.ascii_letters, k=8))
        random_email = random_string + "@example.com"
        random_client_data = {
            "clientName": f"{random_string}",
            "clientEmail": f"{random_email}"
        }
        access_token = requests.post(URL, json=random_client_data).json()['accessToken']
        return access_token

    def set_up_auth_header(self, access_token):
        auth_header = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        return auth_header

    def get_orders(self, access_token):
        URL = self.__orders_route()
        auth_header = self.set_up_auth_header(access_token)
        return requests.get(URL, headers=auth_header)

    def get_an_order_by_orderId(self, access_token, orderId):
        URL= self.__orders_orderId_route(orderId)
        auth_header = self.set_up_auth_header(access_token)
        return requests.get(URL, headers=auth_header)

    def post_create_order(self, access_token, cartId, customerName, comment=None):
        URL = self.__orders_route()
        auth_header = self.set_up_auth_header(access_token)
        json_data = {
            "cartId": cartId,
            "customerName": customerName,
            "comment": comment
        }
        return requests.post(URL, headers=auth_header, json=json_data)

    def patch_an_order(self, access_token, orderId, customerName):
        URL = self.__orders_orderId_route(orderId)
        auth_header = self.set_up_auth_header(access_token)
        json_new_data = {
             "customerName": customerName
        }
        return requests.patch(URL, headers=auth_header, json=json_new_data)

    def delete_by_orderId(self, access_token, orderId):
        URL = self.__orders_orderId_route(orderId)
        auth_header = self.set_up_auth_header(access_token)
        return requests.delete(URL, headers=auth_header)

    # ENTRY DATA
    # products
    def get_products_by_category_positive_entries(self):
        category_positive_entries = [
            "meat-seafood",
            "fresh-produce",
            "candy",
            "bread-bakery",
            "dairy",
            "eggs",
            "coffee"
        ]
        responses = {category: self.get_products_by_category(category) for category in category_positive_entries}
        return responses

    def get_invalid_categories(self):
        invalid_categories = ['invalid', '@#$', 5, -1]
        responses = {category: self.get_products_by_category(category) for category in invalid_categories}
        return responses

    def get_products_by_results_positive_entries(self):
        valid_entries = [1, 2, 5, 10, 15, 19, 20]
        responses = {results: self.get_products_by_results(results) for results in valid_entries}
        return responses

    def get_invalid_results(self):
        invalid_entries = ['a', '@', -20, -1, 0, 21, 99]
        responses = {results: self.get_products_by_results(results) for results in invalid_entries}
        return responses

    def get_products_by_available_positive_entries(self):
        available_positive_values = ['true', 'false']
        responses = {available: self.get_products_by_available(available) for available in available_positive_values}
        return responses

    def get_invalid_available(self):
        invalid_available_values = ['invalid', '@#$', 5, -1]
        responses = {available: self.get_products_by_available(available) for available in invalid_available_values}
        return responses

    def get_invalid_parameters(self):
        return {
            'category': None,
            'john': 'smith',
            14: "%$^^"
        }

    # ENTRY DATA
    # carts

    def post_add_items_to_cart_positive_entries(self):

        # Add multiple items to the cart
        items_to_add = [
            {"productId": 4875, "quantity": 1},
            {"productId": 4641, "quantity": 2},
            {"productId": 8554, "quantity": 3}
        ]
        return items_to_add
