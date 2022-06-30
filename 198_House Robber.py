'''
You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, 

the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Example 3:

Input: nums = [1,2,3]
Output: 3

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

'''
解題思路:

1. 先觀察 example 1: 如果搶了 index = 0 之後，能搶的就是剩下的 [3, 1]，那如果不搶 index = 0 的話剩下能搶的就是 [2, 3 ,1]
2. 決定要不要搶 1 可以看搶 [3, 1] 和 [2, 3, 1] 哪一邊的價值最高
3. 畫出 decision tree:

          [1, 2, 3, 1]
         / 搶 1      \ 不搶 1
     [3, 1]        [2, 3, 1]
     /    \       / 搶2     \ 不搶 2
    []    []    [1]        [3, 1]    
                 |         /    \
                []        []    []
                
4. 劃出來後可以觀察到每做完一次選擇，問題就會變成重複的，只是 array 內的元素減少了，決定用 DP
5. 因為考慮上層需要先知道下層的解決才能做決定，所以 DP 要從後面往回建構:
    意思是需要先從 1 -> 3 -> 2 -> 1 這個方向把 DP 填回來    
6. DP 內的 index 和 value 分別表示考慮從第 index 個元素開始的 sub list (nums[index:]) 以及最大價值
               
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * (len(nums) - 1) + [nums[-1]] 
        
        for i in range(len(nums) - 2, -1, -1):
            if i == len(nums) - 2:
                value = max(nums[i], nums[i+1])
            else:
                value = max(dp[i+1], dp[i+2] + nums[i])
            dp[i] = value
            
        return dp[0]
            
