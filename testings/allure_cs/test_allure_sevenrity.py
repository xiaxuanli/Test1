#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_allure_sevenrity.py
  @time:2023/2/15 17:27
  @desc:
'''
import allure
import pytest

def test_with_no_severity_label():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass




if __name__ == '__main__':
    pytest.main()














