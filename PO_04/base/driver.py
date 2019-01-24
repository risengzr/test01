from appium import webdriver

import page


def init_driver(appPackage, appActivity):
    desired_caps = {}
    desired_caps['platformName'] = "Android"
    desired_caps['platformVersion'] = "5.1"
    desired_caps['deviceName'] = "192.168.56.101:5555"
    desired_caps['appPackage'] = appPackage
    desired_caps['appActivity'] = appActivity
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
