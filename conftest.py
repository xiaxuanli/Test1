#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:conftest.py
  @time:2022/9/15 22:29
  @desc:
'''
import pytest
from datetime import datetime
from py.xml import html


# 编辑报告标题
def pytest_html_report_title(report):
    report.title = "My very own title!"


# 运行测试前修改环境信息
def pytest_configure(config):
    config._metadata["foo"] = "bar"


# # 运行测试后修改环境信息
# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     session.config._metadata["foo"] = "bar"


# 编辑摘要信息
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("foo: bar")])


# 测试结果表格
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()
