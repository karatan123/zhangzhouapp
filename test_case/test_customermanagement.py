# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持端收集点管理测试用例
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

class CustomermanagementTest(unittest.TestCase):
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

        # 重写获取toast方法
    def find_toast(self, message, timeout, poll_frequency):
        u'''获取toast信息文本并验证'''
        message1 = "//*[@text=\'{}\']".format(message)
        element = WebDriverWait(self.driver, timeout, poll_frequency).until(
            EC.presence_of_element_located((By.XPATH, message1)))
        return element.text


    def test_customermanagement_add(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.LinearLayout[3]/android.widget.ImageView"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_id("com.locision.recycling:id/btn_add").click()
        time.sleep(5)
        #收集点名称
        self.driver.find_element_by_id("com.locision.recycling:id/et_collection_name").send_keys(u"九龙烧味（桂城中学旁）")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_add_sub_collection_point").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/et_name").send_keys("miumiu")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_save").click()
        # 获取位置
        self.driver.find_element_by_id("com.locision.recycling:id/iv_location").click()
        time.sleep(5)
        self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/btn_sure").click()
        time.sleep(5)
        # 收集点类型
        self.driver.find_element_by_id("com.locision.recycling:id/btn_type").click()
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)
        # 收集点区域
        self.driver.find_element_by_id("com.locision.recycling:id/btn_area").click()
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.locision.recycling:id/btn_town").click()
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(5)

        # 上传图片
        self.driver.find_element_by_id("com.locision.recycling:id/iv_img").click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]"
        ).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[1]/android.widget.ImageView[2]"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_id("com.locision.recycling:id/done").click()
        time.sleep(5)

    #     提交收集点
        self.driver.find_element_by_id("com.locision.recycling:id/btn_save").click()
        time.sleep(2)
    #     捕获toast
        toasttext = self.find_toast(u'保存收运单位成功', 10, 0.01)
        self.assertEqual(toasttext, u"保存收运单位成功")
        time.sleep(2)

    def test_customermanagement_existsearch(self):
        self.driver.find_element_by_id("com.locision.recycling:id/iv_search").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.locision.recycling:id/et_search").send_keys(u"九龙")
        time.sleep(5)
        result = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
        )
        self.assertIn("九龙烧味", result.text)
    #    点击搜索项  为下一个测试做准备
        result.click()
        time.sleep(2)

    def test_customermanagement_edit_name(self):
        # 进入收集点编辑页面
        self.driver.find_element_by_id("com.locision.recycling:id/iv_search").click()
        time.sleep(5)
    #     修改广场点名及子收集点名
        collectionname = self.driver.find_element_by_id("com.locision.recycling:id/et_collection_name")
        collectionname.clear()
        collectionname.send_keys(u"德圣广场（桂城中学旁）")
        self.driver.find_element_by_id("com.locision.recycling:id/tv_sub_collection_point_name").click()
        time.sleep(5)
        subname = self.driver.find_element_by_id("com.locision.recycling:id/et_name")
        subname.clear()
        subname.send_keys(u"牛牛")
        self.driver.find_element_by_id("com.locision.recycling:id/btn_save").click()
        time.sleep(5)

        self.driver.find_element_by_id("com.locision.recycling:id/btn_save").click()
    #     捕捉toast
        toasttext = self.find_toast(u'修改收运单位成功', 10, 0.01)
        self.assertEqual(toasttext, u"修改收运单位成功")


    def test_customermanagement_edit_address(self):
        # 进入收集点编辑页面
        self.driver.find_element_by_id("com.locision.recycling:id/iv_search").click()
        time.sleep(5)
            #重新手动输入收集点地址
        customeraddress = self.driver.find_element_by_id("com.locision.recycling:id/et_address")
        customeraddress.clear()
        customeraddress.send_keys(u"广东省佛山市南海区丹灶祈福南湾半岛")

        self.driver.find_element_by_id("com.locision.recycling:id/btn_save").click()
        #     捕捉toast
        toasttext = self.find_toast(u'修改收运单位成功', 10, 0.01)
        self.assertEqual(toasttext, u"修改收运单位成功")

    def test_customermanagement_edit_picture(self):
        # 进入收集点编辑页面
        self.driver.find_element_by_id("com.locision.recycling:id/iv_search").click()
        time.sleep(5)
            # 修改收集点图片 上传5张
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.view.View/android.widget.LinearLayout[2]/android.widget.ImageView").click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]"
        ).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[2]/android.widget.ImageView[2]"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[3]/android.widget.ImageView[2]"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[4]/android.widget.ImageView[2]"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[5]/android.widget.ImageView[2]"
        ).click()
        time.sleep(2)
        self.driver.find_element_by_id("com.locision.recycling:id/done").click()
        time.sleep(5)

        #     提交收集点
        self.driver.find_element_by_id("com.locision.recycling:id/btn_save").click()
        time.sleep(2)
        #     捕获toast
        toasttext = self.find_toast(u'修改收运单位成功', 10, 0.01)
        self.assertEqual(toasttext, u"修改收运单位成功")
        time.sleep(2)





    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        print('自动测试完毕！')
        self.driver.quit()


# 运行单个python文件会需要
if __name__ == "__main__":
    unittest.main()