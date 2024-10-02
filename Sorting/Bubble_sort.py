#GFG

class Solution: 

    
    def selectionSort(self, arr,n):
        #code here
        #1) Take the minimum of across the array and swap it with the 0th idnex
        #2) Move to the 1st index, find the minimum from 1st to end of array 
        #   and swap it with the second index
        #3) Repat them until the array last befor element,last element is alreadys orted in this fashion
        for i in range(n-1,0-1,-1):
            didSwap = 0
            for j in range(0,i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    didSwap = 1
            if didSwap == 0:
                return arr   
        return arr
                    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
