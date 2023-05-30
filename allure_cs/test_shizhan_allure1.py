#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_shizhan.py
  @time:2023/2/15 20:32
  @desc:
'''

import allure
import time
import pytest
from selenium import webdriver

@allure.testcase("https://www.baidu.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):

    with allure.step("打开网页"):
        driver = webdriver.Chrome("D:\Programs\Python\Python37\Scripts\chromedriver.exe")
        driver.get("https://www.baidu.com")
        # 浏览器界面最大化
        driver.maximize_window()

    with allure.step(f"输入{test_data1}"):
        driver.find_element_by_id('kw').send_keys(test_data1)
        time.sleep(2)

    with allure.step("点击按钮"):
        driver.find_element_by_id('su').click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("D:\PythonWork\Test\photo\伏尼契手稿_Page_00111.jpg")
        allure.attach.file("D:\PythonWork\Test\photo\伏尼契手稿_Page_00111.jpg",attachment_type=allure.attachment_type.JPG)

    with allure.step("退出浏览器"):
        driver.quit()