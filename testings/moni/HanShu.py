#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:HanShu.py
  @time:2022/8/28 16:47
  @desc:
'''
# 1.代码块
def method(a,b):
    c = a+b
    return c
print(method(5, 6))

# 2.元组传参
def methid(*a):
    return a[1]
print(methid(1, 2, 3, 4))


# 3.字典传参
def methed(**a):
    print(a.keys())
    print(a.values())
    print(a.items())
    print(a.get('a'))
    return
methed(a=1, b=2, c=3, d=4)


# 4.列表解包
list_a = [3,6]
print(list(range(*list_a)))

# 5.字典解包
def jiebao(a,b,c):
    print(a)
    print(b)
    print(c)
dect1 = {'a':1,'b':2,'c':3}
# 对键进行解包
jiebao(*dect1)
# 对值进行解包
jiebao(**dect1)

# lambda表达式
y = lambda x,y,z:x+y+z

print(y(1, 2, 3))

# 1.通过平方生成1，4，9
list_b = []
for i in range(1,4):
    list_b.append(i**2)
print(list_b)

list_c = [i**2 for i in range(1,4) if i!=1]
print('list_c',list_c)