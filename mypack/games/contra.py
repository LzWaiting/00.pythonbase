# contra.py


def play():
	print('正在玩contra')

print('contra 模块被加载')


def gameover():	
	# 用绝对路径方式导入
	# from mypack.menu import show_menu
	# 用相对路径导入
	from ..menu import show_menu
	show_menu()