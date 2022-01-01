# 将给定的一维数组转化为m*n的二维数组，如果无法转化则返回空数组
from typing import List


# 方法1 简单粗暴的两层for循环遍历，然后添加
def construct2DArray_1(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []
    else:
        result_list = []
        for i in range(m):
            temp_list = []
            for j in range(n):
                temp_list.append(original[n * i + j])
            result_list.append(temp_list)
        return result_list


# 方法2 生成1个均为0的二维数组，遍历原数组1次，截取相应位置的一段一维数组
def construct2DArray_2(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []
    else:
        result_list = [[0] * n for _ in range(m)]
        for i in range(m):
            result_list[i] = original[i*n: i*n+n]
        return result_list


# print(construct2DArray([1, 2, 3, 4, 5, 6], 3, 2))
