#!/usr/bin/env python
# encoding: utf-8
'''
  @project:pythonProject
  @author:xxl
  @contact:1755422946@qq.com
  @file:Sum.py
  @time:2022/8/25 14:23
  @desc:
'''
'''
1.计算1~100求和
2.加入分支结构实现1~100之间的偶数求和
3.使用Python实现1~100之间的偶数求和
'''

result = 0
for i in range(101):
    # print(i)
    result = result + i
print(result)


'''
3.使用Python实现1~100之间的偶数求和
'''
zu = 0
for i in range(2,101,2):
    # print(i)
    zu = zu + i
print(zu)
