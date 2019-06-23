# 封装录入的学生信息：
def input_student(*args):
	L = []
	while True:
		name = input("姓名:")
		if not name:
			break
		d = {}			# 创造新字典，重复利用
		d['name'] = name
		age = int(input("年龄:"))
		d['age']= age
		score = int(input("成绩:"))
		d['score'] = score
		L.append(d)
	return L
# <<<————————————————————————————————————————————————————>>>
# 确定表格宽度：
def excel_width(L):
	n,a,s = len('name'),len('age'),len('score')
	for d in L:
		if n < len(d['name']):
			n = len(d['name'])
		if a < len(str(d['age'])):
			a = len(str(d['age']))
		if s < len(str(d['score'])):
			s = len(str(d['score']))
	width = [n,a,s]
	return width
# <<<————————————————————————————————————————————————————>>>
# 打印学生信息：
def output_student(L):
	n,a,s = excel_width(L)	
	i = 1
	for d in L:		
		t = (str(i).center(6),
			d['name'].center(n + 2),		
		 	str(d['age']).center(a + 2),
		 	str(d['score']).center(s + 2)
		 	)
		l = '|%s|%s|%s|%s|' % t 
		i +=1		
		print(l)
# <<<————————————————————————————————————————————————————>>>
# 打印信息表格：
def print_excel(L):
	n,a,s = excel_width(L)
	l0 = '+' + '-' * 6 + '+' + '-'*(n + 2) +'+' + '-'*(a + 2) + '+' + '-'*(s + 2) + '+'
	l1 = '|' + ' sort ' + '|' + 'name'.center(n + 2) + '|' + 'age'.center(a + 2) + '|' + 'score'.center(s + 2) + '|'
	print(l0,l1,l0,sep = "\n")
	output_student(L)
	print(l0) 
# <<<————————————————————————————————————————————————————>>>
# 修改学生信息：
def revise_info(L):
	name = input('请输入要修改学生的姓名：')
	for d in L:
		if name == d['name']:
			opt_age = input("是否要修改年龄（yes/no）:")
			if opt_age == 'yes':
				d['age'] = int(input('请输入新的年龄：'))
			opt_score = input("是否要修改分数（yes/no）:")
			if opt_score == 'yes':
				d['score'] = int(input("请输入新的成绩："))
			L[L.index(d)] = d
			return L
	else:
		print('您输入的学生信息不存在！')

# <<<————————————————————————————————————————————————————>>>
# 删除学生信息：
def delete_info(L):
	name = input('请输入要删除的学生姓名：')
	for d in L:
		if name == d['name']:
			L.remove(d)
			break
	else:
		print('您输入的学生信息不存在！')
	return L

# <<<————————————————————————————————————————————————————>>>
# 添加菜单：
def add_menu():
	d = {}
	k = 1
	while True:
		v = ''
		sr = input('请输入要添加的菜单：')
		if sr == '退出':
			v = '|  '+ 'q' + ') ' + sr + ' '*(35-2*len(sr)) + '|'
			d['q'] = v
			break
		else:
			v = '|  '+ str(k) + ') ' + sr + ' '*(35-2*len(sr)) + '|'
			d[k] = v
		k += 1
	t = (k,d)
	return t

# <<<————————————————————————————————————————————————————>>>
# 菜单：
def menu(t):
	k = t[0]
	d = t[1]
	l0 = '+'+'-'*40+'+'
	print(l0)
	for i in range(1,k):
		print(d[i])
	print(d['q'])
	print(l0)
# <<<————————————————————————————————————————————————————>>>
# 固定菜单：
def main_menu():
	print('+----------------------------------------+')
	print('|  1) 添加学生信息                       |')
	print('|  2) 查看学生信息                       |')
	print('|  3) 修改学生信息                       |')
	print('|  4) 删除学生信息                       |')
	print('|  5) 按成绩从高到低打印学生信息         |')
	print('|  6) 按成绩从低到高打印学生信息         |')
	print('|  7) 按年龄从大到小打印学生信息         |')
	print('|  8) 按年龄从小到大打印学生信息         |')	
	print('|  q) 退出                               |')
	print('+----------------------------------------+')
# <<<————————————————————————————————————————————————————>>>
# 按成绩从高到底排序(desc降序)：
def sort_score1(L):
	print('按成绩从高到低排序后：')
	L1 = sorted(L,key=lambda x : x['score'],reverse=True)
	print_excel(L1)
	# return L1

# <<<————————————————————————————————————————————————————>>>
# 按成绩从低到高排序(asc升序)：
def sort_score2(L):
	print('按成绩从低到高排序后：')
	L2 = sorted(L,key=lambda x : x['score'])
	print_excel(L2)
	# return L2

# <<<————————————————————————————————————————————————————>>>
# 按年龄从大到小排序：
def sort_age1(L):
	print('按年龄从大到小排序后：')
	L3 = sorted(L,key=lambda x : x['age'],reverse=True)
	print_excel(L3)
	# return L3
	
# <<<————————————————————————————————————————————————————>>>
# 按年龄从小到大排序：
def sort_age2(L):
	print('按年龄从小到大排序后：')
	L4 = sorted(L,key=lambda x : x['age'])
	print_excel(L4)
	# return L4
	

# <<<————————————————————————————————————————————————————>>>
def main():	
	L = []						    			# 输入学生信息
	# t = add_menu()								# 添加菜单信息
	while True:	
		# menu(t)									# 显示菜单
		# opt_menu(L)							# 选择菜单操作(可选择函数)
		main_menu()
		num = input('请选择菜单操作：')
		if num == '1':
			L += input_student()				# 添加学生信息
		elif num == '2':
			print_excel(L)						# 查看所有学生信息
		elif num == '3':
			revise_info(L)						# 修改学生信息
		elif num == '4':
			delete_info(L)						# 删除学生信息
		elif num == '5':
			sort_score1(L) 
		elif num == '6':
			sort_score2(L)
		elif num == '7':
			sort_age1(L) 		
		elif num == '8':
			sort_age2(L) 		
		elif num == 'q':
			return	 							# 退出
		else:
			print('输入有误！')
# <<<————————————————————————————————————————————————————>>>
main()


# <<<————————————————————————————————————————————————————>>>
# 选择菜单：
def opt_menu(L):	
	num = input('请选择菜单操作：')
	if num == '1':
		L += input_student()				# 添加学生信息
	elif num == '2':
		print_excel(L)						# 查看所有学生信息
	elif num == '3':
		revise_info(L)						# 修改学生信息
	elif num == '4':
		delete_info(L)						# 删除学生信息
	elif num == '5':
		print('按年龄从大到小排序后：')
		L2 = sort_age(L) 
		print_excel(L2)
	elif num == '6':
		print('按成绩从高到低排序后：')
		L3 = sort_score(L) 
		print_excel(L3)
	elif num == 'q':
		return	 							# 退出
	else:
		print('输入有误！')
# <<<————————————————————————————————————————————————————>>>
# 排序：
def main1():
	L = input_student()
	print_excel(L)
	print('按年龄从大到小排序后：')
	L2 = sort_age(L) 
	print_excel(L2)

	print('按成绩从高到低排序后：')
	L3 = sort_score(L) 
	print_excel(L3)
# <<<————————————————————————————————————————————————————>>>
# main1()