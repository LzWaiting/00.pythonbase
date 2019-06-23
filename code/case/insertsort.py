

# def insertsot(l):
#     N = len(l)
#     for i in range(1, N):  # 从小标1也就是第二位元素开始遍历
#         n = l[i]  # 获取待排序列的值
#         a, b = i, i  # a就是应该插入的位置 b 就是原本的位置
#         while n < l[a - 1] and a - 1 >= 0:
#             a -= 1 #当在有序数组中没有找到小于等于自己元素时，往前挪一位继续找
#             if a - 1 < 0:
#                 a = 0
#         #已经找到了该元素应该插入的位置，现在挪动部分有序数组到待排元素的位置上
#         while b > a:
#             l[b] = l[b-1]
#             b -= 1
#         l[a] = n #将待排序元素插入到应该插入的位置a

#     return l

def insert_sort(L):
    for j in range(len(L)):    
        for i in range(len(L)-1):
            if L[i] >= L[i+1]:
                m = L[i]
                L[i] = L[i+1]
                L[i+1] = m
    return L



print(insert_sort([100, 2, 29, 66, 0, 2, 1, 3]))


