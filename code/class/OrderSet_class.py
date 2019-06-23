class OrderSet:
	def __init__(self,iterable=None):
		self.__data = list(iterable)

	def __repr__(self):
		return 'OrderSet(%r)' % self.__data
	
	def __and__(self,rhs):	
		return OrderSet(x for x in self.__data if x in rhs.__data)

	def __or__(self,rhs):
		return OrderSet(self.__data + [x for x in rhs.__data if x not in self.__data])

	def __sub__(self,rhs):
		return OrderSet(x for x in self.__data if x not in rhs.__data)

	def __xor__(self,rhs):
		return (self - rhs) | (rhs - self)

	def __eq__(self,rhs):
		return self.__data == rhs.__data

	def __ne__(self,rhs):
		return self.__data != rhs.__data

	def __contains__(self,els):
		return els in self.__data


if __name__ == '__main__':
	s1 = OrderSet([1,2,3,4])
	s2 = OrderSet([3,4,5])
	print(s1 & s2)
	print(s1 | s2)
	print(s1 - s2)
	print(s1 ^ s2)
	if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
		print('不相等')
	if s2 == OrderSet([3,4,5]):
	    print('s2 和 OrderSet(3,4,5)相等')
	if 2 in s1:
		print('2 in s1')