#!/usr/bin/python
# -*- coding:utf-8 -*-

import time


'''错误信息'''
def logInfo(msg,file_name="err.log"):
	#追加模式。 读写(如果没有文件会自动创建)。
	with open(file_name,'a+') as f:
		f.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\t' + msg + '\n')
