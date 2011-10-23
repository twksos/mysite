# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
import os

from framework.drivers.driver_initializer import DriverInitializer
import unittest
from framework.testsettings import WAIT, CLOSE_BROWSER_AFTER_TEST

class BaseTest(unittest.TestCase):
    def get_driver_name(self):
        driver_name = "firefox"
        if not os.system('which chromedriver > /dev/null'):
            driver_name = "chrome"
        print "*** Using Selenium Driver: %s ***" % driver_name
        return driver_name

    def setUp(self):
        self.driver = DriverInitializer.initialize(self.get_driver_name())
        self.driver.implicitly_wait(WAIT)
        self.driver.execute_script("window.innerWidth = screen.width;window.innerHeight = screen.height;window.screenX = 0;window.screenY = 0;alwaysLowered = false;")

    def tearDown(self):
        try:
            if CLOSE_BROWSER_AFTER_TEST:
                self.driver.quit()
        except TypeError as e:
            pass

if __name__ == "__main__":
    unittest.main()
