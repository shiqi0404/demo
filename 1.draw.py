# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:  demo
File Name   :  1.draw.py
Description :  
Author      :  Steven.zou
E-mail      :  zoushiqi0404@gmail.com
Date        :  2022/9/22 15:30
Software    :  PyCharm
-------------------------------------------------
 Change Activity:
 
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
colors = np.array(["red", "green", "black", "orange", "purple", "beige", "cyan", "magenta"])

plt.scatter(x, y, c=colors)
plt.show()
