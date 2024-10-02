#gfg

#User function Template for python3

class Solution:
    def merge(self,arr, low, mid, high):
        left = low
        right = mid+1
        temp = []
        while(left<=mid and right<= high):
            if arr[left] <= arr[right]: 
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        while(right<=high):
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i] = temp[i-low]
            
            
        # code here
    def mergeSort(self,arr, low, high):
        if low>=high:
            return
        mid = (low+high)//2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends

