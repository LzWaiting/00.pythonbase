# 练习1:
'''100米高扔球,每次反弹高度的一半
'''

# 方法1:
# def ball_high(height,times):
# 	for _ in range(times):
# 		height = height / 2	
# 	return height

# def ball_distance(height,times):
# 	dis = 0
# 	for _ in range(times):
# 		dis += height	# 下落过程
# 		height /= 2
# 		dis += height 	# 反弹过程
# 	return dis

# def main():
# 	h = int(input('请输入高度:'))
# 	n = int(input('请输入掉落次数:'))
# 	print(ball_high(h,n))
# 	print(ball_distance(h,n))

# main()

# 方法2:
# n = int(input('请输入掉落次数:'))
# print('从100高落下,在第',n,'次落地后反弹高度是:',100/2**n,'米')

# print('球',n,'次落地反弹共经过了',2*sum(map(lambda s:100/2**s,range(n)))-100,'米') 
