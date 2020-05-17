# -*- coding = utf-8 -*-
# @Time : 2020/5/11 17:26
# @Author : AX
# @File : draw.py
# @Software: PyCharm
import tkinter as tk
import random


class lifeGame(object):
    # 定义alive二维数组用来保存状态 True生False死
    alive = []

    def __init__(self, count):
        # count为格子大小
        self.count = count
        self.random_alive()
        print(len(self.alive), len(self.alive[0]))

    def random_alive(self):
        self.alive = []
        for i in range(self.count // 10):
            # 二维化
            self.alive.append([])
            for j in range(self.count // 10):
                # 随机初始化，按照生存概率（当前为50）
                if i != 0 and j != 0 and i != self.count // 10 - 1 and j != self.count // 10 - 1 and random.randrange(0,100) >= 50:
                    self.alive[i].append(1)
                else:
                    self.alive[i].append(0)
        # print(self.alive)

    def init(self):
        # 创建tk
        self.window = tk.Tk()
        # 设置title
        self.window.title("生命游戏")
        # 设置窗口大小
        self.window.geometry(str(self.count * 2 + 200) + "x" + str(self.count * 2 + 200))
        # 创建canvas
        # 创建按钮
        button = tk.Button(self.window, text="游戏开始", command=self.refresh)
        button.pack(anchor='n', fill="y")
        button2 = tk.Button(self.window, text="游戏暂停", command=self.stop)
        button2.pack(anchor='n', fill="y")
        button3 = tk.Button(self.window, text="随机改变", command=self.reset)
        button3.pack(anchor='n', fill="y")
        self.canvas = tk.Canvas(self.window, width=2 * self.count, height=2 * self.count, bg="#fefefe")
        # 安装canvas
        self.canvas.pack()
        # 调用绘画函数
        self.draw()
        # 进入主界面（死循环）
        self.window.mainloop()

    def stop(self):
        self.canvas.after_cancel(self.cid)

    def reset(self):
        self.random_alive()
        self.draw()

    def alive_refresh(self):
        # 遍历进行判断，注意下标从1开始
        # print(len(self.alive),len(self.alive[1]))
        countI = len(self.alive) - 1
        for i in range(1, countI):
            countJ = len(self.alive[i]) - 1
            for j in range(1, countJ):
                # 计算和
                sum = self.alive[i][j - 1] + self.alive[i][j + 1] + self.alive[i - 1][j - 1] + self.alive[i - 1][j] + \
                      self.alive[i - 1][j + 1] + \
                      self.alive[i + 1][j - 1] + self.alive[i + 1][j] + self.alive[i + 1][j + 1]
                # 由死亡条件，列真值表进行逻辑电路分析 sum==3 sum==2 alive[][]==true
                if sum == 3 and self.alive[i][j] == False:
                    self.alive[i][j] = True
                elif self.alive[i][j] == True:
                    if sum < 2 or sum > 3:
                        self.alive[i][j] = False

    def draw(self):
        # canvas销毁再创建
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.window, width=2 * self.count, height=2 * self.count, bg="#fefefe")
        # 安装canvas
        self.canvas.pack()
        countI = len(self.alive)
        for i in range(countI):
            countJ = len(self.alive[i])
            for j in range(countJ):
                if self.alive[i][j] == 1:
                    self.canvas.create_rectangle(i * 20, j * 20, (i + 1) * 20, (j + 1) * 20, fill="red")
                else:
                    self.canvas.create_rectangle(i * 20, j * 20, (i + 1) * 20, (j + 1) * 20, fill="white")

    def refresh(self):
        # 更新二维数组
        self.alive_refresh()
        # 更新canvas
        self.draw()
        # 添加定时器
        self.cid = self.canvas.after(100, self.refresh)

x = lifeGame(300)
x.init()
