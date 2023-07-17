#!/usr/bin/env python
# encoding: utf-8
'''
  @project:pythonProject
  @author:xxl
  @contact:1755422946@qq.com
  @file:String1.py
  @time:2022/8/24 18:17
  @desc:
'''
a = "aaaaaa"
b = "bbbbbb"
c = f"cccccc{a}"
d = "dddddd{}"
e = "eeeeee{}{}"
f = "ffffff{x}{y}"
print(a + b)
print("aaaaaa" "bbbbbb")
print(c)
print(d.format(a))
print(e.format(a,b))
print(f.format(x=a,y=b))

