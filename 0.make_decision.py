# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:  demo
File Name   :  0.make_decision.py
Description :  一个做决定的小 demo
Author      :  Steven.zou
E-mail      :  zoushiqi0404@gmail.com
Date        :  2022/9/22 11:19
Software    :  PyCharm
-------------------------------------------------
 Change Activity:

-------------------------------------------------
"""


import numpy as np


def print_answer1(c):
    if 0 < c <= 50:
        print("Go outside!")
    else:
        print("Dining room!")


def print_answer2(a):
    if 0 < a <= 25:
        print("Final answer is: 烧烤!")
    elif 25 < a <= 75:
        print("Final answer is: 猪肚鸡")
    else:
        print("Final answer is: 海底捞!")


def enter_print(b):
    print("Ok, Random Val is: ", b)
    return b


if __name__ == '__main__':
    c1 = np.random.randint(low=0, high=100, size=(1, 1))
    print_answer1(c1)
    if c1 <= 50:
        loop_val = np.linspace(1, 100, 100)
        for epoch_val in loop_val:
            print("Current epoch ==========>", epoch_val)
            a1 = np.random.randint(low=0, high=100, size=(1, 1))
            b1 = enter_print(a1[0])
            print_answer2(b1)
    else:
        print("Enjoy school life!")
