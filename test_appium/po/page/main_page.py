#-*- conding:utf-8 -*-
from page.base_page import BasePage
from page.home_page import HomePage

_author_ = 'liy'
_data_ = '2021/3/4 14:28'


class MainPage(BasePage):

    def goto_homepage(self):
        """
        进入首页
        :return:
        """
        self.parse_yaml(self.data_path('goto_home'), 'goto_home')
        return HomePage(self.driver)
