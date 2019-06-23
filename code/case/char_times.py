# 练习:
# 打印字符串出现的字符及次数
s = input("请输入一段字符串:")

# 方法1(使用字典):
d = {}
for ch in s:	# 遍历运算时间优于方法
# 使用方法:	# s.count() 运算时间较长
# 方法1:
	# d1 = {ch:s.count(ch)}		
	# d.update(d1)
# 方法2:
	# d[ch]=s.count(ch)		
# 使用if语句:		# 去重,累加次数
	# if ch not in d:
	# 	d[ch] = 1
	# else:	
	# 	d[ch] += 1
# 打印字典每个元素:
for k in d:
	print(k,":",d[k],"次")

# 方法2(使用列表):
# l = []
# L = []
# for i in s:
# 	if i in l:
# 		continue
# 	l += [i]
# 	L += [s.count(i)]
# 	print(i,s.count(i),sep = ':')
# print(l,L,sep = "\n")