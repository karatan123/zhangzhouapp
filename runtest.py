# coding=utf-8
'''
Created on 2018-11-14
@author: kara
Project:漳州手持机测试用例
'''
import unittest
import os
import time
from test_case import test_login
from test_case import test_personmanagement
from test_case import test_rfidmanagement
from test_case import test_customermanagement
from test_case import test_vehiclesmanagement


from HTMLTestRunner import HTMLTestRunner

# 报告存放路径
report_path = "/Users/kara/zhangzhouapp/report"
print(report_path)

#构造测试集
suite = unittest.TestSuite()
'''suite.addTest(test_login.LoginTest('test_login_success'))
suite.addTest(test_login.LoginTest('test_login_wrong_role'))
suite.addTest(test_login.LoginTest('test_login_error_password'))
suite.addTest(test_login.LoginTest('test_login_error_username'))
suite.addTest(test_personmanagement.PersonmanagementTest('test_personmanagement_existsearch'))
suite.addTest(test_personmanagement.PersonmanagementTest('test_personmanagement_notexistsearch'))
suite.addTest(test_vehiclesmanagement.VehiclesmanagementTest('test_vehiclesmanagement_existsearch'))
suite.addTest(test_vehiclesmanagement.VehiclesmanagementTest('test_vehiclemanagement_notexistsearch'))
suite.addTest(test_rfidmanagement.RfiddmanagementTest('test_rfidmanagement_notuse'))
suite.addTest(test_rfidmanagement.RfiddmanagementTest('test_rfidmanagement_use'))
suite.addTest(test_rfidmanagement.RfiddmanagementTest('test_rfidmanagement_invalidinput'))'''
suite.addTest(test_customermanagement.CustomermanagementTest('test_customermanagement_add'))
suite.addTest(test_customermanagement.CustomermanagementTest('test_customermanagement_existsearch'))
suite.addTest(test_customermanagement.CustomermanagementTest('test_customermanagement_edit_name'))
suite.addTest(test_customermanagement.CustomermanagementTest('test_customermanagement_edit_address'))
suite.addTest(test_customermanagement.CustomermanagementTest('test_customermanagement_edit_picture'))



if __name__=='__main__':
   now = time.strftime("%Y-%m-%d-%H-%M-%S")
   report_abspath = os.path.join(report_path,"result_"+now+".html")
   fp = open(report_abspath,"wb")
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告，测试结果如下：',description=u'用例执行情况：')
   runner.run(suite)