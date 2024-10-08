#leetcode 26. Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 0
        for j in range(len(arr)):
            if arr[j] != arr[i]:
                arr[i+1] = arr[j]
                i+=1
        return i+1

            
        
