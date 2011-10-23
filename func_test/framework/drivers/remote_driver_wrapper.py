# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from selenium.webdriver.remote.webdriver import WebDriver
from framework.drivers.driver_wrapper import DriverWrapper


class RemoteDriverWrapper(WebDriver, DriverWrapper):
    def __init__(self, timeout=30):
        """ Create htmlunit Driver Wrapper"""
        WebDriver.__init__(self,
                           command_executor="http://127.0.0.1:4444/wd/hub",
                           browser_name="htmlunit")
        DriverWrapper.__init__(self)
