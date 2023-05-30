#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_mark_parametrize.py
  @time:2022/9/12 23:54
  @desc:
'''
import pytest
import sys
import requests


# 参数化，前两个变量，后面是对应的数据
# "3+5"对应test_input，8对应expected
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7*5", 30)])
def test_eval(test_input, expected):
    #  eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected


# 参数组合
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x：{x},y:{y}")


# 方法名作为参数
test_users_data = ["Tom", "Jerry"]


@pytest.fixture(scope="module")
def login_r(request):
    # 接收并传入参数
    user = request.param
    print(f"\n打开首页准备登录，登录用户：{user}")
    return user

# 不确定是否正常，跳过不执行，并做出标记
@pytest.mark.xfail
# 添加跳过条件，不在。。。。执行
# @pytest.mark.skipif(sys.platform == "darwin", reason="不在MacOS上执行")
# @pytest.mark.skipif(sys.platform == "win32", reason="不在windows上执行")
# 本次不执行
# @pytest.mark.skip("跳过本次登录")
# indirect=True，可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r", test_users_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中的login返回值：{a}")
    assert a != ""


if __name__ == '__main__':
    pytest.main('-v')
