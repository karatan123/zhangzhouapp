# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持端标签卡管理测试用例
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
from appium.webdriver.common.touch_action import TouchAction

class RfiddmanagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = 'YDEQORZHB6OR8SMV'
        desired_caps['app'] = os.path.abspath('/Users/kara/Downloads/pda5.66.apk')
        desired_caps['appActivity'] = '.commissioner.auth.CommissionerLoginActivity'
        desired_caps['appPackage'] = 'com.locision.recycling'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 进入专员登录页面
        self.driver.find_element_by_id("com.locision.recycling:id/et_username").send_keys("zhangzhou1012")
        self.driver.find_element_by_id("com.locision.recycling:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_login").click()
        time.sleep(5)

    def test_rfidmanagement_notuse(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.LinearLayout[4]/android.widget.ImageView"
        ).click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/btn_input").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/et_content").send_keys("1206137545")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_ok").click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_id("com.locision.recycling:id/tv_content").text, u"未使用")

    def test_rfidmanagement_use(self):
    #返回标签卡输入
        self.driver.find_element_by_id("com.locision.recycling:id/tv_title").click()
        self.driver.find_element_by_id("com.locision.recycling:id/btn_input").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/et_content").send_keys("1206534649")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_ok").click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_id("com.locision.recycling:id/btn_go_bind_or_unbind").text, u"解除绑定")

    def test_rfidmanagement_invalidinput(self):
        # 返回标签卡输入
        self.driver.find_element_by_id("com.locision.recycling:id/tv_title").click()
        self.driver.find_element_by_id("com.locision.recycling:id/btn_input").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/et_content").send_keys("fdsjhfjskf")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_ok").click()
        time.sleep(2)
    #     捕捉toast
        toast_loc1 = ("xpath", ".//*[contains(@text,'只能输入数字！')]")
        massage1 = WebDriverWait(self.driver, 20, 0.0001).until(EC.presence_of_element_located(toast_loc1))
        self.assertEqual(massage1.text, "只能输入数字！")

    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.driver.quit()
