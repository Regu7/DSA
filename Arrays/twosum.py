class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        ''' when we want to return, only if sum exists'''
        # nums.sort()
        # i = 0
        # j = len(nums)-1
        # while(i<j):
        #     summ = nums[i] + nums[j]
        #     if summ ==  target:
        #         return 'Yes'
        #     elif summ < target:
        #         i+=1
        #     else:
        #         j-=1
        hashh = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashh:
                return [i,hashh[diff]]
            else:
                hashh[nums[i]] = i

            



        
