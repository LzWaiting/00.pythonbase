# object_relative.py

# 此示例示意面向对象的综合示例:
'''并建立对象与对象之间的逻辑关系'''

class People:
	'''用于描述人的行为与属性'''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.money = 0	# 钱为0
	def teach(self,other,skill):
		print(self.name,'教',other.name,'学习',skill)
	def make_money(self,money):
		self.money += money
		print(self.name,'工作赚了',self.money,'元钱')
	def borrow_money(self,other,money):
		'''描述一个人向其他人借钱,有借,没有不借'''
		if other.money > money:
			print(self.name,'向',other.name,'借了',money,'元')
			self.money += money
			other.money -= money
		else:
			print(other.name,'不借给',self.name,'钱')
	def show_info(self):
		print(self.age,'岁的',self.name,'存有',self.money,'元钱')

if __name__ == '__main__':
	z3 = People('张三',35)
	l4 = People('李四',8)
	z3.teach(l4,'python')
	l4.teach(z3,'橡皮筋')
	z3.make_money(1000)
	l4.borrow_money(z3,200)
	l4.borrow_money(z3,2000)
	z3.show_info()
	l4.show_info()
