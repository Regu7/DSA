class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moores voting algorithm
        n = len(nums)
        cnt = 0
        for i in range(n):
            if cnt == 0:
                cnt=1
                ele = nums[i]
            elif nums[i] == ele:
                cnt+=1
            else:
                cnt-=1
        return ele
            
            
            


        ''' Brute Force
        if n < 1 :
            return
        hashh = {}
        for i in range(n):
            if nums[i] in hashh.keys():
                hashh[nums[i]] += 1
            else:
                hashh[nums[i]] = 1
        maxi = max(hashh.values())
        for key,val in hashh.items():
            if val == maxi:
                return key
        '''

        
