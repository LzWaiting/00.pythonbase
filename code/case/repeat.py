print("去重")
# # 重复出现多次的数字只显示一次(去重复)
L = [1,1,3,3,2,1,6,4,2,12,15,15,23,25,31,98,82,23,6,1]

# 方法1(逐一比较):
# L2 = []
# for x in L:
# 	if x not in L2:		
# 		L2.append(x)

L2 = L.copy()
# 方法2(消元法,不推荐):
# for x in L2:
# 	if L2.count(x) > 1:
# 		L2.remove(x)

# 方法3(索引):
i = 0
while i < len(L2):
	if L2.count(L2[i]) > 1:
		del L2[i] 
		continue	# 此时注意删除的元素索引应补位,此处无需i += 1
	i += 1
print(L,L2,sep="\n")
