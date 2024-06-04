from behave import *


@given('Navigate to the Dropdown webpage')
def step_impl(context):
    context.dropdown_page.navigate_to_the_dropdown_page()


@when('Switch to first dropdown option by visible text "{option}"')
def step_impl(context, option):
    context.dropdown_page.switch_dropdown_to_option(option)


@then('After the first selection dropdown displays "{option}" and his value is "{state}"')
def step_impl(context, state, option):
    value = context.dropdown_page.get_dropdown_value()
    option_1_state = context.dropdown_page.check_dropdown_state().text
    assert value == state, f"Initial Dropdown state is {value} instead of {state}"
    assert option_1_state == option, f"The {option_1_state} is selected insted of {option}"


@when('Switch to second dropdown option by visible text "{option}"')
def step_impl(context, option):
    context.dropdown_page.switch_dropdown_to_option(option)


@then('After the second selection dropdown displays "{option}" and his value is "{state}"')
def step_impl(context, state, option):
    value = context.dropdown_page.get_dropdown_value()
    option_2_state = context.dropdown_page.check_dropdown_state().text
    assert value == state, f"Initial Dropdown state is {value} instead of {state}"
    assert option_2_state == option, f"The {option_2_state} is selected insted of {option}"

