# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:  demo
File Name   :  3.torch_grad.py
Description :  
Author      :  Steven.zou
E-mail      :  zoushiqi0404@gmail.com
Date        :  2022/9/25 23:00
Software    :  PyCharm
-------------------------------------------------
Change Activity:

-------------------------------------------------
"""
import numpy as np
from matplotlib_inline import backend_inline
import torch


def f(x):
    return 3 * x ** 2 - 4 * x


def numerical_lim(f, x, h):
    return (f(x + h) - f(x)) / h


if __name__ == '__main__':
    h = 0.1
    for i in range(5):
        print(f'h={h:.5f}, numerical limit={numerical_lim(f, 1, h):.5f}')
        h *= 0.1
