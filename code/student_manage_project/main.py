# main.py

'''操作系统
'''

from menu import main_menu 
from student_info import *

def main():	
	L = []						    			# 输入学生信息
	while True:	
		main_menu()
		num = input('请选择菜单操作：')
		if num == '1':
			L += input_student()				# 添加学生信息
		elif num == '2':
			output_student(L)					# 查看所有学生信息
		elif num == '3':
			revise_info(L)						# 修改学生信息
		elif num == '4':
			delete_info(L)						# 删除学生信息
		elif num == '5':
			sort_score1(L) 
		elif num == '6':
			sort_score2(L)
		elif num == '7':
			sort_age1(L) 		
		elif num == '8':
			sort_age2(L) 
		elif num == '9':
			write_info(L) 		
		elif num == '10':
			L = read_info() 		
		elif num == 'q':
			return	 							# 退出
		else:
			print('输入有误！')
# <<<————————————————————————————————————————————————————>>>
main()
