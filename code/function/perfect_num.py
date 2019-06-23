# 判断一个数是否是完全数：
def is_perfect_num(n):
	L = []		# 每次循环开始都创建一个新列表，用来存因数
	for i in range(1,n):
		if n % i == 0:
			L.append(i)	 # 此时列表是n的所有因数
	if sum(L) == n:
		return True
	return False
# <<<------------------------------>>>
# 从range(1,n)中有哪些完全数？
def perfect_num(n):
	i = 1
	while i < n:
		flag = is_perfect_num(i)
		if flag == True:
			print(i,'是完全数！')
		i += 1

perfect_num(10000)
# <<<------------------------------>>>
# 获得m个完全数：
def find_perfect(m):
	L1 = []
	n = 2
	while True:
		L = []
		for i in range(1,n):
			if n % i == 0:
				L.append(i)	
		if sum(L) == n:
			L1.append(n)
			print(L)
		n += 1
		if len(L1) == m:	
			break
	print(L1)

myperfect(4)
