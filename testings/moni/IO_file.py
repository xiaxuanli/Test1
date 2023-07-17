#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:IO_file.py
  @time:2022/8/29 18:01
  @desc:
'''
"""
f = open('Hello.py','rt')
print(f.read())
print(f.readable())
f.close()
"""

with open('Hello.py', 'rt') as f :
    print(f.read())