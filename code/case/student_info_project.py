# 学生管理项目准备工作:
# 方法1：
# d = {}
# L = []
# n,a,s = len('name'),len('age'),len('score')
# print("---录入学生信息---")
# while True:
# 	name = input("姓名:")
# 	if not name:
# 		break
# 	else:
# 		d['name'] = name
# 		age = int(input("年龄:"))
# 		d['age']= age
# 		score = int(input("成绩:"))
# 		d['score'] = score
# 		if n < len(d['name']):
# 			n = len(d['name'])
# 		if a < len(str(d['age'])):
# 			a = len(str(d['age']))
# 		if s < len(str(d['score'])):
# 			s = len(str(d['score']))
# 		L.append({k:d[k] for k in d})		# 此处注意字典d会重复覆盖，可先提取，再更新
# l0 = '+' + '-'*(n + 2) +'+' + '-'*(a + 2) + '+' + '-'*(s + 2) + '+'
# l1 = '|' + 'name'.center(n + 2) + '|' + 'age'.center(a + 2) + '|' + 'score'.center(s + 2) + '|'
# print("---学生信息汇总---",'\n',L)
# print('---学生信息列表---')
# print(l0,l1,l0,sep = "\n")
# for i in range(len(L)):
# 	nv = str(L[i]['name'])
# 	av = str(L[i]['age'])
# 	sv = str(L[i]['score'])
# 	l = '|' + nv.center(n + 2) + '|' + av.center(a + 2) + '|' + sv.center(s + 2) + '|'
# 	print(l)
# print(l0) 

# 方法2
		# d = {}			# 创造新字典，重复利用
		# d['name'] = name
		# age = int(input("年龄:"))
		# d['age']= age
		# score = int(input("成绩:"))
		# d['score'] = score
		# if n < len(d['name']):
		# 	n = len(d['name'])
		# if a < len(str(d['age'])):
		# 	a = len(str(d['age']))
		# if s < len(str(d['score'])):
		# 	s = len(str(d['score']))
		# L.append(d)
# l0 = '+' + '-'*(n + 2) +'+' + '-'*(a + 2) + '+' + '-'*(s + 2) + '+'
# l1 = '|' + 'name'.center(n + 2) + '|' + 'age'.center(a + 2) + '|' + 'score'.center(s + 2) + '|'
# print("---学生信息汇总---",'\n',L)
# print('---学生信息列表---')
# print(l0,l1,l0,sep = "\n")
# for d in L:		# d 绑定列表中的字典
# 	t = (d['name'].center(n + 2),		# t为元组
# 		 str(d['age']).center(a + 2),
# 		 str(d['score']).center(s + 2)
# 		 )
# 	l = '|%s|%s|%s|' % t 		# 字符串格式化
# 	print(l)
# print(l0) 

print('<<<------------------------------------------------------------>>>')

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

# 打印学生信息：
def output_student(L):
	n,a,s = excel_width(L)	
	for d in L:		
		t = (d['name'].center(n + 2),		
		 	str(d['age']).center(a + 2),
		 	str(d['score']).center(s + 2)
		 	)
		l = '|%s|%s|%s|' % t 		
		print(l)

# 打印信息表格：
def print_excel(L):
	n,a,s = excel_width(L)
	l0 = '+' + '-'*(n + 2) +'+' + '-'*(a + 2) + '+' + '-'*(s + 2) + '+'
	l1 = '|' + 'name'.center(n + 2) + '|' + 'age'.center(a + 2) + '|' + 'score'.center(s + 2) + '|'
	print(l0,l1,l0,sep = "\n")
	output_student(L)
	print(l0) 


# 运行程序：
print_excel(input_student())
