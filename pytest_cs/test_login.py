#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_login.py
  @time:2022/9/12 16:51
  @desc:
'''
import pytest


def test_case1(login):
    print("test_case1")
    pass


def test_case2():
    print("test_case2")
    pass


def test_case3(login):
    print("test_case3")
    pass


if __name__ == '__main__':
    pytest.main()
