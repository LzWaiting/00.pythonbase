# 去掉一个字符串的前后字符
# s = input('请输入一个字符串:')
# x = s[1:len(s)-1]
# print('处理后的字符串为:',x)

# s = input('请输入一个字符串:')
# x = s[1:-1]
# print('处理后的字符串为:',x)

# 判断一个字符串是否是回文(回文是指中心对称的文字)
# s = (input('请输入一个字符串:'))
# h = s[::-1]
# if h == s:
# 	print('您所输入的:',s,'是回文')
# else:
# 	print('您所输入的:',s,'不是回文')

# 不为空,打印第一个字符编码
# s = input('请输入一段字符串:')
# if s != '':
# 	print('第一个字符的编码:',ord(s[0]))

# 打印一个数值对应的字符
# num = int(input('请输入一个整数(0~65535):'))
# if 0 <= num <= 65535:
# 	print(chr(num))

# 使用字符串*打印三角形
# n = int(input('请输入一个整数:'))
# line0 = ' '*(n + 3) + '*'
# line1 = '\n' + ' '*(n + 2) + '*'*3
# line2 = '\n' + ' '*(n + 1) + '*'*5
# line3 = '\n' + ' '*n + '*'*7
# print(line0,line1,line2,line3)

# 文字居中
w1 = input('请输入三行文字:\n')
w2 = input('')
w3 = input('')
n1 = len(w1)
n2 = len(w2)
n3 = len(w3)
# n0 = n1
# if n0 < n2:
# 	n0 = n2
# if n0 < n3:
# 	n0 = n3
# l1 = '+' + '-'*(n0 + 2) + '+'
# l2 = '\n' + '|' + ' '*((n0 + 2 - n1)//2) + w1 + ' '*((n0 + 2 - n1) - (n0 + 2 - n1)//2) + '|'
# l3 = '\n' + '|' + ' '*((n0 + 2 - n2)//2) + w2 + ' '*((n0 + 2 - n2) - (n0 + 2 - n2)//2) + '|'
# l4 = '\n' + '|' + ' '*((n0 + 2 - n3)//2) + w3 + ' '*((n0 + 2 - n3) - (n0 + 2 - n3)//2) + '|'
# l5 = '\n' + l1
# print(l1,l2,l3,l4,l5)

# 方法2使用方法进行:
# n0 = max(n1,n2,n3)	
# l1 = '+' + '-'*(n0 + 2) + '+'
# l2 = '\n' + '| ' + w1.center(n0) + ' |'
# l3 = '\n' + '| ' + w2.center(n0) + ' |'
# l4 = '\n' + '| ' + w3.center(n0) + ' |'
# l5 = '\n' + l1
# print(l1,l2,l3,l4,l5)