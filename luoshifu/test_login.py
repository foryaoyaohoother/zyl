# -*- coding: utf-8 -*-
# @Time    : 2023-02-06 20:04
# @Email   : foryaoyaoho@163.com
# @File    : test_01.py.py
# @Software: PyCharm
import pytest
from selenium import webdriver
import allure
class Test(object):
    def test_login(self,browser):
        with allure.step("step1：打开登录首页"):
            browser.get("https://blog.csdn.net/kami_ochin_akane/article/details/109681523")

        # 故意断言失败，看是否会截图
        assert browser.title == "悠悠"


if __name__ == '__main__':
    import os
    pytest.main(['test_login.py', '-s', '--alluredir', '../outfiles/report/tmp', '--clean-alluredir'])
    os.system('allure serve ../outfiles/report/tmp')








