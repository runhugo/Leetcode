# 剑指offer 35 ii
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# input: [0,1,3], output: 2
# input: [0,1,2,3,4,5,6,7,9], output: 8


# 我的思路：通过二分，查看mid对应的元素，然后通过+1/-1来与mid下一个/上一个元素进行比较，
# 如果相等，表示这几个数字连续，则不连续数字是在[left, mid-1]和[mid+1, right]之间
# 以此类推，通过不断划分区间，并对这些区间进行二分查询，找到缺失数字
## 但是该方法不可行，1是没有想明白跳出循环点的条件，2是问题复杂化，需要左右两边要分别查询。此外如果数组很大，而缺失数字由在极端位置，使得复杂度增加


# 推荐思路：因为是递增有序数组，且数字都是唯一，则如果没有期间数字缺失的话，数组索引与索引对应的值应该是相等的（因为值也是从0开始）-->即num[i]=i
# 则可以把数组分为左右两个部分（以缺失数字为分界），即寻找左数组的末尾索引和右数组的首位索引。
# 而缺失数字则对应右数组的首位索引（即第一个num[i]!=i）。所以
# 循环：left<=right（left = 0, right = len - 1）
# 寻找中点：mid = left + right // 2 --> int((left + right) / 2)
# if num[mid] == mid，则右数组的首位一定在[mid + 1, right]之中
# if num[mid] != mid，则左数组的末位一定在[left, mid - 1]之中（即右数组首位在[left, mid]之间--可能mid刚好就是右数组首位）
def missingNumber(nums):

    left = 0
    right = len(nums) - 1

    while left <= right:
        # mid = (left + right) // 2
        # 当left和right都是极端大的数时，直接相加可能会导致溢出（python可能不存在这样的问题，但是java和c都有可能会）
        # 所有先做减法（right - left）可以有效避免变量溢出
        mid = left + (right - left) // 2 
        guess = nums[mid]

        if guess == mid:
            left = mid + 1
        else:
            right = mid - 1
        
    return left

nums = [0,1,3,4,5,6,7,8,9]
print(missingNumber(nums))