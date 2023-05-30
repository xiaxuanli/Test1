#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:PyYaml1.py
  @time:2022/9/5 15:31
  @desc:
'''
import yaml

# 转换为列表
print(yaml.load("""
- aaaa
- bbbb
- cccc
- dddd
""", Loader=yaml.FullLoader))

# 转换为字典
print(yaml.load("""
a : 1
""", Loader=yaml.FullLoader))


# 打开文件获取
print(yaml.load(open("Test.yml"), Loader=yaml.FullLoader))
# 打开文件获取
print(yaml.load(open("Test1.yml"), Loader=yaml.FullLoader))
print(yaml.load(open("Test12.yml"), Loader=yaml.FullLoader))
print(yaml.load(open("Test3.yml"), Loader=yaml.FullLoader))

with open("Test4.yml","w") as f:
    yaml.dump(data={'a': [1, 2]},stream=f)

