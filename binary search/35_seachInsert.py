# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。

# Example: 
# input: [1,3,5,6], 5; output: 2
# input: [1,3,5,6], 2; output: 1

# 基本思路：（排序数组寻找目标值，用二分查找）
#
# 当num[mid] == target时，直接返回mid
# 当num[mid] < target, 证明target在右半边
# 当num[mid] > target，证明在左半边
# 如果最后没有找到，left最终指向的位置则是插入的位置，因为：
# 最后找不到时必定会有left==right==mid的情况，此时（在元素不重复时），target只会插在这个元素的左边或右边
# （1）若num[mid] < target，则target应该插在右边，根据上述条件，left=mid+1
# （2）若num[mid] > target，则target应该插在这个元素左边，此时right=mid-1，left不变（相当于元素插入到当前位置，现在的值往后移）
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        guess = nums[mid]

        if guess == target:
            return mid

        if guess < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = [1,5,6,9]
target = 8

print(str(searchInsert(nums, target)))