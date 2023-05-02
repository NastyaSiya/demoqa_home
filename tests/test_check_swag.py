from pages.swag_labs import SwagLabs


def search_icon(browser):
    swag_check_page = SwagLabs(browser)
    swag_check_page.visit()
    assert swag_check_page.exist_icon()
    assert swag_check_page.find_element('#user-name')
    assert swag_check_page.find_element('#password')

