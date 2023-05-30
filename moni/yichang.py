#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:yichang.py
  @time:2022/8/30 14:14
  @desc:
'''
try:
    a = int(input("请输入一个整数"))
    b = int(input("请输入一个整数"))
    print(a / b)
except:
    print("这是一个异常")
finally:
    print("程序结束")