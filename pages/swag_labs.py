from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):

    def exist_icon(self, locator):
        try:
            self.find_element(locator='div.login.logo')
        except NoSuchElementException:
            return False
        return True
