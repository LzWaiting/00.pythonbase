# 点名系统:
# 共用部分:
List_names = {'唐一','刘二','张三','李四','王五','赵六'}	# 全班名单
Uncall_names = set(List_names)	# 未到的人员名单
print('全班人名单:',List_names)
Absent_names = []		# 缺席名单
for name in List_names:
	print(name,"到了吗?")
	info = input('请确认是否到场(到场请输入y):')

# 方法1:
	# if info == 'y':
	# 	Uncall_names.discard(name)		# 去掉在场人员
# print('缺席人名单:',Uncall_names)

# 方法2:
	if info != 'y':
		Absent_names.append(name)		# 增加缺席人员
print('缺席人名单:',Absent_names)
