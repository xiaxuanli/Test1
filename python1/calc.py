#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:calc.py
  @time:2023/3/14 16:44
  @desc:
'''

# 加减乘除

class Calc():
    # 加
    def add(self,a:int,b:int):
        return a + b
    # 减
    def sub(self,a:int,b:int):
        return a - b
    # 乘
    def mul(self,a:int,b:int):
        return a * b
    # 除
    def div(self,a:int,b:int):
        if b != 0:
            return a / b
        else:
            return "被除数不能为0!!!"
