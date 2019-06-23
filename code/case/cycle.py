# 重复打印 n 行字符串

# n = int(input("请输入一个整数:"))
# 方法1:
# str = "\nhello world" * n
# print(str)

# 方法2:
# i = 0
# while i < n: 
# 	print("hello world")
# 	i += 1
# else:
# 	print("循环结束")

# 方法3:
# while n > 0:
# 	print("hello world")
# 	n -= 1
# else:
# 	print("结束")


# 用while打印1~n 的整数(包含n)
# 方法1:
# i = 1
# while i <= n:
# 	print(i)
# 	i += 1 



# 输入两个整数,一个begin,一个end,打印begin~end 所有的整数
# begin = int(input("输入一个整数:"))
# end = int(input("输入一个大于上一个数的整数:"))
# while begin <= end:
# 	print(begin)
# 	begin += 1



# 打印1~20整数,显示一行内,每个数字之间用空格分开
# 方法1:
# i = 1
# num = str()
# while i <= 20:
# 	num += str(i) + " "
# 	i += 1 
# print(num)

# 方法2:
# i = 1
# while i <= 20:
# 	print(i,end = " ")
# 	i += 1
# print()



# 打印1~20整数,每行5个
# 方法1:
# i = 1
# num = str()
# while i <= 20:
	# num += str(i) + " "
	# if i % 5 == 0:
		# num += "\n"
# 	i += 1
# print(num)
# 方法2:
# while i <= 20:
# 	print(i,end = " ")
# 	if i % 5 == 0:
# 		print()
# 	i += 1



# 用while语句打印10~1所有的整数(包含1)
# i = 1
# num = str()
# while i <= 10:
# 	num += str(11 - i) + " "
# 	i += 1
# print(num)

# 1 + 2 + 3 +...+ 100 求和
# i = 1
# sum = 0
# while i <= 100:
# 	sum += i
# 	i += 1
# print (sum)



# 打印三角形,输入一个整数,表示三角形的宽度和高度,打印对应直角三角形
# i = 1
# while i <= n:
# 	print("*"*i)
#	i += 1

# i = 1
# while i <= 10:
# 	j = 1
# 	while j <= 20:
# 		print(j,end = " ")
# 		j += 1
# 	if i == 8:
# 		break
# 	print()
# 	i += 1
# print()



# 求输入正整数的和:
# s = 0
# while True:
# 	i = int(input("任意输入一些整数:"))
# 	if i < 0:
# 		break
# 	s += i
# print("您输入的所有正整数和为:",s)



# 使用for语句循环遍历,迭代对象中的元素
# s = 'ABCDEF'
# for ch in s:
# 	print('ch-->',ch)
# else:
# 	print("else语句")
# print("退出")



# s = input("输入一个字符串:")
# i = 0
# for t in s:
# 	if t == " ":
# 		i += 1
# print(i)

# print(s.count(" "))

# for ch in range(5):
# 	print(ch)

# for num in range(1,21):
# 	print(num,end = " ")
# print()



# 0~100,有那些整数,n(n+1)%11=8
# for num in range(100):
# 	if num*(num + 1)%11 == 8:
# 		print(num)



# 计算1 + 3 + 5 + ... + 99的和(while/for)

# while 语句
# n = 1
# s = 0
# while n < 100:
# 	s += n
# 	n += 2

# for 语句嵌套if语句
# for n in range(100):
# 	if n % 2 == 1:
# 		s += n 

# for 语句range 函数
# for n in range(1,100,2):
# 		s += n 
# print(s)



# for x in "ABC":
# 	for y in "123":
# 		print(x + y,end=" ")
# 	print()

# count = 0
# for x in range(5):
# 	for y in range(10):
# 		count += 1
# 	print(count)	# 10 20 30 40 50
# print(count)	# 50

# for x in range(5):
# 	for y in range(10):
# 		pass
# print(x,y)
 
