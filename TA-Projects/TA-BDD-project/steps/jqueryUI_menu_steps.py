import pdb

from behave import *


@given('Navigate to the JQuery Menu webpage')
def step_impl(context):
    context.jqueryUI_menu_page.navigate_to_jquery_webpage()


@when('Move the mouse cursor to Enable -> Downloads -> PDF')
def step_impl(context):
    context.jqueryUI_menu_page.move_cursor_to_downloads()


@when('Click on the first suboption "{sub_option}"')
def step_impl(context, sub_option):
    # take the sub_options map
    menu_options = context.jqueryUI_menu_page.menu_options_map()

    # check if is a valid sub_option
    assert sub_option in menu_options, f"You want to click on {sub_option} which is not in JQuery menu sub_options {menu_options}"

    # move mouse cursor
    context.jqueryUI_menu_page.move_mouse_cursor_to_file_type(sub_option)


@then('"{sub_option}" file named "{file_name}" is downloading')
def step_impl(context, sub_option, file_name):
    context.jqueryUI_menu_page.check_filename_type_click_save_file(file_name, sub_option)


@when('Move the mouse cursor to Enable -> Downloads -> CSV')
def step_impl(context):
    context.jqueryUI_menu_page.refresh_webpage()
    context.jqueryUI_menu_page.move_cursor_to_downloads()


@when('Click on the second suboption "{sub_option}"')
def step_impl(context, sub_option):
    # take the sub_options map
    menu_options = context.jqueryUI_menu_page.menu_options_map()

    # check if is a valid sub_option
    assert sub_option in menu_options, f"You want to click on {sub_option} which is not in JQuery menu sub_options {menu_options}"

    # move mouse cursor
    context.jqueryUI_menu_page.move_mouse_cursor_to_file_type(sub_option)


@then('"{sub_option}" file format: "{file_name}" is downloading')
def step_impl(context,sub_option, file_name):
    success, error_message = context.jqueryUI_menu_page.check_filename_type_click_save_file(file_name, sub_option)
    assert success, error_message

@when('Move the mouse cursor to Enable -> Downloads -> Excel')
def step_impl(context):
    context.jqueryUI_menu_page.refresh_webpage()
    context.jqueryUI_menu_page.move_cursor_to_downloads()


@when('Click on the third suboption "{sub_option}"')
def step_impl(context, sub_option):
    # take the sub_options map
    menu_options = context.jqueryUI_menu_page.menu_options_map()

    # check if is a valid sub_option
    assert sub_option in menu_options, f"You want to click on {sub_option} which is not in JQuery menu sub_options {menu_options}"

    # move mouse cursor
    context.jqueryUI_menu_page.move_mouse_cursor_to_file_type(sub_option)


@then('"{sub_option}" file named "{file_name}" is downloading in computer')
def step_impl(context, sub_option, file_name):
    success, error_message = context.jqueryUI_menu_page.check_filename_type_click_save_file(file_name, sub_option)
    assert success, error_message
