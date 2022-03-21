# 升序排列的数组，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。(元素的相对顺序应该保持一致)
from typing import List


# 复制原数组，for循环遍历复制的，在原数组上操作
def removeDuplicates_1(nums: List[int]) -> int:
    nums_copy = nums.copy()
    for index in range(len(nums_copy)):
        if index == 0:
            continue
        if nums_copy[index] == nums_copy[index - 1]:
            nums.remove(nums_copy[index])
    return len(nums)


# 快慢指针，快的正常遍历，慢的记录非重复
def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


# 扩展 输出列表
def add(nums: List[int]) -> int:
    i = 0
    result = [nums[i]]
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            result.append(nums[i])
    return result


print(add([0,0,1,1,1,2,2,3,3,4]))
