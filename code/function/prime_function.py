# 素数函数

# 判断x是否是素数：
def isprime(x):
	if x > 1:
		for i in range(2,x):
			if x % i == 0:
				return False
		return True
	else:
		return False

# 找出(m,n)之间的素数：
def prime_m2n(m,n):
	# L = []
	# for i in range(m,n):
	# 	if isprime(i):
	# 		L.append(i)
	# return L
	return [i for i in range(m,n) if isprime(i)]

# 返回n以内的所有素数：
def primes(n):
	L = prime_m2n(0,n)
	print(L)
	return L

# 求和函数
def mysum(*args):
	sum = 0
	for i in args:
		sum += i
	print('和：',sum)
	return sum

L = prime_m2n(1,10)
print(L)

primes(20)
primes(100)
mysum(*primes(100))



