# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from framework.drivers.firefox_driver_wrapper import FirefoxDriverWrapper
from framework.drivers.ie_driver_wrapper import IEDriverWrapper
from framework.drivers.chrome_driver_wrapper import ChromeDriverWrapper
from framework.drivers.remote_driver_wrapper import RemoteDriverWrapper


class DriverInitializer(object):
    @classmethod
    def initialize(cls, browser):
        """ Create Driver Wrapper"""
        print "Creating %s wrapper" % browser
        if browser == "firefox":
            cls.wrapper = FirefoxDriverWrapper()
        elif browser == "ie":
            cls.wrapper = IEDriverWrapper()
        elif browser == "chrome":
            cls.wrapper = ChromeDriverWrapper()
        elif browser == "htmlunit":
            cls.wrapper = RemoteDriverWrapper()
        return cls.wrapper.driver
