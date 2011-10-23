# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
import random
import string
import time
from framework.exception import CouldNotLocateElementException

from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import datetime

__all__ = ['by_css', 'by_id', 'by_xpath', 'by_name']


class CommonUtilities(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)

    def wait_for_element(self, time_out_in_seconds, object_id):
        """Finds elements by their id by waiting till timeout."""

        current_time = datetime.datetime.now()
        end_time = current_time + datetime.timedelta(0, time_out_in_seconds)

        while current_time < end_time:
            try:
                self.driver.find(object_id)
                print "Object", object_id, "is present."
                break
            except NoSuchElementException:
                current_time = datetime.datetime.now()
        return self

    def find_text_box_by_id_and_enter_text(self, text_box_id, text_to_be_entered):
        self.driver.find_element_by_id(text_box_id).send_keys(text_to_be_entered)
        return self

    def find_text_box_by_name_and_enter_text(self, text_box_name, text_to_be_entered):
        self.driver.find_element_by_name(text_box_name).send_keys(text_to_be_entered)
        return self

    def find_text_box_by_css_and_enter_text(self, text_box_css, text_to_be_entered):
        self.driver.find_element_by_css_selector(text_box_css).send_keys(text_to_be_entered)
        return self

    def find_drop_down_by_id_and_select_option(self, drop_down_id,
                                               option_to_be_selected):
        self.driver.find_drop_down(drop_down_id).set_selected(option_to_be_selected)
        return self

    def find_drop_down_by_name_and_select_option(self, drop_down_name,
                                                 option_to_be_selected):
        self.driver.find_drop_down(drop_down_name).set_selected(option_to_be_selected)
        return self

    def find_element_and_click(self, element_id):
        self.driver.find_element_by_id(element_id).click()
        return self

    def is_element_present(self, element_locator):
        try:
            locator = self.driver.find(element_locator)
            return locator
        except CouldNotLocateElementException:
            return False


def get_random_three_digit_string():
    return''.join(random.choice(string.ascii_lowercase) for x in range(3))


def get_epoch_last_three_digit():
    epoch = long(time.time() * 100)
    epoch_last_three_digit = divmod(epoch, 1000)[1]
    while len(str(epoch_last_three_digit)) < 3:
        epoch_last_three_digit += 900
    return epoch_last_three_digit


def get_epoch_last_ten_digit():
    epoch = long(time.time() * 1000000)
    epoch_last_ten_digit = divmod(epoch, 10000000000)[1]
    while len(str(epoch_last_ten_digit)) < 10:
        epoch_last_ten_digit += 9000000000
    return epoch_last_ten_digit


def generateId():
    epoch_last_three_digit = get_epoch_last_three_digit()
    return str(epoch_last_three_digit) + get_random_three_digit_string()


# End of class and Starting of normal functions
def by_css(element_locator):
    """
    Function to create locator dictionary by css

    Args:
    element_locator is value of locator

    Return dictionary of locator e.g. {"locator":element_locator,"by":By.CSS_SELECTOR}
    """
    return {"locator": element_locator, "by": By.CSS_SELECTOR}


def by_id(element_locator):
    """
    Function to create locator dictionary by ID

    Args:
    element_locator is value of locator

    Return dictionary of locator e.g. {"locator":element_locator,"by":By.ID}
    """
    return {"locator": element_locator, "by": By.ID}


def by_xpath(element_locator):
    """
    Function to create locator dictionary by XPath

    Args:
    element_locator is value of locator

    Return dictionary of locator e.g. {"locator":element_locator,"by":By.XPATH}
    """
    return {"locator": element_locator, "by": By.XPATH}


def by_name(element_locator):
    """
    Function to create locator dictionary by Name

    Args:
    element_locator is value of locator

    Return dictionary of locator e.g. {"locator":element_locator,"by":By.NAME}
    """
    return {"locator": element_locator, "by": By.NAME}
