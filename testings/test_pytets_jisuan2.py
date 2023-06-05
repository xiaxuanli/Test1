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

    with open("./datas/add2.yml", "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        for n in data:
            list_data = n

    @pytest.mark.parametrize(["a", "b", "c"], list_data)
    def test_add2(self, a, b, c):
        result = self.cacl.add(a, b)
        assert result == c

    @pytest.mark.parametrize(["a", "b", "c"], list_data)
    def test_sub2(self, a, b, c):
        result = self.cacl.sub(a, b)
        assert result == c

    @pytest.mark.parametrize(["a", "b", "c"], list_data)
    def test_mul2(self, a, b, c):
        result = self.cacl.mul(a, b)
        assert result == c

    @pytest.mark.parametrize(["a", "b", "c"], list_data)
    def test_div2(self, a, b, c):
        result = self.cacl.div(a, b)
        assert result == c

if __name__ == '__main__':
    pytest.main(["-vs"])

