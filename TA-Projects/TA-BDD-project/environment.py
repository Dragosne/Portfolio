from driver import Driver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.checkboxes_page import CheckBoxes
from pages.alerts_page import AlertsPage
from pages.brokenImages_page import BrokenImages
from pages.dropdown_page import DropDown
from pages.drag_and_drop_page import DragDrop
from pages.challengingDOM_page import ChallengingDOM
from pages.jqueryUI_menu_page import JqueryMenu


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.logout_page = LogoutPage()
    context.checkboxes_page = CheckBoxes()
    context.alerts_page = AlertsPage()
    context.brokenImages_page = BrokenImages()
    context.dropdown_page = DropDown()
    context.drag_and_drop_page = DragDrop()
    context.challengingDOM_page = ChallengingDOM()
    context.jqueryUI_menu_page = JqueryMenu()


def after_all(context):
    context.browser.close()

