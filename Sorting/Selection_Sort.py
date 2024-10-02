#Geeksforgeeks
#User function Template for python3

class Solution: 

    
    def selectionSort(self, arr,n):
        #code here
        #1) Take the minimum of across the array and swap it with the 0th idnex
        #2) Move to the 1st index, find the minimum from 1st to end of array 
        #   and swap it with the second index
        #3) Repat them until the array last befor element,last element is alreadys orted in this fashion
        for i in range(n-1):
            mini = i
            for j in range(i,n):
                if arr[j] < arr[mini]:
                    mini = j
            temp = arr[mini]
            arr[mini] = arr[i]
            arr[i] = temp
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
