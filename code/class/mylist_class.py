class MyList(list):
	def __init__(self,*args):
		super().__init__(*args)
	def insert_head(self,value):
		'''将value插入到列表的开始处'''
		# self[0:0] = [value]
		self.insert(0,value)
	def insert_tail(self,value):
		'''将value插入到列表的开始处'''
		# self[len(self):len(self)] = [value]
		self.insert(len(self),value)

L = MyList(range(1,5))
print(L)
L.insert_head(0)
print(L)
L.insert_tail(5)
print(L)
L.append(6)
print(L)