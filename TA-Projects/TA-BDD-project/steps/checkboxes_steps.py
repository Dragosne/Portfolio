from behave import *


@given('Navigate to the Checkboxes webpage')
def step_navigate_to_checkboxes_page(context):
    context.checkboxes_page.navigate_to_checkboxes_page()


# expected initial state: checkbox1: not selected, checkbox2: selected
@then('Check the initial state of the Checkboxes')
def step_initial_state(context):
    checkbox_1_state = context.checkboxes_page.is_checkbox_1_selected()
    checkbox_2_state = context.checkboxes_page.is_checkbox_2_selected()
    assert checkbox_1_state is False, "Checkbox 1 IS selected at the beginning of the test"
    assert checkbox_2_state is True, "Checkbox 2 IS NOT selected at the beginning of the test"


@when('Click on the Checkbox_1')
def step_click_on_checkbox_1(context):
    context.checkboxes_page.click_checkbox_1()


# expected state: checkbox1: selected, checkbox2: selected
@then('Check the Checkboxes state after clicking on Checkbox_1')
def step_intermediary_state1(context):
    checkbox_1_state = context.checkboxes_page.is_checkbox_1_selected()
    checkbox_2_state = context.checkboxes_page.is_checkbox_2_selected()
    assert checkbox_1_state is True, "Checkbox 1 IS NOT selected after clicking on first checkbox"
    assert checkbox_2_state is True, "Checkbox 2 IS NOT selected after clicking on first checkbox"


@when('Click on the Checkbox_2')
def step_click_on_checkbox_2(context):
    context.checkboxes_page.click_checkbox_2()


# expected state: checkbox1: selected, checkbox2: not selected
@then('Check the Checkboxes state after clicking on Checkbox_2')
def step_intermediary_state2(context):
    checkbox_1_state = context.checkboxes_page.is_checkbox_1_selected()
    checkbox_2_state = context.checkboxes_page.is_checkbox_2_selected()
    assert checkbox_1_state is True, "Checkbox 1 IS NOT selected after clicking on second checkbox"
    assert checkbox_2_state is False, "Checkbox 2 IS selected after clicking on second checkbox"


@when('Click on both Checkboxes')
def step_click_on_both_checkboxes(context):
    context.checkboxes_page.click_checkbox_1()
    context.checkboxes_page.click_checkbox_2()


# expected state: checkbox1: not selected, checkbox2: selected
@then('Check the Checkboxes state after clicking on both Checkboxes')
def step_final_state(context):
    checkbox_1_state = context.checkboxes_page.is_checkbox_1_selected()
    checkbox_2_state = context.checkboxes_page.is_checkbox_2_selected()
    assert checkbox_1_state is False, "Checkbox 1 IS selected after clicking on both checkbox"
    assert checkbox_2_state is True, "Checkbox 2 IS NOT selected after clicking on both checkbox"
