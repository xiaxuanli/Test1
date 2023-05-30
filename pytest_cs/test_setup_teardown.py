#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_setup_teardown.py
  @time:2022/9/10 11:58
  @desc:
'''
import pytest


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_login():
    print("这是外部方法 test_login")


class Test_demo():

    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup222222")

    def test_one(self):
        print("开始执行 test_one 方法")
        x = "this"
        assert "h" in x

    def teardown(self):
        print("teardown222222")



    def test_two(self):
        print("开始执行 test_two 方法")
        x = "hello"
        assert "e" in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    pytest.main("-v -s")
    # pytest.main(["-v -s", "test_setup_teardown.py"])
