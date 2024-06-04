from behave import *


@given('Navigate to the webpage')
def step_impl(context):
    context.brokenImages_page.navigate_to_the_url()


@when('The page is loaded')
def step_impl(context):
    context.brokenImages_page.wait_for_page_loading()


@then('Check if there are broken images')
def step_impl(context):
    brokenImages = context.brokenImages_page.check_for_broken_images()

    # expecting the list of broken images to be empty
    assert len(brokenImages) == 0, f"Broken images found: {brokenImages}"
