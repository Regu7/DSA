class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's algo
        maxi = nums[0]
        summ = 0
        for num in nums:
            summ += num
            maxi = max(summ,maxi)
            if summ <  0:
                summ = 0
        return maxi
