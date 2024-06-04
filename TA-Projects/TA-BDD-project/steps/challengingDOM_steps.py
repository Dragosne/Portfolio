from behave import *

# using a global variable to store canvas status for assertions
canvas_initial_status = None


# Finding elements from the table using different selectors
@given('Navigate to the Challenging DOM webpage')
def step_impl(context):
    context.challengingDOM_page.navigate_to_challengingDOM_webpage()


@then('I wish to find "{element_name}" element from the table using CSS and verify its text')
def step_impl(context, element_name):
    element_text = context.challengingDOM_page.select_element_and_get_text(element_name)
    assert element_name == element_text, f"We found element {element_text}: not the requested element: {element_name}"


@then('I wish to find "{element_name}" element from the table using CSS again and verify its text')
def step_impl(context, element_name):
    element_text = context.challengingDOM_page.select_element_and_get_text(element_name)
    assert element_name == element_text, f"We found element {element_text}: not the requested element: {element_name}"


@then('I wish to find "{element_name}" element from the table using absolute XPATH and verify its text')
def step_impl(context, element_name):
    element_text = context.challengingDOM_page.select_element_and_get_text(element_name)
    assert element_name == element_text, f"We found element {element_text}: not the requested element: {element_name}"


@then('I wish to find "{element_name}" element from the table using relative XPATH and verify its text')
def step_impl(context, element_name):
    element_text = context.challengingDOM_page.select_element_and_get_text(element_name)
    assert element_name == element_text, f"We found element {element_text}: not the requested element: {element_name}"


@then('I wish to find "{element_name}" element from the table using XPATH and verify its text')
def step_impl(context, element_name):
    element_text = context.challengingDOM_page.select_element_and_get_text(element_name)
    assert element_name == element_text, f"We found element {element_text}: not the requested element: {element_name}"


# Interact with the buttons and check if the canvas changed
@then('I check & store the canvas initial state')
def step_impl(context):
    # set the canvas initial status
    global canvas_initial_status
    canvas_initial_status = context.challengingDOM_page.canvas_status()


@when('I Click on the "{button_number}" button (blue)')
def step_impl(context, button_number):
    context.challengingDOM_page.click_button(button_number)


@then('I verify if the canvas changed after first action')
def step_impl(context):
    # use the initial state of the canvas
    global canvas_initial_status

    # check and store the canvas status after second click
    canvas_state_after_click = context.challengingDOM_page.canvas_status()

    # assertion: canvas initial status is not the same with the canvas status after first click
    assert canvas_initial_status != canvas_state_after_click, \
        f"Something went wrong, the canvas not changed after clicking on 1st button"

    # set the new canvas status after first click to initial status
    canvas_initial_status = canvas_state_after_click


@when('Click on the "{button_number}" button (red)')
def step_impl(context, button_number):
    context.challengingDOM_page.click_button(button_number)


@then('I verify if the canvas changed after second action')
def step_impl(context):
    # use the canvas status after first click
    global canvas_initial_status

    # check and store the canvas status after second click
    canvas_state_after_click = context.challengingDOM_page.canvas_status()

    # assertion: canvas status after first click is not the same with the canvas status after second click
    assert canvas_initial_status != canvas_state_after_click, \
        f"Something went wrong, the canvas not changed after clicking on 2nd button"

    # set the new canvas status after second click to initial status
    canvas_initial_status = canvas_state_after_click


@when('Click on the "{button_number}" button (green)')
def step_impl(context, button_number):
    context.challengingDOM_page.click_button(button_number)


@then('I verify if the canvas changed after third action')
def step_impl(context):
    # use the canvas status set after second click
    global canvas_initial_status

    # check and store the canvas status after third click
    canvas_state_after_click = context.challengingDOM_page.canvas_status()

    # assertion: canvas status after second click is not the same with the canvas status after third click
    assert canvas_initial_status != canvas_state_after_click, \
        f"Something went wrong, the canvas not changed after clicking on 3rd button"