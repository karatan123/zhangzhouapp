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

    #     封装函数判断某元素是否存在
    def is_notexist_element(self):
        searchelement = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView"
                         )
        massage = WebDriverWait(self.driver, 20, 0.1).until(EC.invisibility_of_element_located(searchelement))
        if massage == True:
            return True
        else:
            return False


    def test_personmangement_swip(self):
        view1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.LinearLayout[1]/android.widget.ImageView"
        )
        view1.click()
        time.sleep(5)
        TouchAction(self.driver).press(x=662, y=1770).wait(100).move_to(x=708, y=983).release().perform()
    #    获取toast    未捕捉到
        toast_loc1 = ("xpath", ".//*[contains(@text,'已是最后一页')]")
        massage1 = WebDriverWait(self.driver, 20, 0.0001).until(EC.presence_of_element_located(toast_loc1))
        self.assertEqual(massage1.text, '已是最后一页')

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
        self.assertTrue(self.is_notexist_element())



    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.driver.quit()
