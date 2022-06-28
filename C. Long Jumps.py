def read_int():
    return int(input())
def read_ints():
    return map(int, input().split(' '))

t = read_int()
for _ in range(t):
    n = read_int()
    a = list(read_ints())
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        dp[i] = (0 if i + a[i] >= n else dp[i + a[i]]) + a[i]
    print(max(dp))