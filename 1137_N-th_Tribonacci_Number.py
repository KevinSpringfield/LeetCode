'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''


# Bottom up DP
# Time O(n)
# Space O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        
        if n < 3:
            return dp[n]
        
        for i in range(3, n + 1):
            cur = dp[0] + dp[1] + dp[2]
            dp = [dp[1], dp[2], cur]
            
        return dp[2]
        
