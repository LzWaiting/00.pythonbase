# -*- coding:utf-8 -*-

'''存储正整数列表为字节串
'''

# 获取正整数列表:
def numbers_list():
	L = []
	while True:
		i = int(input('请输入整数:'))
		if i < 0:
			break
		L.append(i)
	return L

# 将正整数列表写入numbers.txt文件中
def write_numbers(L,filename=None):
	try:
		# 将列表转成字节串
		# f = open(filename,'wb')
		# f.write(bytes(L))
	
		# 将列表转成字符串
		f = open(filename,'w')
		for _ in L:
			f.write(str(_))
			f.write('\n')	

		f.close()
	except OSError:
		print('文件打开失败')

# 读取numbers.txt文件中的数据:
def read_numbers(filename):
	L = []
	try:
		# f = open(filename,'rb')
		# b = f.read()
		# s = b.decode('utf-8')
		# L = []
		# for _ in s:
		# 	L.append(ord(_))

		# 将字符串转换成列表
		f = open(filename) 		
		try:	
			for line in f:	# line绑定末尾带'\n'的字符串
				n = int(line.rstrip())
				L.append(n)		
		finally:	
			f.close()
	except OSError:
		print('打开文件失败')
	except ValueError:
		print('打开文件失败')
	return L

if __name__ == '__main__':
	L1 = numbers_list()
	write_numbers(L1,'numbers.txt')
	L2 = read_numbers('numbers.txt')
	print(max(L2),min(L2),sum(L2),sep='\n')