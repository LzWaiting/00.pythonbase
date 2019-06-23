
'''此示例示意斐波那契数迭代器协议的使用
'''
# 方法1
# class Fibonacci:
# 	def __init__(self,n):
# 		self.__count = n	
	
# 	def __repr__(self):
# 		return '%r' % self
	
# 	def __iter__(self):
# 		return FiboIterator(self.__count)


# class FiboIterator:
# 	def __init__(self,n):
# 		self.__count = n
# 		self.cur_count = 0
# 		self.a = 0
# 		self.b = 1	
	
# 	def __next__(self):
# 		if self.cur_count >= self.__count:
# 			raise StopIteration
# 		self.a, self.b = self.b, self.a + self.b
# 		self.cur_count += 1
# 		return self.a


# 方法2
class Fibonacci:
	def __init__(self,n):
		self.__count = n	
	
	def __repr__(self):
		return '%r' % self
	
	def __iter__(self):
		self.cur_count = 0
		self.a = 0
		self.b = 1	
		return self
	
	def __next__(self):
		if self.cur_count >= self.__count:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		self.cur_count += 1
		return self.a


if __name__ == '__main__':
	for x in Fibonacci(10):
		print(x)
	L = [x for x in Fibonacci(30)]
	print(L)
	print(sum(Fibonacci(25)))