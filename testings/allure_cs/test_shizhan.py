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

@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):
    driver = webdriver.Chrome('D:\soft\cs\chromedriver_win32\chromedriver.exe')
    driver.get("https://www.baidu.com")

    driver.find_element_by_id('kw').send_keys(test_data1)
    time.sleep(2)

    driver.find_element_by_id('su').click()
    time.sleep(2)

    driver.save_screenshot("D:\PythonWork\Test1\photo1\伏尼契手稿_Page_00111.jpg")
    driver.quit()