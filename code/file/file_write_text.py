
'''此示例示意写文件f.write /f.writelines
'''

def file_write():
	try:
		f = open('mynote.txt','w')
		
		f.write('I love you!\n')		
		
		L = ['I am Mr.Li\n','I love Miss.zx']
		f.writelines(L)
		
		f.close()
	except OSError:
		print('出错')

if __name__ == '__main__':
	file_write()
