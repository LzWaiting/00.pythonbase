
class Student:
	
	def __init__(self,name,age=0,score=0):
		'''信息输入
		'''
		self.__name = name
		self.__age = age
		self.__score = score
	
	def get_infos(self):
		return(self.__name,self.__age,self.__score)
	
	def get_age(self):
		return self.__age
	
	def get_score(self):
		return self.__score
	
	def is_name(self,name):
		return self.__name == name
	
	def write_file(self,file):
		t = (self.__name,self.__age,self.__score)
		s = '%s,%d,%d\n' % t
		file.write(s)

	def set_score(self,score):
		'''此方法用于制定成绩设置规则'''
		if 0 <= score <= 100:
			self.__score = score
			return
		raise ValueError('不合法的成绩信息:'+str(score))

