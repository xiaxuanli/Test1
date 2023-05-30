#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_demo.py
  @time:2022/9/10 11:31
  @desc:
'''
import pytest


class TestDemo():
    def test_one(self):
        print("开始执行 test_one 方法")
        x = "this"
        assert "h" in x

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
    pytest.main("-v -x TestDemo")
