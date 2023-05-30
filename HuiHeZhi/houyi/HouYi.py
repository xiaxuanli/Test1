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
from HuiHeZhi.game.Game import Game


class HouYi(Game):
    def __init__(self,defense):
        super().__init__(hp, power)
        self.defense = defense

    def houyi_fight(self, enemy_hp, enemy_power):
        final_hp = self.hp + self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("你赢了")
        elif final_hp < enemy_final_hp:
            print("你输了")
        else:
            print("平局")

# hp = 1000
# power = 200
hp = int(input("请输入hp"))
power = int(input("请输入power"))
defense = int(input("请输入defense"))

game = Game(hp,power)
houyi = HouYi(defense)
houyi.houyi_fight(1000,200)