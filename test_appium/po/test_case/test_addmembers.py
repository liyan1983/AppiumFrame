#-*- conding:utf-8 -*-

from page.delete_member_page import DeletMember
from page.main_page import MainPage

_author_ = 'liy'
_data_ = '2021/3/1 7:50'


def test_add_memebers():
    MainPage().goto_homepage().goto_maillist().go_addmembers().add_members()

def test_delete_members():
    DeletMember().delete_member()