#输入一个学生的三科成绩
# 方法一:
# Chinese = float(input("语文成绩:"))
# Math = float(input("数学成绩:"))
# English = float(input("英语成绩:"))
# scoremax = max(Chinese,Math,English)
# scoremin = min(Chinese,Math,English)
# average = round(((Chinese + Math + English)/3),2)
# print("最高分为:",scoremax,"\n最低分为:",scoremin,"\n平均成绩为:",average)

# 方法二:
# score1 = float(input("数学成绩:"))
# score2 = float(input("语文成绩:"))
# score3 = float(input("英语成绩:"))
# if score1 >= score2 and score1 >= score3:
# 	scoreMax = score1
# 	if score2 >= score3:
# 		scoreMin = score3
# 	else:
# 		scoreMin = score2
# elif score2 >= score1 and score2 >= score3:
# 	scoreMax = score2
# 	if score1 >= score3:
# 		scoreMin = score3
# 	else:
# 		scoreMin = score1
# else:
# 	scoreMax = score3
# 	if score1 >= score2:
# 		scoreMin = score2
# 	else:
# 		scoreMin = score1
# averageScore = round(((score1 + score2 + score3) / 3),2)
# print("最高分为:",scoreMax)
# print("最低分为:",scoreMin)
# print("平均分为:",averageScore)

# 方法三:
# score1 = float(input("数学成绩:"))
# score2 = float(input("语文成绩:"))
# score3 = float(input("英语成绩:"))
# averageScore = round(((score1 + score2 + score3)/3),2)
# if score1 >= score2 and score1 >= score3:
# 	scoreMax = score1
# elif score2 >= score1 and score2 >= score3:
# 	scoreMax = score2
# else:
# 	scoreMax = score3
# if score1 <= score2 and score1 <= score3:
# 	scoreMin = score1
# elif score2 <= score1 and score2 <= score3:
# 	scoreMin = score2
# else:
# 	scoreMin = score3	
# print("最高分为:",scoreMax)
# print("最低分为:",scoreMin)
# print("平均分为:",averageScore)

# s1 = int(input('第1科:'))
# s2 = int(input('第2科:'))
# s3 = int(input('第3科:'))
# 方法四
# if s1 > s2:
# 	if s1 > s3:
# 		print('最高成绩是:',s1)
# 	else:
# 		print('最高成绩是:',s3)
# else:
# 	if s2 > s3:
# 		print('最高成绩是:',s2)
# 	else:
# 		print('最高成绩是:',s3)
# 方法五:
# if s2 <= s1 >= s3:
# 	print('最高成绩是:',s1)
# elif s1 <= s2 >= s3:
# 	print('最高成绩是:',s2)
# else:
# 	print('最高成绩是:',s3)

# 方法六:
# print('最高成绩是:',max(s1,s2,s3))

# 经典方法(捡玉米):
# m = s1
# if s2 > m:
# 	m = s2
# if s3 > m:
# 	m = s3
# print('最高成绩是:',m)

#案例(成绩判断):
# score = int(input("请输入一个学生的成绩:"))
# if 0 <= score <= 100:
# 	if score >= 90:
# 		print("优")
# 	elif score >= 80:
# 		print("良")
# 	elif score >= 60:
# 		print("及格")
# 	else:
# 		print("不及格")
# else:
# 	print("您输入的分数不合法")

#案例(成绩是否有效):
# score = int(input("输入一个数:"))
# if 0 <= score <= 100:
# 	pass
# else:
# 	print("有误") 

# score = input("请输入成绩:") or "0"
# score = int(score)
# if score < 0 or score > 100:
# 	print("您输入的成绩不合法")
# else:
# 	print("您输入的成绩:",score)

# score = int(input("成绩") or '0')
# if score < 0 or score > 100:
# 	print("有误")
# else:
# 	print(score)