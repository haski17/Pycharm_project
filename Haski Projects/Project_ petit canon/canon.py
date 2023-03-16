from tkinter import *
from math import pi, sin, cos

class Canon(object):
    """Petit canon graphique"""
    def __int__(self, boss, x, y):
        self.boss = boss
        self.x1, self.y1 = x, y
        self.lbu = 50
        self.x2, self.y2= x + self.lbu, y
        self.buse = boss.create_line(self.x1, )