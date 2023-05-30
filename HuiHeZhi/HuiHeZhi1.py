#!/usr/bin/env python
# encoding: utf-8
'''
  @project:Test
  @author:xxl
  @contact:1755422946@qq.com
  @file:HuiHeZhi1.py
  @time:2022/8/31 22:50
  @desc:
'''
class Game:
    hp = 1000
    power = 200
    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("你赢了")
        elif final_hp < enemy_final_hp:
            print("你输了")
        else:
            print("平局")
game = Game()
game.fight(1000,300)



