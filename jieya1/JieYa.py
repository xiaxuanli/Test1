#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:JieYa.py
  @time:2022/11/26 19:56
  @desc:
'''
import zipfile
import itertools

def JieYa(filename,password):
    try:
        with zipfile.ZipFile(filename) as zp:
            zp.extractall("./",pwd=password.encode("utf-8"))
        return True
    except:
        return False

filename="新建文本文档.rar"
chars="abcdefghijklmnopqrstuvwxyz0123456789"
for c in itertools.permutations(chars,4):
    password="".join(c)
    if JieYa(filename,password):
        print("解压成功!", password)
        break
    else:
        print("解压失败!", password)
        break
