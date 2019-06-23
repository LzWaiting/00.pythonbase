# 练习:
# 由两个列表生成对应字典:
Nos = [1001,1002,1003,1004]
names = ['Tom','Jerry','Spike','Tyke']

# 方法1(经典):
# d = {Nos[i]:names[i] 
# 	 for i in range(min(len(Nos),len(names)))} 
# 方法2(索引值):
# d = {k:names[Nos.index(k)] for k in Nos}

# d = {}
# 方法3(for循环):
# for k in Nos:
# 	d[k] = names[Nos.index(k)]
# 方法4:
# for i in range(min(len(Nos),len(names))):
# 	d[Nos[i]] = names[i]

print(d)