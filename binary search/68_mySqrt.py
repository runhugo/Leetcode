# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 基本思路：
# 因为平方根之后的数一定在[0,x]之间（nums=[0,x]），通过二分
# 查看mid点的数的平方是否等于x
#（1）num[mid]*num[mid] = x，则返回num[mid]
#（2）num[mid]*num[mid] < x，则得数在[num[mid+1]，x]之间
#（3）num[mid]*num[mid] > x，则得数在[0，num[mid-1]]之间
# 最后结束时，right所指即x开方后的取整值
def mySqrt(x:int):
    if(x < 0):
        return -1
    
    left = 0
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        sq = mid * mid

        if sq == x:
            return mid

        if sq < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# 还可以用牛顿法
# todo


print(str(mySqrt(9)))

