#-*- conding:utf-8 -*-
from tkinter.tix import Shell

_author_ = 'liy'
_data_ = '2021/3/4 17:05'

class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o

