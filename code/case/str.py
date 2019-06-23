# 字符串方法:
# s = input("输入一个字符串:")
# print(s.count(' '))
# n = s.strip()
# print(len(n))
# if n.isdigit():
# 	print('您输入的',s,'是数字')
# else:
# 	print('您输入的',s,'不是数字') 

# 格式化表达式
# fmt = "姓名:_%s_\n年龄:_%d_"
# name = input('请输入姓名:')
# age = int(input("请输入年龄:"))
# s = fmt % (name,age)
# print (s)

# 文字宽度20,右对齐
# s1 = input("输入第一行文字:")
# s2 = input("输入第二行文字:")
# s3 = input("输入第三行文字:")
# __以下按宽度20,右对齐
# s01 = "%20s" % s1
# s02 = "%20s" % s2
# s03 = "%20s" % s3
# __以下按最长的字符串的长度右对齐
# a = max(len(s1),len(s2),len(s3))
# m = "%%%ds" % a
# print(m % s1)
# print(m % s2)
# print(m % s3)