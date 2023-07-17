#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:Time1.py
  @time:2022/9/2 17:12
  @desc:
'''
import time

# 国外的时间格式
time1 = time.asctime()
print(time1)
# 时间戳
time2 = time.time()
print(time2)
# 时间戳转换为时间元组
time3 = time.localtime(time2)
print(time3)
# 将当前时间戳转成带格式的时间
# 例子：time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
# 当前时间两天前的时间
time4 = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime(time2-60*60*24*2))
print(time4)
