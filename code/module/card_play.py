
'''模拟斗地主发牌

	说明：
		♠('\u2660'),♣('\u2663'),♥('\u2665'),♦('\u2666')
		大小王
		A2...10JQK
		三人玩牌，每人发17张牌，底牌留三张
		操作：
			输入回车：打印第一个人的17张牌
			输入回车：打印第二个人的17张牌
			输入回车：打印第三个人的17张牌
			输入回车：打印剩余的三张底牌
'''
# 方法1(使用集合+随机抽牌):
# def get_poke():
	
# 	colour = ['\u2660','\u2663','\u2665','\u2666']
# 	size = ['A'] + list(map(str,range(2,11))) + ['J','Q','K']
# 	king = ['大王','小王']
# 	card_info = king + [x + y for x in size for y in colour]
# 	poke = set(card_info)
# 	return poke

# def poke_games():
	
# 	import random			
# 	rest_card = get_poke()
# 	while True:
# 		deal = input('请发牌：')
# 		deal_num = set(random.sample(rest_card,17))
# 		print(sorted(deal_num))	
# 		print()	
# 		rest_card -= deal_num
# 		if len(rest_card) == 3:
# 			break	
# 	print()	
# 	print('底牌：',rest_card)
		
# 方法2(使用列表+随机打乱+切片):
def get_poke():
	
	colour = ['\u2660','\u2663','\u2665','\u2666']
	size = ['A'] + list(map(str,range(2,11))) + ['J','Q','K']
	king = ['大王','小王']
	poke = king + [x + y for x in size for y in colour] 
	return poke

import random			

# def poke_games():	
# 	pk = get_poke()
# 	random.shuffle(pk)
# 	input('请发牌(输入回车继续发牌)：')
# 	print('第一个人的牌:',pk[:17])	
# 	input('请发牌(输入回车继续发牌)：')
# 	print('第二个人的牌:',pk[17:34])	
# 	input('请发牌(输入回车继续发牌)：')
# 	print('第三个人的牌:',pk[34:51])
# 	input('剩余底牌(输入回车抢地主)：')	
# 	print('底牌：',pk[51:])

# 方法2(一张一张发):
def poke_games():	
	pk = get_poke()
	random.shuffle(pk)
	input('请发牌(输入回车继续发牌)：')
	print('第一个人的牌:',pk[:51:3])	
	print('第二个人的牌:',pk[1:51:3])	
	print('第三个人的牌:',pk[2:51:3])
	input('剩余底牌(输入回车抢地主)：')	
	print('底牌：',pk[51:])


poke_games()