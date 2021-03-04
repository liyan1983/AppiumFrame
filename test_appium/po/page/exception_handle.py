#-*- conding:utf-8 -*-
import os

import allure
import yaml

_author_ = 'liy'
_data_ = '2021/3/3 13:37'


def exception_handle(func):
    def wrapper(*args,**kwargs):
        from page.base_page import BasePage
        instance: BasePage=args[0]
        try:
            result=func(*args,**kwargs)
            instance.error_num=0
            return result
        except Exception as e:
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png","rb") as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            if instance.error_num>instance.max_num:
                raise e
            instance.error_num+=1
            path=(os.path.dirname(os.path.abspath('.')))+"\\data\\alert_dispose.yaml"
            with open(path,encoding='utf-8') as f:
                data=yaml.load(f)
                for step in data['alert_displse']:
                    if step['text'] in instance.driver.page_source:
                        instance.driver.find_element(step['by'],step['locator']).click()
                        return wrapper(*args, **kwargs)

    return wrapper







