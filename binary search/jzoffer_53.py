# 剑指offfer 53
# 统计一个数字在排序数组中出现的次数
# 输入：数组=[5, 7, 7, 8, 8, 10], target=8(target = 6)
# ouput: 2(0)

import time

# 我的思路：
# 先找到任意一个目标数字的位置，计算一次次数
# 然后对该位置的上、下方向分别逐个查找，找到一个次数+1，数字与目标不匹配则结束
def search(nums, target):

    start = time.time()
    count = 0

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = nums[mid]

        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
        else:
            count = count + 1

            low_limit = mid
            while low_limit > 0:
                low_limit = low_limit - 1
                low_target = nums[low_limit]
                if low_target == target:
                    count = count + 1
                else:
                    break
                
            high_limit = mid
            while high_limit < len(nums) - 1:
                high_limit = high_limit + 1
                high_target = nums[high_limit]
                if high_target == target:
                    count = count + 1
                else:
                    break
            break
    stop = time.time()
    print("My Answer-Running time: " + str(stop - start))
    return count

# 精选答案：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/
def search_suggested(nums, target):
    # 以后为基本思路的优化代码
    # 帮助找到边界点
    def helper(tar):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            guess = nums[mid]

            if guess <= tar:
                left = mid + 1
            else:
                right = mid - 1
        return left

    start = time.time()

    # target的左边界(包含target)可以理解为找target - 1的右边界
    # 此时则可以抽象为同一个函数
    # 最后的计数则直接为right - left即可
    count = helper(target) - helper(target - 1)
    stop = time.time()
    print("Suggested-Running time:" + str(stop - start))
    return count

    # 基本思路：
    # left = 0
    # right = len(nums) - 1
    # # 先寻找右边界(不包含target的)
    # while left <= right:
    #     mid = int((left + right) / 2)
    #     edge = nums[mid]
    #     # 为了寻找右边界，当edge=target的时候，也要对使左边界+1
    #     # 当循环条件结束达成后，右边界即为最后的left = mid+1（此时left>right）
    #     if edge <= target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # right_edge = left
    # # 寻找到右边界后，左边界则在[0,right]之间
    # # 在此之前，先判断有没有必要寻找左边界
    # # 先通过判断nums[right]是否等于target来判断最终的数组是否包含target
    # # 如果不等于，即不包含，则直接返回0，没有必要寻找左边界
    # if right >= 0 and nums[right] != target:
    #     return 0
    # left = 0
    # while left <= right:
    #     mid = int((left + right) / 2)
    #     edge = nums[mid]
    #     if edge < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    # left_edge = right
    # count = right_edge - left_edge + 1
    

nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10]
target = 7
print(str(search(nums, target)))
print(str(search_suggested(nums, target)))