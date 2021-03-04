#-*- conding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage

_author_ = 'liy'
_data_ = '2021/3/1 7:55'


class DeletMember(BasePage):

    def delete_member(self):
        self.parse_yaml(self.data_path('goto_home'), 'goto_home')
        self.parse_yaml(self.data_path('delete_member'),'delete_member')





