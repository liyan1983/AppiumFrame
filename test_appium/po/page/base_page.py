#-*- conding:utf-8 -*-
import os

import yaml
from appium.webdriver.webdriver import WebDriver
from appium import webdriver
from page.exception_handle import exception_handle

_author_ = 'liy'
_data_ = '2021/2/28 14:13'



class BasePage:

    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):

        if driver is None:
            udid = Device.get_android_devices()[0]
            des_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:7555',
                'platformVersion': '6.0.1',
                'appPackage': 'com.tencent.wework',
                'appActivity': '.launch.WwMainActivity',
                'noRest': 'True',
                # 不停止应用，直接运行测试用例
                'dontStopAppOnReset': 'true',
                'waitForIdleTimeout': 0,
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)

        else:
            self.driver=driver
        self.driver.implicitly_wait(10)

    def data_path(self,name):
        path=(os.path.dirname(os.path.abspath('.')))+"\\data\\{0}.yaml".format(name)
        return path

    @exception_handle
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """

        if locator is None:
            # 如果传的元素是一个，只有 by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素是二个，既有 by ，又有 locator
            result = self.driver.find_element(by, locator)
        return result

    def parse_yaml(self,path,func_name):
        """
        取 yaml ，取出关键数据，用 parse 进行解析
        :param path:
        :return:
        """

        with open(path,encoding='utf-8') as f:
            data=yaml.load(f,Loader=yaml.FullLoader)
            self.parse(data[func_name])

    def parse(self,steps):
        """
        解析 yaml　内容
        :param steps:
        :return:
        """
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send_keys' == step['action']:
                self.find(step['by'],step['locator']).send_keys(step["content"])
            elif 'text' == step['action']:
                reality=self.find(step['by'],step['locator']).text
                print(reality)
                try:
                    assert reality==step['check_text']
                except Exception as e:
                    assert False ,"实际结果为%s,预期结果为%s" % (reality, step['check_text'])



