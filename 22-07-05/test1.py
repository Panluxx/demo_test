# -*- coding: utf-8 -*-
# @Time     : 2022/7/5 21:23
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test1.py
# Software  : PyCharm


class Game(object):

    def __init__(self, hp=1000, power=200):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):
        my_final_hb = self.hp - enemy_power
        enemy_final_hb = enemy_hp - self.power
        print(f'{my_final_hb} : {enemy_final_hb}')
        if my_final_hb > enemy_final_hb:
            print('我赢了')
        elif my_final_hb < enemy_final_hb:
            print('你赢了')
        else:
            print('两个煞笔')


class HouYi(Game):

    def __init__(self, defense):
        # defense:护甲
        super(HouYi, self).__init__()
        self.defense = defense

    def hou_yi_fight(self, enemy_hp, enemy_power):
        my_final_hb = self.hp + self.defense - enemy_power
        enemy_final_hb = enemy_hp - self.power
        print(f'{my_final_hb} : {enemy_final_hb}')
        if my_final_hb > enemy_final_hb:
            print('我赢了')
        elif my_final_hb < enemy_final_hb:
            print('你赢了')
        else:
            print('两个煞笔,平局了')


hou_yi = HouYi(100)
hou_yi.hou_yi_fight(200, 300)
