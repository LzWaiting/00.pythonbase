# 生成字典,并进行搜索:
# 方法1（两个列表，一个字典，一个字典推导式）：
# W = []
# E = []
dictionary = {}
# while True:
# 	word = input("单词:")
# 	W.append(word)
# 	if world == "":
# 		break
# 	explain = input("解释:")
# 	E.append(explain)
# dictionary = {k:E[W.index(k)] for k in W}
# while True:	
# 	Index_word = input("请输入要查寻的单词:")
# 	if not I:
# 		break
# 	else:
# 		if Index_word in dictionary:
# 			print("你输入的单词",Index_word,"\n意思是:",dictionary[I])
# 		else:
# 			print("你输入的单词不在词库里")

# 方法2（一个字典）：
while True:		# 输入词汇
	word = input("单词：")
	if not word:
		break
	explain = input("解释：")
	dictionary[word] = explain
while True:		# 查找词汇
	index_word = input("请输入要查寻的单词：")
	if not index_word:
		break
	if index_word in dictionary:
		print(index_word,"的解释：",dictionary[index_word]) 
	else:
		print("您输入的单词不在字典里！请重新输入：")
