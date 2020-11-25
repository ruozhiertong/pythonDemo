#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

import datetime

import copy

import functools

import builtins

from typing import NamedTuple

class test:

    @classmethod
    def fun():
        pass

def main():

    print(datetime.date.today())

    weight = np.array([0.15, 0.2, 0.25, 0.4])
    print(type(weight))
    weight.shape

    stock_return =np.array([[0.0037131, 0.021066, -0.004854, 0.006098, 0.00606],[-0.001838, 0.001842, -0.016544, -0.003738, 0.003752],[-0.003087, -0.000344, -0.033391, -0.007123, 0.004597],[-0.024112, 0.011704, -0.029563, -0.01457, 0.016129]])

    print(stock_return)

    print(stock_return.shape)

    print(np.eye(4))

    l = [1,2,3,4,5,6]

    print(stock_return.reshape)


if __name__ == "__main__":
    main()
