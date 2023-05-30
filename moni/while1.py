#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:while1.py
  @time:2022/8/25 16:56
  @desc:
'''
"""
a = 0
while a < 5:
    a = a + 1
    print(a)
else:
    print(a)
"""

"""
1.猜数字
"""
import random
computer_number = random.randint(1,100)
while True:
    ren_number = int(input("请输入数字"))
    if ren_number > computer_number:
        print("猜的比实际大一点")
    elif ren_number < computer_number:
        print("猜的比实际小一点")
    else:
        print("猜对了")
        break



