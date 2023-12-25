#!D:/Application/python/python.exe
# 青蛙跳台阶

def frog_jump(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # 使用动态规划思想，记录每一级台阶的跳法数量
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# 测试
n = 5
result = frog_jump(n)
print(f"青蛙跳上 {n} 级台阶的跳法有 {result} 种")


# 添加递归法
def frog_jump_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return frog_jump_recursive(n - 1) + frog_jump_recursive(n - 2)

# 测试
n = 4
result = frog_jump_recursive(n)
print(f"青蛙跳上 {n} 级台阶的跳法有 {result} 种")