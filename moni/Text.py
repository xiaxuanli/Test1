#!/usr/bin/env python
# encoding: utf-8
'''
  @project:pythonProject
  @author:xxl
  @contact:1755422946@qq.com
  @file:Text.py
  @time:2022/8/24 17:40
  @desc:
'''
#coding =utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
print(driver.title)
driver.quit()