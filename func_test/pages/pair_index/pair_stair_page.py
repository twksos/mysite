from framework.utils.common_utils import by_css

LOCATOR = "locator"
BY = "by"

ADD_NEW_PROGRAMMER_BUTTON = by_css('button#add_new_programmer')

from pages.page import Page

class PairStairPage(Page):

    def get_button_text(self):
        return self.driver.find(ADD_NEW_PROGRAMMER_BUTTON).text