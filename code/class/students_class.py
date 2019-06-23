
'''此示例示意类变量和方法的使用
'''
class Student:
	count = 0	# 类变量用来记录学生的个数
	# docs = []	# 此列表保存所有的学生对象
	def __init__(self,name,age,score=0):
		self.name = name
		self.age = age
		self.score = score
		Student.count += 1	# 让对象个数加1
		# Student.docs.append((self.name,self.age,self.score))
	
	def __del__(self):
		Student.count -= 1	# 将对象销毁

	def get_score(self):
		return self.score

	@classmethod
	def getTotalCount(cls):		# 此方法用来得到学生的个数
		return cls.count

def test():
	L = []
	L.append(Student('小张',20,98))
	L.append(Student('小李',21,89))
	L.append(Student('小王',20,93))
	print('学生总人数:',Student.getTotalCount())

	L2 = []
	L2.append(Student('小陈',18,95))
	L2.append(Student('小赵',19,90))
	L2.append(Student('小林',21,97))
	print('学生总人数:',Student.getTotalCount())
	
	L.pop(1)
	print('学生总人数:',Student.getTotalCount())

	docs = L + L2
	scores = 0	# 所有学生成绩总和
	for s in docs:
		scores += s.get_score()
	print('平均成绩:',scores/len(docs))

if __name__ == '__main__':
	test()