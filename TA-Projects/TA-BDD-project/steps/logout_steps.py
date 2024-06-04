from behave import *
from steps.login_steps import *


@given('The user is logged in')
def step_login_to_account(context):
    # using login steps
    step_navigate_to_login_page(context)
    step_insert_username(context, "tomsmith")
    step_insert_password(context, "SuperSecretPassword!")
    step_click_login_button(context)


@when('The user clicks on the Logout button')
def step_click_logout_button(context):
    context.logout_page.click_logout()


@then('The text banner is displayed')
def step_logout_banner(context):
    assert context.logout_page.is_logout_message_displayed(), "The logout banner is not displayed"


@then('The displayed message is "{logout_message}"')
def step_logout_message(context, logout_message):
    message_received = context.logout_page.get_logout_message_text()
    assert logout_message in message_received, \
        f"Expected logout message: {logout_message} is not the same with the message received: {message_received}"


@then('The user is redirected to the "{page_name}"')
def step_is_redirected_to_login_page(context, page_name):
    page_name_found = context.logout_page.get_login_page_text()
    assert page_name in page_name_found, \
        (f"The user is not redirected to the Login Page: expected login pge name {page_name}. "
         f"Page name found: {page_name_found}")
