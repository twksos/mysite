from framework.utils.common_utils import by_css, CommonUtilities

LOCATOR = "locator"
BY = "by"

CLICK_ADD_NEW_PROGRAMMER_BUTTON_SCRIPT = '$("input#add_new_programmer").click()'
ADD_NEW_PROGRAMMER_INPUT = by_css('input#new_programmer_name')
ERROR_MESSAGE_LABEL = by_css('.message.error')
SUCCESS_MESSAGE_LABEL = by_css('.message.success')
PROGRAMMER_NAMES = by_css('.title-name')
CLICK_DELETE_BUTTON_SCRIPT = '$(".%s.delete").click()'
DELETE_ALL_PROGRAMMER_SCRIPT = '$(".delete").click()'
CLICK_DO_PAIR_SCRIPT = '$(".%s.%s.pair_time").click()'
PAIR_TIME = '.%s.%s.pair_time'

from pages.page import Page

class PairStairPage(Page):
    
    def get_add_button(self):
        return self.driver.find(ADD_NEW_PROGRAMMER_BUTTON)
    
    def _get_programmer_name_input(self):
        return self.driver.find_text_box(ADD_NEW_PROGRAMMER_INPUT)

    def add_programmer_with_name(self,programmer_name):
        self._get_programmer_name_input().enter_text(programmer_name)
        self.driver.execute_script(CLICK_ADD_NEW_PROGRAMMER_BUTTON_SCRIPT)
        
    def get_error_message(self):
        return self.driver.find(ERROR_MESSAGE_LABEL)

    def get_programmer_names(self):
        names=[]
        name_elements = self.driver.find_elements_(PROGRAMMER_NAMES)
        for name_element in name_elements:
            names.append(name_element.text)
        return names
    
    def delete_all_programmer(self):
        self.driver.execute_script(DELETE_ALL_PROGRAMMER_SCRIPT)

    def delete_with_name(self, programmer_name):
        self.driver.execute_script(CLICK_DELETE_BUTTON_SCRIPT % programmer_name)
        CommonUtilities(self.driver).wait_for_element(2,SUCCESS_MESSAGE_LABEL)

    def get_pair_time(self, programmer_0_name, programmer_1_name):
        return self.driver.find(by_css(PAIR_TIME % (programmer_0_name, programmer_1_name))).text

    def do_pair(self, programmer_0_name, programmer_1_name):
        self.driver.execute_script(CLICK_DO_PAIR_SCRIPT % (programmer_0_name,programmer_1_name))
        CommonUtilities(self.driver).wait_for_element(2,SUCCESS_MESSAGE_LABEL)


