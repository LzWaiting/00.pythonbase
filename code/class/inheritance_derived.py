
'''此示例示意继承和派生
'''
class Human(object):
	'''此类用来描述人类的共性行为:'''
	def say(self,that):
		print('say:',that)
	def walk(self,distance):
		print('walk',distance,'km')

class Student(Human):
	def study(self,subject):
		print('正在学习',subject)

class Teacher(Student):
	def teach(self,subject):
		print('正在教',subject)

h1 = Human()
h1.say('今天天气真热')
h1.walk(5)
print('--------以下是学生行为---------')
s1 = Student()
s1.say('学习有点累')
s1.walk(3)
s1.study('python')
print('--------以下是学生行为---------')
t1 = Teacher()
t1.say('明天就星期天了')
t1.walk(6)
t1.teach('面向对象')
t1.study('class')