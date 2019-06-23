
class Bicycle:
	
	def __init__(self):
		pass
	
	def run(self,km):
		print('自行车骑行了',km,'公里')

class EBicycle(Bicycle):

	def __init__(self,vol): 
		self.volume = vol
	
	def fill_charge(self,vol):
		self.volume += vol
		print('剩余电量',self.volume,'度')
	
	def run(self,km):
		e_km = min(self.volume*10,km)
		# 方法1:
		if e_km > 0:
			print('电动骑行了',e_km,'公里',end = ',')
			self.volume -= e_km / 10
			km -= e_km
		if km > 0:
			super().run(km)
		# 方法2:
		# if e_km == km:
		# 	print('电动骑行了',e_km,'公里')
		# 	self.volume -= e_km / 10
		# else:
		# 	print('电动骑行了',e_km,'公里',end = ',')
		# 	self.volume -= e_km / 10
		# 	km -= e_km
		# 	super().run(km)
		# 方法3:
		# if self.volume >= km / 10:
		# 	print('电动骑行了',km,'公里')
		# 	self.volume -= km / 10
		# else:	
		# 	print('电动骑行了',self.volume * 10,'公里')
		# 	self.km = km - self.volume * 10
		# 	self.volume = 0
		# 	super().run(self.km)
		print('本次骑行后剩余电量:',self.volume,'度')

		
if __name__ == '__main__':
	b = Bicycle()
	b.run(10)	# 自行车骑行了10公里
	e = EBicycle(5)
	e.run(10)	# 电动车骑行了10公里
	e.run(100)	# 电动车骑行了40公里,自行车骑行了60公里
	e.fill_charge(10)
	e.run(80)
