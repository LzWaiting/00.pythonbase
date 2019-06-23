# print("示例1:列表推导式")
# # 用字符串s1 = 'ABC'和 s2 = '123' 生成列表:['A1','A2','A3','B1','B2','B3','C1','C2','C3']
s = 'ABC'
s2 = '123'
s1 = [x + y for x in s for y in s2]
print(s1)