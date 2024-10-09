#leetcode 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        n = len(nums)
        sum1 = (n*(n+1))/2
        sum2 =0
        for i in range(n):
            sum2 += nums[i] 
        return int(sum1 - sum2)
        '''
        XOR1,XOR2 = 0, 0
        for i in range(len(nums)):
            XOR1 = XOR1 ^ nums[i]
            XOR2 = XOR2 ^ (i+1)
        return XOR1 ^ XOR2

        
