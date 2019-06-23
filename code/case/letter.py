# 练习2---使用循环语句生成:
# 'ABC...XYZ'
# 'AABbCc...XxYyZz'		# ord('a')- ord('A') = 32
# s = ''
# for ch in range(ord('A'),ord('Z')+1):
# 	i = chr(ch)
# 	s += i
# print(s)

# for i in range(ord('A'),ord('Z') + 1):
# 	s = chr(i)
# 	print(list(s),end = " ")

# for i in range(26):
# 	n = chr(ord('A') + i)
# 	s += n
# print(s)

# i = 0
# s = ''
# for ch1 in range(ord('A'),ord('Z')):
# 	n = chr(ch1)
# 	for ch2 in range(ord('a') + i,ord('a') + i + 1):
# 		m = chr(ch2)
# 	i +=1
# 	s += n + m
# print(s)