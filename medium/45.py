# 给你一个非负整数数组nums ，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 假设你总是可以到达数组的最后一个位置。
from typing import List


# 贪心算法，暂时没太理解
def jump(nums: List[int]) -> int:
    answer = 0
    max_pos = 0
    end = 0
    for index in range(0, len(nums) - 1):
        max_pos = max(max_pos, nums[index] + index)
        if end == index:
            end = max_pos
            answer += 1
    return answer


print(jump([2, 3, 1, 1, 4]))
