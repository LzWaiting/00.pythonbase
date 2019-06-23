# try_except.py

'''此示例示意try-except 语句的用法
'''

def div_apple(n):
	print('%d个苹果您想分给几个人?' % n)
	s = input('请输入人数:')
	cnt = int(s)	# <<= 可能触发ValueError 错误异常
	# 以下一行可能触发ZeroDivisionError错误异常
	try:
		resuit = n / cnt
		print('每个人分了',resuit,'个苹果')
	except ZeroDivisionError:
		print('被零除错误')

# 以下是调用者
# 用try-except 语句来捕获并处理ValueError类型错误
try:
	print('开始分苹果')
	div_apple(10)
	print('分苹果完成')

# 此示例说明一般用法:
# except ValueError:
# 	print('div_apple内出现了ValueError错误,已处理')
# 	print('用户输入不合法,苹果退回来不分了')
# except ZeroDivisionError:
# 	print('div_apple内出现了ZeroDivisionError错误,已处理')
# 	print('用户输入不合法,苹果退回来不分了')

# 此示例说明返回值一样的用法:
# except (ValueError,ZeroDivisionError):
# 	print('用户输入不合法,苹果退回来不分了')

# 此示例说明 as 的用法:
except (ValueError,ZeroDivisionError) as Error:
	print('用户输入不合法,苹果退回来不分了\n','\r错误信息是:',Error)

# 此示例说明 except: other 的用法:
except:
	print('除ValueError,ZeroDivisionError以外的其他类型错误可以被捕获')
else:
	print('程序正常,没有发生异常')
finally:
	print('我是finally子句,一定会执行')		

print('程序正常退出')