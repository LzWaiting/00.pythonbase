# 去重,按顺序打印
# 共用部分
L = []
while True:
	str = input('输入一个单词:')
	if not str:
		break
	L.append(str)

# 方法1:
# s = set()
# for word in L:
# 	if word not in s:	
# 		print(word)
# 	s.add(word)				# 增加新元素

# 方法2:
# 	if str not in L:		# 增加新元素
# 		L.append(str)
# print('输入的单词共%d个' % len(L))
# for word in L:
# 	print(word)

# 方法3:
# s = set(L)
# print('共输入%d个不同的单词' % len(s))
# for word in L:
# 	if word in s:
# 		print(word)
# 		s.discard(word)		# 删除已经打印过的