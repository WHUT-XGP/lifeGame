# -*- coding:utf-8 -*-
# @Time : 2020/5/25 14:10
# @Author : AX
# @File : unitest.py
# @Software: PyCharm


"""
生命游戏单元测试.

copyright@AX
"""

# 导入生命游戏：

import drawlint
# 导入unittest
import unittest

# 定义结果
alive = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
# 第一次后结果
refresh_alive = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
# 第二次后结果
refresh_alive2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]


class TestAlive(unittest.TestCase):
    def testAlive(self):
        """
        循环检测初始值
        :return:
        """
        # 循环检测
        for i in range(len(x.get_alive())):
            for j in range(len(x.get_alive()[i])):
                self.assertEqual(alive[i][j], x.get_alive()[i][j])
        # 进行下一个测试
        x.alive_refresh()

    def testAliveRe1(self):
        """
         循环检测更新第一次后的值
         :return:
        """
        for i in range(len(x.get_alive())):
            for j in range(len(x.get_alive()[i])):
                self.assertEqual(refresh_alive[i][j], x.get_alive()[i][j])
        # 进行下一个测试
        x.alive_refresh()

    def testAliveRe3(self):
        """
        循环检测更新第二次后的值
        :return:
        """
        for i in range(len(x.get_alive())):
            for j in range(len(x.get_alive()[i])):
                self.assertEqual(refresh_alive2[i][j], x.get_alive()[i][j])


if __name__ == '__main__':
    x = drawlint.LifeGame(50)
    x.set_alive(alive)
    x.init()
    unittest.main()
