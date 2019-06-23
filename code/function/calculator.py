# 一个计算器解释执行器：

# 加法：
def myadd(x,y):
	return x + y
# 乘法：
def mymul(x,y):
	return x * y
# 减法：
def mysub(x,y):
	return x - y
# 除法：
def mydiv(x,y):
	return x / y

# 计算器解释执行器：
def get_op(s):		# s 代表字符串：‘加‘，’乘‘
	if s == '加' or s == '+':
		return myadd
	elif s == '乘' or s == '*':
		return mymul
	elif s == '减' or s == '-'：
		return mysub
	elif s == '除' or s == '/':
		return mydiv

# 主函数：
def main():
	while True:
		s = input('请输入计算公式：') 		# 10 加 20
		L = s.split()
		a,s,b = L
		a,b = int(a),int(b)
		fn = get_op(s)
		print('结果是：',fn(a,b))

# 调用函数：
main()