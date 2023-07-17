#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_pytest_yield.py
  @time:2022/9/12 23:26
  @desc:
'''
import pytest


# 作用域，module是在模块之前或之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield


    print("执行teardown!!!")
    print("最后关闭浏览器")


def test_search1(open):
    print("test_search1")
    raise NameError
    pass


def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

if __name__ == '__main__':
    pytest.main()

