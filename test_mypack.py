
# pbase/test_mypack.py

'''导入menu.py模块
'''

# 第一种用法：
# import mypack.menu 
# mypack.menu.show_menu()

# 第二种用法：
# import mypack.menu as m 
# m.show_menu()

# 第三种用法：
# from mypack.menu import show_menu as menu
# menu()

# <<<-------------------------------->>>

# 此示例测试games包里的子文件是否导入，测试games包中__all__的作用
# from mypack.games import *

# 此示例测试contra模块相对导入menu模块
# 此主模块在pbase下
import mypack.games.contra as contra

contra.gameover()