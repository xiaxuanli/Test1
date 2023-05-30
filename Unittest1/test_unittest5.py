#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:Unittest2.py
  @time:2022/9/7 0:03
  @desc:
'''
import unittest

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner


class demo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUp Class1")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown Class")

    def setUp(self) -> None:
        print("setUp1")

    def tearDown(self) -> None:
        print("tearDown")

    def test_demo(self):
        print("test_demo")
        self.assertEqual(2, 2, "数据相等")

    def test_demo1(self):
        print("test_demo1")
        self.assertEqual(2, 2, "数据相等1")

    @unittest.skipIf(1 + 1 == 2, "跳过此demo2")
    def test_demo2(self):
        print("test_demo2")
        self.assertEqual(2, 3, "数据相等2")


class demo2(unittest.TestCase):
    def test_demo5(self):
        print("test_demo5")

    def test_demo6(self):
        print("test_demo6")


class demo3(unittest.TestCase):
    def test_demo7(self):
        print("test_demo7")

    def test_demo8(self):
        print("test_demo8")


if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_demo1"))
    # suite.addTest(demo2("test_demo6"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo3)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)

    dir = "./"
    discover = unittest.defaultTestLoader.discover(dir, 'test*.py')
    unittest.TextTestRunner().run(discover)

