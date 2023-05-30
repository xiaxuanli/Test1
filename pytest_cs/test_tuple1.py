#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_tuple1.py
  @time:2022/12/5 17:51
  @desc:
'''
import pytest

class Test_Tuple1:
    @pytest.mark.parametrize(("a","b"),[(10,20),(10,21),(10,29)])
    def test_param(self,a,b):
        print(a + b)

if __name__ == '__main__':
    pytest.main()