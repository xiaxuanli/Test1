#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_pytest.py
  @time:2023/3/14 16:54
  @desc:
'''
import pytest
from decimal import Decimal

from python1.calc import Calc

class TestCalc():

    def setup(self):
        self.cacl = Calc()

    def test_add_1(self):
        result = self.cacl.add(1,2)
        print(result)
        assert result == 3


if __name__ == '__main__':
    pytest.main(['-vs'])