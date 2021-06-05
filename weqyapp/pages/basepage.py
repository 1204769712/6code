import json
from typing import Dict, List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:

    _params = {}

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find_click(self,locator):
        try:
            self.find(locator).click()
        except Exception as e:
            print("----------元素查找点击失败-----------")

    def find(self,locator):
        try:
            return self.driver.find_element_by_xpath(locator)
        except Exception as e:
            print("----------元素查找失败-----------")

    def parse_action(self,path,func_name):
        with open(path,"r",encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[func_name]
        raw = json.dumps(steps)
        for key,value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find":
                self.find(step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "find_sendkeys":
                try:
                    # self.find(step["locator"]).send_keys(step["text"])
                    self.find_sendkeys(step["locator"],step["value"])
                except Exception as e:
                    print("查找元素输入失败")

    def swip_click(self, text):
        try:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().'
                                     'scrollable(true).instance(0)).'
                                     'scrollIntoView(new UiSelector().'
                                     f'text("{text}").instance(0));').click()
        except Exception as e:
            print("----------滑动点击失败----------")

    def find_sendkeys(self,locator,value):
        self.find(locator).send_keys(value)










