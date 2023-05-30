#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:Urllib1.py
  @time:2022/9/2 17:31
  @desc:
'''
import urllib.request

response = urllib.request.urlopen("https://www.baidu.com")
# 获取状态信息
print(response.status)
# 获取response
print(response.read())
# 获取头信息
print(response.headers)