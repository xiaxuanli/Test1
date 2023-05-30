#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_allure_attach.py
  @time:2023/2/15 18:39
  @desc:
'''
import pytest
import allure

def test_attach_text():
    allure.attach("这是一段纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_body():
    allure.attach("<body>这是一段HTMLbody块</body>",name="HTML代码块",attachment_type=allure.attachment_type.HTML)

def test_attach_Picture():
    allure.attach.file("D:\PythonWork\Test\photo\伏尼契手稿_Page_006.jpg",attachment_type=allure.attachment_type.JPG,name="伏尼契手稿图片")

