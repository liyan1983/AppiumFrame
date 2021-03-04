#-*- conding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.mailist_page import MailList

_author_ = 'liy'
_data_ = '2021/2/28 14:03'

class HomePage(BasePage):

    def goto_information(self):
        pass

    def goto_maillist(self):
        """
        进入通讯录页面
        :return:
        """
        # self.driver.find_element(
        #     MobileBy.XPATH,'//*[@text="通讯录" and @resource-id="com.tencent.wework:id/dnh"]').click()
        self.parse_yaml(self.data_path('home_page'),'home_page')
        return MailList(self.driver)

    def goto_desk(self):
        pass

    def goto_my(self):
        pass




