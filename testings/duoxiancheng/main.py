#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:main.py
  @time:2022/9/4 17:12
  @desc:
'''
import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


class MyThread(threading.Thread):
    # func为函数
    def __init__(self, func, args, name=''):
        # 主动调Thread构造方法
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


# nloop哪一个
# nsec休眠多少秒
def loop(nloop, nsec):
    logging.info(" start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info(" end loop " + str(nloop) + " at " + ctime())


def main():
    logging.info(" start all at " + ctime())
    threads = []
    # 查看loops长度
    nloops = range(len(loops))
    # 实例化线程对象
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    # 启动线程
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info(" end all at " + ctime())


if __name__ == "__main__":
    main()
