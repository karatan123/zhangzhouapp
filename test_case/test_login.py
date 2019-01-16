# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持端登录测试用例
'''
# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:登录LockerLife Web端测试用例
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# available since 2.12
from selenium.webdriver.support.ui import Select

import logging

from selenium import webdriver
import time
import unittest
from appium import webdriver
import os

class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'YDEQORZHB6OR8SMV'
        desired_caps['app'] = os.path.abspath('/Users/kara/Downloads/pda5.66.apk')
        desired_caps['appActivity'] = '.commissioner.auth.CommissionerLoginActivity'
        desired_caps['appPackage'] = 'com.locision.recycling'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 封装登录函数
    def login(self, username, password):
        # 进入专员登录页面
        self.driver.find_element_by_id("com.locision.recycling:id/et_username").send_keys(username)
        self.driver.find_element_by_id("com.locision.recycling:id/et_password").send_keys(password)
        self.driver.find_element_by_id("com.locision.recycling:id/btn_login").click()

    def test_login_success(self):
        # 进入专员登录页面
        self.login('zhangzhou1012','123456')
        # 截屏
        self.driver.get_screenshot_as_file("/Users/kara/zhangzhouapp/screenshot/login_success.jpg")
        # 获取toast
        toast_loc = ("xpath", ".//*[contains(@text,'登录成功')]")
        massage = WebDriverWait(self.driver, 20, 0.0001).until(EC.presence_of_element_located(toast_loc))
        self.assertEqual(massage.text, "登录成功")
        # 退出
        self.find_element_by_id("com.locision.recycling:id/btn_logout").click()
        time.sleep(5)

        # 获取toast
       # 缩小查询时间间隙，不然可能漏掉检测元素
        # driver:返回浏览器的一个实例，这个不用多说
        #
        # timeout：超时的总时长
        #
        # poll_frequency：循环去查询的间隙时间，默认0.5秒
    def test_login_wrong_role(self):
        self.login('zhangzhou1007', '123456')
        toast_loc1 = ("xpath", ".//*[contains(@text,'请求失败')]")

        massage1 = WebDriverWait(self.driver, 20, 0.0001).until(EC.presence_of_element_located(toast_loc1))
        self.assertEqual(massage1.text, "请求失败，请联系管理员")

    def test_login_error_password(self):
        self.login('zhangzhou1012', 'cxb37588')
        toast_loc2 = ("xpath", ".//*[contains(@text,'请求失败')]")
        massage2 = WebDriverWait(self.driver, 20, 0.0001).until(EC.presence_of_element_located(toast_loc2))
        self.assertEqual(massage2.text, "请求失败，请联系管理员")

    def test_login_error_username(self):
        self.login('kara', '123456')
        toast_loc3 = ("xpath", ".//*[contains(@text,'请求失败')]")
        massage3 = WebDriverWait(self.driver, 20, 0.0001).until(EC.presence_of_element_located(toast_loc3))
        self.assertEqual(massage3.text, "请求失败，请联系管理员")

    def tearDown(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.driver.quit()
