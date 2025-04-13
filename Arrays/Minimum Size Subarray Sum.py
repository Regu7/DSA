#leetcode 209. Minimum Size Subarray Sum


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        total = 0
        for r in range(0,len(nums)):
            total += nums[r] 
            while total >=target and l<=r:
                res = min(res,r-l+1)
                total -= nums[l]
                l+=1
        if res != float('inf'):
            return res
        else:
            return 0
