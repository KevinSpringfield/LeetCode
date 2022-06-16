'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
'''

# Brutal force method
class Solution:
    def count_one(self, number: int) -> int:
        ones = 0
        while number > 0:
            number, remain = divmod(number, 2)
            
            if remain == 1:
                ones += 1
        return ones
        
    def countBits(self, n: int) -> List[int]:
        return [self.count_one(m) for m in range(n + 1)]
