from behave import *


# common step
@given('I am on the alerts page')
def step_impl(context):
    context.alerts_page.navigate_to_the_alerts_webpage()


# action steps for JS Alert
@when('I click on JS alert button')
def step_impl(context):
    context.alerts_page.click_on_JS_Alert_button()


@when('I accept the JS alert')
def step_impl(context):
    context.alerts_page.click_OK_on_JS_Alert_alert()


@then('The message on JavaScript Alerts page is "{message}"')
def step_impl(context, message):
    page_message = context.alerts_page.get_result_text()
    assert message in page_message, f'Message is not the same: expected {message} but found {page_message}'


# action steps for JS Confirm
@when('I click on JS confirm button')
def step_impl(context):
    context.alerts_page.click_on_JS_Confirm_button()


@when('I accept the JS confirm alert')
def step_impl(context):
    context.alerts_page.click_OK_on_JS_Confirm_alert()


@then('The message on JavaScript Alerts page if accept is "{message}"')
def step_impl(context, message):
    page_message = context.alerts_page.get_result_text()
    assert message in page_message, f'Message is not the same: expected {message} but found {page_message}'


@when('I click on JS confirm button again')
def step_impl(context):
    context.alerts_page.click_on_JS_Confirm_button()


@when('I am CANCEL the JS confirm alert')
def step_impl(context):
    context.alerts_page.click_CANCEL_on_JS_Confirm_alert()


@then('The message on JavaScript Alerts page if dismiss is "{message}"')
def step_impl(context, message):
    page_message = context.alerts_page.get_result_text()
    assert message in page_message, f'Message is not the same: expected {message} but found {page_message}'


# action steps for JS Prompt
@when('I click on the JS prompt button')
def step_impl(context):
    context.alerts_page.click_on_JS_Prompt_button()


@when('Input the text "JavaScript" in alert field')
def step_impl(context):
    context.alerts_page.input_text_in_JS_Prompt_field()


@when('I click OK on the JS Prompt alert')
def step_impl(context):
    context.alerts_page.click_OK_on_JS_Prompt_alert()


@then('The message on JavaScript Alerts page after the input is "{message}"')
def step_impl(context, message):
    page_message = context.alerts_page.get_result_text()
    assert message in page_message, f'Message is not the same: expected {message} but found {page_message}'


@when('I click on the JS prompt button again')
def step_impl(context):
    context.alerts_page.click_on_JS_Prompt_button()


@when('I am CANCEL the JS Prompt alert')
def step_impl(context):
    context.alerts_page.click_CANCEL_on_JS_Prompt_alert()


@then('The message on JavaScript Alerts page if cancel is "{message}"')
def step_impl(context, message):
    page_message = context.alerts_page.get_result_text()
    assert message in page_message, f'Message is not the same: expected {message} but found {page_message}'

