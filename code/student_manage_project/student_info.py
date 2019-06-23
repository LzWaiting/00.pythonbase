
# student_info.py

'''学生信息系统：

	1. 添加学生信息
	2. 查看学生信息
	3. 修改学生信息
	4. 删除学生信息
	5. 按成绩从高到低打印学生信息
	6. 按成绩从低到高打印学生信息
	7. 按年龄从大到小打印学生信息
	8. 按年龄从小到大打印学生信息
	q. 退出
'''
from student_class import Student
# 1. 添加学生信息：
def input_student():
	L = []
	while True:
		name = input("姓名:")
		if not name:
			break
		age = int(input("年龄:"))
		score = int(input("成绩:"))
		d = Student(name,age,score)
		L.append(d)
	return L
# <<<————————————————————————————————————————————————————>>>
# 打印学生信息：
# <<<————————————————————————————————————————————————————>>>
# 2. 查看学生信息：
def output_student(L):
	l0 = '+' + '-' * 6 + '+' + '-'*(12) +'+' + '-'*(6) + '+' + '-'*(7) + '+'
	l1 = '|' + ' sort ' + '|' + 'name'.center(12) + '|' + 'age'.center(6) + '|' + 'score'.center(7) + '|'
	print(l0,l1,l0,sep = "\n")
	i = 1
	for d in L:		
		n,a,s = d.get_infos()	
		t = (str(i).center(6),
			n.center(12),		
		 	str(a).center(6),
		 	str(s).center(7)
		 	)
		l = '|%s|%s|%s|%s|' % t 
		i +=1		
		print(l)
	print(l0) 
# <<<————————————————————————————————————————————————————>>>
# 3. 修改学生信息：
def revise_info(L):
	name = input('请输入要修改学生的姓名：')
	for d in L:
		if d.is_name(name):
			score = int(input("请输入新的成绩："))
			d.set_score(score)
			print('修改',name,'的成绩为',score)
			return 
	else:
		print('您输入的学生信息不存在！')
# <<<————————————————————————————————————————————————————>>>
# 4. 删除学生信息：
def delete_info(L):
	name = input('请输入要删除的学生姓名：')
	for d in L:
		if d.is_name(name):
			del L[L.index(d)]
			return 
	else:
		print('没有找到名为:',name,'的学生')
# <<<————————————————————————————————————————————————————>>>
# 5. 按成绩从高到低打印学生信息(desc降序)：
def sort_score1(L):
	print('按成绩从高到低排序后：')
	lst = sorted(L,key=lambda d : d.get_score(),reverse=True)
	output_student(lst)

# <<<————————————————————————————————————————————————————>>>
# 6. 按成绩从低到高打印学生信息(asc升序)：
def sort_score2(L):
	print('按成绩从低到高排序后：')
	lst = sorted(L,key=lambda d : d.get_score())
	output_student(lst)

# <<<————————————————————————————————————————————————————>>>
# 7. 按年龄从大到小打印学生信息：
def sort_age1(L):
	print('按年龄从大到小排序后：')
	lst = sorted(L,key=lambda d : d.get_age(),reverse=True)
	output_student(lst)
	
# <<<————————————————————————————————————————————————————>>>
# 8. 按年龄从小到大打印学生信息：
def sort_age2(L):
	print('按年龄从小到大排序后：')
	lst = sorted(L,key=lambda d : d.get_age())
	output_student(lst)
# <<<————————————————————————————————————————————————————>>>
# 9. 保存信息到文件(si.txt)：
def write_info(L,filename = "si.txt"):
	try:
		f = open(filename,'wt')
		for _ in L:
		# 方法1(调用类获得信息,在此处保存):
		# 	t = _.get_infos()
		# 	s = '%s,%d,%d\n' % t
		# 	f.write(s)
		# 方法2(在类中保存,调用类):	
			_.write_file(f)

		f.close()
		print('保存文件成功')
	except OSError:
		print('保存文件失败')

# <<<————————————————————————————————————————————————————>>>
# 10. 从文件中读取数据(si.txt)：	
def read_info(filename = 'si.txt'):
	# 方法1:
	# try:
	# 	f = open(filename,'rt')
	# 	s = f.read()
	# 	print(s)
	# 	f.close()
	# except OSError:
	# 	print('读取文件失败')
	# 方法2:
	L = []
	try:
		f = open(filename,'rt')
		for line in f:
			s = line.rstrip()
			name,age,score = s.split(',')
			age = int(age)
			score = int(score)
			L.append(Student(name,age,score))

		f.close() 
	except OSError:
		print('读取文件失败')
	return L
# <<<————————————————————————————————————————————————————>>>
if __name__ == '__main__':
	L = input_student()		# 1
	output_student(L)		# 2
	revise_info(L)			# 3
	delete_info(L)			# 4
	sort_score1(L)			# 5
	sort_score2(L)			# 6
	sort_age1(L)			# 7
	sort_age2(L)			# 8
	write_info(L)			# 9
	read_info()				# 10