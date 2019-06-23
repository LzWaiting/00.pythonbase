#北京出租车计费
# 方法一:
# distance = float(input("请输入行驶的公里数:"))
# if 3 < distance <= 15:
# 	pay = 13 + (distance - 3)*2.3  
# elif distance > 15:
# 	pay = 13 + (distance - 3)*2.3 + (distance - 15)*1.15
# else:
# 	pay = 13
# print("您需要支付:",round(pay),"元")

# 方法二:
# km = float(input("请输入行驶的公里数:"))
# pay = 13  
# if 3 < km <= 15:
# 	pay += (km - 3) * 2.3
# elif km > 15:
# 	pay += 27.6 + (km - 15) * 3.45
# else:
# 	pass
# print("您需要支付:",round(pay),"元") 

# 方法三:
# km = float(input("请输入行驶的公里数:"))
# pay = 13  
# if km > 3:
# 	pay += (km - 3) * 2.3
# if km > 15:
# 	pay += (km - 15) * 1.15
# print("您需要支付:",round(pay),"元") 