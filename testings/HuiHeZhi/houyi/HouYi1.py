#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:HouYi.py
  @time:2022/9/1 0:14
  @desc:
'''
from testings.HuiHeZhi.game.Game import Game


class HouYi(Game):
    def __init__(self,defense):
        super().__init__(hp, power)
        self.defense = defense

    def houyi_fight(self, enemy_hp, enemy_power):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)
            if self.hp <= 0:
                print("你输了")
                break
            elif enemy_hp <= 0:
                print("敌人输了")
                break

# hp = 1000
# power = 200
hp = int(input("请输入hp"))
power = int(input("请输入power"))
defense = int(input("请输入defense"))

game = Game(hp,power)
houyi = HouYi(defense)
houyi.houyi_fight(1000,200)