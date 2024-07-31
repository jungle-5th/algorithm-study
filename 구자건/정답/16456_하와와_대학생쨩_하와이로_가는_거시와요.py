from sys import stdin
input = stdin.readline

def hawawawa(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    
    end_dp = [0 for i in range(number)]
    dp = [0 for i in range(number)]
    end_dp[0], end_dp[1] = 1, 1
    dp[0], dp[1] = 1, 1
    
    for i in range(2, number):
        end_dp[i] = dp[i-1]
        dp[i] = end_dp[i] + end_dp[i-2]
        
    return dp[number-1] % 1000000009

number = int(input())
print(hawawawa(number))
