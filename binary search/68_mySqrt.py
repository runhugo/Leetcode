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
# 牛顿法的介绍：https://www.matongxue.com/madocs/205/
# 
# 基本思路：求x的平方根，其实就是求函数f(x)=x^2-a等于0时的正解
# 通过牛顿法，可算得迭代式：x(n+1) = (x(n)^2 + a) / (2*x(n))
# 迭代停止条件：
# 我的思路（可行吗？代码上可行）：每次算得x(n+1)，带回f(x)中，当收敛于0时，则可以视为是x的平方根 (我的思路。。这个可行吗？)
# 网站思路：当两次的迭代点足够近时，则认为收敛，找到解
def mySqrt_newton(x):
    if x < 0:
        return -1
    
    if x == 0:
        return 0
    
    x1 = x
    while True:
        x0 = x1
        x1 = 0.5 * (pow(x1, 2) + x) / x1
        # 我的思路可实现
        # x_hat = pow(x1, 2) - x
        # if abs(x_hat) < 1e-7:
        #     return x1
        
        # 网站思路
        if abs(x1 - x0) < 1e-7:
            return x1    


print(str(mySqrt(8)))
print(str((mySqrt_newton(8))))
print(3%6)

