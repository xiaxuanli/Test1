#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:test_unittest2.py
  @time:2022/9/8 21:59
  @desc:
'''
import unittest


class Cs(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_demo(self):
        print("test_demo")
        self.assertEqual(2, 2, "数据相等")

    def test_demo1(self):
        print("test_demo1")
        self.assertEqual(1, 1, "数据相等")

    @unittest.skipIf(1 + 1 == 2, "跳过此demo2")
    def test_demo2(self):
        print("test_demo2")
        self.assertEqual(3, 3, "数据相等")


class Cs2(unittest.TestCase):
    def test_demo22(self):
        print("test_demo22")

    def test_demo21(self):
        print("test_demo21")


if __name__ == '__main__':
    unittest.main()
