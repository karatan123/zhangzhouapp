# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持端人员管理测试用例
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

class PersonmanagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = '0123456789ABCDEF'
        desired_caps['app'] = os.path.abspath('/Users/kara/Downloads/apps_1551929344465-zhangZhouRecycling3.4_release.apk')
        desired_caps['appActivity'] = '.commissioner.auth.CommissionerLoginActivity'
        desired_caps['appPackage'] = 'com.locision.recycling'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 进入专员登录页面

        self.driver.find_element_by_id("com.locision.recycling:id/et_username").send_keys("zhangzhou1012")
        self.driver.find_element_by_id("com.locision.recycling:id/et_password").send_keys("123456")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_login").click()
        time.sleep(5)
    #     进入人员管理页面
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        time.sleep(5)
        # 判断元素是否存在

    def isElementExist(self, css):
        try:
            self.driver.find_element_by_xpath(css)
            return True
        except:
            return False

    def test_personmanagement_existsearch(self):
        self.driver.find_element_by_id("com.locision.recycling:id/iv_search").click()
        searchinput = self.driver.find_element_by_id("com.locision.recycling:id/et_search")
        searchinput.send_keys("kara")
        time.sleep(5)
        result = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"
        )
        self.assertIn("kara", result.text)
        #     清除搜索框内容
        searchinput.clear()

    def test_personmanagement_notexistsearch(self):
        self.driver.find_element_by_id("com.locision.recycling:id/et_search").send_keys("12121")
    #     判断某个元素不存在
        self.assertFalse(self.isElementExist("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"))



    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.driver.quit()


# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()
