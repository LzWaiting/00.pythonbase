'''加载电话号码到phone_book.txt,并读取信息:
'''

# 1. 输入电话信息:
def phone_line():
	L = []
	while True:
		name = input('请输入姓名:')
		if not name:
			break
		phone = input('请输入电话:')
		L.append((name,phone))
	return L

# 2. 加载电话信息到phone_book.txt:
def write_phone(L,filename='phone_book.txt'):	# 此处可以有两个形参
	try:
		f = open(filename,'w')
		for name,number in L:		
			f.write(name)
			f.write(':')
			f.write(number)
			f.write('\n')
		f.close()	
	except OSError:
		print('文件未打开')

# 3. 读'phone_book.txt'信息:
def read_phone(filename):
	try:
		L = []
		f = open(filename)
		while True:
			s = f.readline()
			if not s:		# 注意循环
				break
			s = s.rstrip()	# 去掉右侧的换行符'\n'
			name,phone  = s.split(':')		# 字符串解析
			L.append((name,phone))
		return L
		f.close()
	except OSError:
		print('文件未打开')

# 4. 打印读取的信息:
def output_excel(L):
	print('+------------+--------------+')
	print('|    name    |    number    |')
	print('+------------+--------------+')
	for _ in L:
		name = _[0]
		phone = _[1]
		print('|%s|%s|'% (name.center(12),phone.center(14)))
		print('+------------+--------------+')
	
# 主程序:	
if __name__ == '__main__':
	L = phone_line()
	write_phone(L)
	lst = read_phone('phone_book.txt')
	output_excel(lst)
	