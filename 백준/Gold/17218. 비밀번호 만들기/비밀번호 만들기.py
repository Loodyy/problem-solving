S, T = input(), input()
dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
ans = [[""] * (len(T) + 1) for _ in range(len(S) + 1)]
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            ans[i + 1][j + 1] = ans[i][j] + S[i]
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            ans[i + 1][j + 1] = max(ans[i + 1][j], ans[i][j + 1], key=lambda x: len(x))
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(ans[-1][-1])