# guess_number(猜数字游戏/二分查找)

'''此函数用来随机生成一个数，
进行猜数字游戏
'''

def guess_number():
	
	import random as R

	x = R.randrange(101)

	times = 0

	while True:
		y = int(input('请随意输入一个数：'))
		times += 1
		if y == x:
			print('恭喜您，您猜对了！')
			break
		elif y < x:
			print('很遗憾，您猜小了，请再接再厉！')
		elif y > x:
			print('恭喜您，您猜大了，请继续！')
	print('您猜了%d次' % times)

guess_number()