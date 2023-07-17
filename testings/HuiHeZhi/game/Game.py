#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:Game.py
  @time:2022/9/1 0:15
  @desc:
'''
class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("你赢了")
        elif final_hp < enemy_final_hp:
            print("你输了")
        else:
            print("平局")

