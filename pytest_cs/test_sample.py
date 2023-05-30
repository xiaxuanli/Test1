#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_sample.py
  @time:2022/9/10 10:25
  @desc:
'''
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5