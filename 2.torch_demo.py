# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:  demo
File Name   :  2.torch_demo.py
Description :  首先，我们介绍n维数组，也称为张量（tensor）。 使用过Python中NumPy计算包的读者会对本部分很熟悉。
               无论使用哪个深度学习框架，它的张量类（在MXNet中为ndarray， 在PyTorch和TensorFlow中为Tensor）
               都与Numpy的ndarray类似。 但深度学习框架又比Numpy的ndarray多一些重要功能：
               首先，GPU很好地支持加速计算，而NumPy仅支持CPU计算；
               其次，张量类支持自动微分。 这些功能使得张量类更适合深度学习。
Author      :  Steven.zou
E-mail      :  zoushiqi0404@gmail.com
Date        :  2022/9/25 21:24
Software    :  PyCharm
-------------------------------------------------
Change Activity:

-------------------------------------------------
"""
import torch

# 2.1 入门
x = torch.arange(12)
print("x:", x)

print("X.shape:", x.shape)
print("x.numel():", x.numel())

X = x.reshape(3, 4)
print("X:", X)

x_zeros = torch.zeros((2, 3, 4))
print("x_zeros:", x_zeros)

x_ones = torch.ones((2, 3, 4))
print("x_ones:", x_ones)

x_rand = torch.randn(3, 4)
print("x_randn:", x_rand)

x_def = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print("x_def:", x_def)

# 2.2 运算符
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print("x:", x, "y:", y)
print("+:", x + y)
print("-:", x - y)
print("*", x * y)
print("/", x / y)
print("^", x ** y)
print("exp:", torch.exp(x))

X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print("cat_dim=0:", torch.cat((X, Y), dim=0))
print("cat_dim=1:", torch.cat((X, Y), dim=1))

print("logic1:", X == Y)
print("logic2:", X < Y)
print("logic3:", X > Y)

# 2.3 广播机制
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print("a:", a)
print("b:", b)
print("a+b:", a + b)

# 2.4 索引和切片
print("X[-1]:", X[-1])
print("X[1:3]:", X[1:3])
print("X:", X)
X[1, 2] = 9
print("X_change1:", X)
X[0:2, :] = 12
print("X_change2:", X)

# 2.5 节省内存
before = id(Y)
Y = Y + X
print(id(Y) == before)

Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X + Y
print('id(Z):', id(Z))

before = id(X)
X += Y
print(id(X) == before)

# 2.6 转换为其他python对象
A = X.numpy()
B = torch.tensor(A)
print(type(A), type(B))

a = torch.tensor([3.5])
print('a:', a)
print('float(a):', float(a))
print('a.item():', a.item())
print('int(a):', int(a))

# 2.7 张量算法的基本性质
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone() # 分配新的内存，将A的副本分配给B
print('A:', A)
print('A+B:', A + B)
print('A*B:', A * B)

a = 2
X = torch.arange(24).reshape(2, 3, 4)
print('a+X:', a + X)
print('a*X_shape:', (a * X).shape)
print('A:', A)
print('A_sum_axis0:', A.sum(axis=0), 'shape:', A.sum(axis=0).shape)
print('A_sum_axis1:', A.sum(axis=1), 'shape:', A.sum(axis=1).shape)
print('sum_axis_all:', A.sum(axis=[0, 1]))
print('A_cumsum:', A.cumsum(axis=0))
