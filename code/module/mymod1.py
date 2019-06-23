# mymod1.py

'''此模块示意__all__列表的作用和用法
'''

__all__ = ['f1','var1']		# 限制 用from mymod1 import *时导入的变量，只导入__all__列表中的变量

def f1():
	pass

def f2():
	pass

def f3():
	pass

var1 = 'hello'
var2 = 'world' 