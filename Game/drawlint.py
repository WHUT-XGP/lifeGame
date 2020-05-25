# -*- coding = utf-8 -*-
# @Time : 2020/5/11 17:26
# @Author : AX
# @File : draw.py
# @Software: PyCharm

"""
生命游戏.

copyright@AX
"""

import tkinter as tk
import random


# 生命游戏类
class LifeGame:
    """
    LifeGame：extend from object.
    Args: count used by init to tell the class how the

    Canvas's size
    """

    # 定义alive二维数组用来保存状态 True生False死
    alive = []
    count = 0
    window = None
    canvas = None
    cid = None

    # 构造函数
    def __init__(self, count):

        """
        :argument count.
        Init：extend from object

        Args: tell the class how size is
        """

        # count为格子大小
        self.count = count
        self.random_alive()
        print(len(self.alive), len(self.alive[0]))

    # random_alive:随机初始化数组
    def random_alive(self):

        """
        Randow_alive.

        Make the alive array has its initial num
        """

        self.alive = []
        for i in range(self.count // 10):
            # 二维化
            self.alive.append([])
            for j in range(self.count // 10):
                # 随机初始化，按照生存概率（当前为50）
                if i != 0 and j != 0 and i != self.count \
                        // 10 - 1 and j != self.count // 10 \
                        - 1 and random.randrange(100) >= 50:
                    self.alive[i].append(1)
                else:
                    self.alive[i].append(0)
        # print(self.alive)

    # init:初始化绘制
    def init(self):

        """
        :argument:self.
        :return: None

        :keyword:use it to draw
        """

        # 创建tk
        self.window = tk.Tk()
        # 设置title
        self.window.title("生命游戏")
        # 设置窗口大小
        self.window.geometry(str(self.count * 2 + 200)
                             + "x" + str(self.count * 2 + 200))
        # 创建canvas
        # 创建按钮
        button = tk.Button(self.window, text="游戏开始", command=self.refresh)
        button.pack(anchor='n', fill="y")
        button2 = tk.Button(self.window, text="游戏暂停", command=self.stop)
        button2.pack(anchor='n', fill="y")
        button3 = tk.Button(self.window, text="随机改变", command=self.reset)
        button3.pack(anchor='n', fill="y")
        self.canvas = tk.Canvas(self.window,
                                width=2 * self.count, height=2 * self.count,
                                bg="#fefefe")
        # 安装canvas
        self.canvas.pack()
        # 调用绘画函数
        self.draw()
        # 进入主界面（死循环）
        self.window.mainloop()

    # 停止运动
    def stop(self):

        """
                :argument:self.
                :return: None
                Make the canvas stop

                Cancel the time Intervals
        """

        self.canvas.after_cancel(self.cid)

    # 重新进行随机和绘制
    def reset(self):

        """
           To reset the alive
        """

        self.random_alive()
        self.draw()

    def set_alive(self, alive):

        """
        set the array of alive by hand operation.

        :param alive:
        :return: None
        """
        self.alive = alive

    def get_alive(self):

        """
        get the self.alive.

        :return: self.alive
        """
        return self.alive

    def alive_refresh(self):

        """
        Make the alive array refresh.

        :return
        """

        # 遍历进行判断，注意下标从1开始
        # print(len(self.alive),len(self.alive[1]))
        count_i = len(self.alive) - 1
        for i in range(1, count_i):
            count_j = len(self.alive[i]) - 1
            for j in range(1, count_j):
                # 计算和
                ans_sum = self.alive[i][j - 1] + self.alive[i][j + 1] \
                          + self.alive[i - 1][j - 1] + self.alive[i - 1][j] + \
                          self.alive[i - 1][j + 1] + \
                          self.alive[i + 1][j - 1] + \
                          self.alive[i + 1][j] + self.alive[i + 1][j + 1]
                # 由死亡条件，列真值表进行逻辑电路分析 ans_sum==3 ans_sum==2 alive[][]==true
                if ans_sum == 3 and not self.alive[i][j]:
                    self.alive[i][j] = 1
                elif self.alive[i][j]:
                    if ans_sum < 2 or ans_sum > 3:
                        self.alive[i][j] = 0

    def draw(self):

        """
        Use it to refresh the draw.

        :return:
        """

        # canvas销毁再创建
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.window, width=2 * self.count,
                                height=2 * self.count, bg="#fefefe")
        # 安装canvas
        self.canvas.pack()
        count_i = len(self.alive)
        for i in range(count_i):
            count_j = len(self.alive[i])
            for j in range(count_j):
                if self.alive[i][j] == 1:
                    self.canvas.create_rectangle(i * 20, j * 20,
                                                 (i + 1)
                                                 * 20,
                                                 (j + 1) * 20, fill="red")
                else:
                    self.canvas.create_rectangle(i * 20, j * 20,
                                                 (i + 1) *
                                                 20,
                                                 (j + 1) * 20, fill="white")

    def refresh(self):

        """
        To refresh the alive and canvas.

        :return:
        """
        print(self.alive)
        # 更新二维数组
        self.alive_refresh()
        print(self.alive)
        # 更新canvas
        self.draw()
        # 添加定时器
        self.cid = self.canvas.after(100, self.refresh)


if __name__ == '__main__':
    x = LifeGame(300)
    x.init()
