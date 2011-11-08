from framework.testsettings import WAIT

class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = self.driver.current_url
        self.driver.implicitly_wait(WAIT)

    def get_title(self):
        return self.driver.get_title()