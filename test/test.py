#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
sys.path.append('../log')

'整个模块导入'
import log
'导入模块中的方法或类'
from log import Complex
from log import logInfo
from log import testFun



x = Complex(3.0, -4.5)
x.printComplex()
y = log.Complex(1,-2)
y.printComplex()

'如果直接导入函数／类，可以直接使用'
testFun()
'如果只是导入模块，那么要在前面加模块名'
log.testFun()

