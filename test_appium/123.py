#-*- conding:utf-8 -*-
import os

_author_ = 'liy'
_data_ = '2021/3/4 16:26'

deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
readDeviceId = list(os.popen('adb devices').readlines())


print(deviceAndroidVersion,readDeviceId)