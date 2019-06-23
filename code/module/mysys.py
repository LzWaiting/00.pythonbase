# -*- coding:utf-8 -*-
import sys

if sys.version_info[0] == 2:
	print('运行环境为python2')
elif sys.version_info[0] == 3:
	print('运行环境为python3')

print('当前的主版本号是：',sys.version_info.major,
	  '当前的次版本号是：',sys.version_info.minor,
	  '当前的微版本号是：',sys.version_info.micro)