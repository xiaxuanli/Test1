#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_mark_zidingyi.py
  @time:2022/9/15 16:04
  @desc:
'''
import pytest


@pytest.mark.login
def test_login1():
    print("test_login1")
    raise NameError
    pass


@pytest.mark.login
def test_login2():
    print("test_login2")
    pass


@pytest.mark.login
def test_login3():
    print("test_login3")
    pass


@pytest.mark.search
def test_search1():
    print("test_search1")
    pass


@pytest.mark.search
def test_search2():
    print("test_search2")
    pass


@pytest.mark.search
def test_search3():
    print("test_search3")
    pass


if __name__ == '__main__':
    pytest.main()
