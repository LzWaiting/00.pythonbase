# 猴子吃桃（有一只猴子，摘了很多桃）
def yesterday_peach_num(num):
	last_num = (num + 1) * 2
	return last_num

def monkey_peach_days(day,num):
	for i in range(day):
		if i == day - 1:
			print('小猴子',day,'前总共摘了',num,'个桃子！')
		num = yesterday_peach_num(num)

monkey_peach_days(10,1)
