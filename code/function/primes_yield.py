'''使用生成器函数primes(begin,end)生成素数
'''

from myrange_yield import *

def is_prime(n):
	if n < 2:
		return False
	for _ in myrange(2,n):
		if n % _ == 0:
			return False
	return True

def primes(begin,end):
	for _ in myrange(begin,end):
		if is_prime(_):
			yield _

if __name__ == '__main__':
	L = [x for x in primes(10,20)]
	print(L)