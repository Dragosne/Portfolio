from behave import *


@given('Navigate to the Drag&Drop webpage')
def step_impl(context):
    context.drag_and_drop_page.navigate_to_the_drag_and_drop_webpage()


@then('Initial state is: the source object is "{statusA}" and the target object is "{statusB}"')
def step_impl(context, statusA, statusB):
    statusA = context.drag_and_drop_page.source_element_state()
    statusB = context.drag_and_drop_page.target_element_state()
    assert statusA == "A", f"Status of source element after drag&drop is incorrect: {statusA}"
    assert statusB == "B", f"Status of target element after drag&drop is incorrect: {statusB}"


@when('First Action: Drag the source object A and drop it to the target object B')
def step_impl(context):
    context.drag_and_drop_page.drag_and_drop_action()


@then('Check status after first action: First object is "{statusB}" and second object is "{statusA}"')
def step_impl(context,statusA, statusB):
    statusA = context.drag_and_drop_page.source_element_state()
    statusB = context.drag_and_drop_page.target_element_state()
    assert statusA == "B", f"Status of source element after drag&drop is incorrect: {statusA}"
    assert statusB == "A", f"Status of target element after drag&drop is incorrect: {statusB}"


@when('Second action: Drag the source object B and drop it to the target object A')
def step_impl(context):
    context.drag_and_drop_page.drag_and_drop_action()


@then('Check status after second action: First object is "{statusA}" and second object is "{statusB}"')
def step_impl(context, statusA, statusB):
    statusA = context.drag_and_drop_page.source_element_state()
    statusB = context.drag_and_drop_page.target_element_state()
    assert statusA == "A", f"Status of source element after drag&drop is incorrect: {statusA}"
    assert statusB == "B", f"Status of target element after drag&drop is incorrect: {statusB}"

