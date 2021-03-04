#-*- conding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from page.add_members_page import AddMembers
from page.base_page import BasePage

_author_ = 'liy'
_data_ = '2021/2/28 14:07'

class MailList(BasePage):

    def go_addmembers(self):
        """
        进入添加成员列表
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.parse_yaml(self.data_path('goto_addmember'), 'goto_addmemeber')
        return AddMembers(self.driver)


