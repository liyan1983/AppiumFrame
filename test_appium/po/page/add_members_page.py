#-*- conding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage

_author_ = 'liy'
_data_ = '2021/2/28 14:11'

class AddMembers(BasePage):

    def add_members(self):
        """
        添加成员页面
        :return:
        """
        result=self.parse_yaml(self.data_path('add_members'),'add_members')
        print(result)
        return result



