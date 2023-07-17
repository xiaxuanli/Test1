#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:requests1.py
  @time:2022/9/5 0:13
  @desc:
'''
import requests
res = requests.get("https://www.baidu.com")
# 获取网址状态码
print(res.status_code)
# 查看编码格式
print(res.encoding)
res.encoding='utf-8'
print(res.text)

r = requests.post("http://httpbin.org/post",data={'key':'value'})
print(r.text)