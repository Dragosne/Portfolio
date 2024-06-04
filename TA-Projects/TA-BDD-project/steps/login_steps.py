from behave import *


@given('I am on the login page')
def step_navigate_to_login_page(context):
    context.login_page.navigate_to_page()


@when('I insert an username "{username}"')
def step_insert_username(context, username):
    context.login_page.set_email(username)


@when('I insert a password "{password}"')
def step_insert_password(context, password):
    context.login_page.set_password(password)


@when('I click on the login button')
def step_click_login_button(context):
    context.login_page.click_login()


@then('The "{message_pn}" banner is displayed')
def step_impl_banner(context, message_pn):
    assert context.login_page.is_message_displayed(), f"The {message_pn} banner is not displayed"


@then('The message is "{message}"')
def step_impl_message(context, message):
    assert message in context.login_page.get_message_text(), "Message is not the same"
