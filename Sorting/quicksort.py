#gfg

class Solution:
    def swap(self,arr,idx1,idx2):
        temp = arr[idx1]
        arr[idx1] =  arr[idx2]
        arr[idx2] =  temp

    def partition(self,arr,low,high):
        i = low
        j = high
        pivot = arr[i]
        while(i<j):
            while(i<=high-1 and arr[i] <= pivot):
                i+=1
            while(j>=low+1 and arr[j]>pivot):
                j-=1
            if i < j : self.swap(arr,i,j)
        self.swap(arr,low,j)
        return j
    
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low<high:
            partition_index = self.partition(arr,low,high)
            self.quickSort(arr,low,partition_index-1)
            self.quickSort(arr,partition_index+1,high)
        
        
    
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
