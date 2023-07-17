#!/usr/bin/env python
# encoding: utf-8
'''
  @author:xxl
  @contact: 
  @file: testadd.py
  @time: 2023/7/8 18:19
  @desc:
'''
import pytest
import yaml
from decimal import Decimal
from python1.calc import Calc

class testadd():

    def setup(self):
        self.cacl = Calc()


    with open("./datas/shuju.yml","r",encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)

    @pytest.mark.skip(reason="div_开头的方法不执行")
    @pytest.mark.parametrize(["a","b","c"],data)
    def div_1(self,a,b,c):
        result = self.cacl.div(a,b)
        assert result == c
        print("div_1")

    @pytest.mark.parametrize(["a", "b", "c"], data)
    def add_1(self,a,b,c):
        result = self.cacl.add(a,b)
        assert result == c
        print("add_1")

if __name__ == '__main__':
    pytest.main(['-vs','testadd.py::testadd::add_1'])
