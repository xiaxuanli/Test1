#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:SheZhi.py
  @time:2022/11/26 20:03
  @desc:
'''

import os
import sys
import multiprocessing
import itertools
import time
from unrar import unrarlib
from unrar import rarfile

numbers = '1234567890'
lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
upperLetters = lowerLetters.upper()
symbols = '~!@#$%^&*()_-=+{}[]\\|;:\'",.<>/?`'
# 涉及到生成密码的参数
words = numbers  # +lowerLetters+upperLetters+symbols

filename = '新建文本文档.rar'
# filename = r'zh.rar'
File = rarfile.RarFile(filename)

index = 0


def append_on_file(password):
    # 把解析出的密码写入到文件中
    with open('password.txt', 'a', encoding='utf8') as f:
        text = password + '\n'
        f.write(text)


def get_password(min_digits, max_digits, words):
    """
    :param min_digits: 密码最小长度
    :param max_digits: 密码最大长度
    :param words: 密码可能涉及的字符
    :return: 密码生成器
    """
    while min_digits <= max_digits:
        pwds = itertools.product(words, repeat=min_digits)
        for pwd in pwds:
            yield ''.join(pwd)
        min_digits += 1


def extract(password):
    global index

    index = index + 1

    print(f"尝试第{index}次,密码:{password}")

    try:
        # 打开压缩文件,提供密码...
        File.extractall(pwd=password)
        # 破解到密码
        print("password is " + password)

        append_on_file(password)

        return True

    except Exception as e:
        # print(e)
        return False


class FoundException(Exception): pass


if __name__ == '__main__':
    start_time = time.time()
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    passwords = get_password(1, 6, words)  # 设置密码的长度1-4

    N = 11

    end_flag = 0

    try:
        while True:
            g2 = pool.imap(extract, itertools.islice(passwords, N))  # 对迭代器做切片操作
            if g2:
                for i in g2:
                    end_flag = 0
                    if i:
                        raise FoundException()
                else:
                    end_flag = end_flag + 1
                    if end_flag > 1:
                        break
            else:
                break
    except Exception as e:
        print(e)

    print("破解结束")
    end_time = time.time()
    change_time = end_time - start_time
    print("破解耗时：{}s".format(change_time))
