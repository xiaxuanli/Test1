#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:conftest.py
  @time:2022/9/12 22:58
  @desc:
'''
import pytest


# 不带参数的fixture默认参数为 Scope=function
@pytest.fixture()
def login():
    print("这是一个登录方法")


def pytest_configure(config):
    # 标签名集合
    marker_list = ["search", "login"]
    # marker注册
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
