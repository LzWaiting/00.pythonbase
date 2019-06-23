
'''分解质因数,输入一个正整数,分解质因数(质因数是指最小能被原数整除的素数(不包括1)):
	如:90=2*3*3*5
'''
# 判断n是否是素数:
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				return False
		return True
	else:
		return False

'''如何用n求出所有的因数
'''
def get_prime_list(n):
	L = []		# 用来存放所有的因数(素数)
	while not isprime(n):	# 不是素数,拆因数
		for _ in range(n):
			if isprime(_) and n % _ == 0:	# 此时_一定是n的因数
				L.append(str(_))
				n /= _
				n = int(n)		# 此处为浮点数,应转为整型
				break
	else:
		L.append(str(n))
	return L

if __name__ == '__main__':
	n = int(input('请输入一个正整数:'))
	L = get_prime_list(n)
	print(n,'=','*'.join(L))


