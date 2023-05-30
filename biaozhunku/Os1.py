#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:Os1.py
  @time:2022/9/2 17:32
  @desc:
'''
import os
# os.removedirs("Testdir")
print(os.listdir("../"))
if not os.path.exists("Testdir"):
    os.mkdir("Testdir")
if not os.path.exists("Testdir/Test.txt"):
    file1 = open("Testdir/Test.txt", "w")
    file1.write("Hi.Python")
    file1.close()