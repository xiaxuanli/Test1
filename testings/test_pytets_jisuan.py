#!/usr/bin/env python
# encoding: utf-8
'''
  @author:xxl
  @contact: 
  @file: test_pytets_jisuan.py
  @time: 2023/6/5 13:17
  @desc:
'''

import pytest

from decimal import Decimal

import yaml

from python1.calc import Calc


class TestCalc1():

    def setup(self):
        self.cacl = Calc()


    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./datas/add1.yml")))
    def test_add1(self,a,b,c):
        print(a)
        print(b)
        print(c)
        result = self.cacl.add(a,b)
        print(result)
        assert result == c


if __name__ == '__main__':
    pytest.main(['-vs'])
