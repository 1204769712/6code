from appium import webdriver

from weqyapp.pages.information_page import InformationPage


class App():
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = True
        caps["settings[waitForIdleTimeout]"] = 0
        caps["resetKeyboard"] = True
        caps["unicodeKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def goto_main(self):
        return InformationPage(self.driver)








