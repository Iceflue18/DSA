class Solution:
    def searchInSorted(self,arr, k):
        n=len(arr)
        for i in range(0,n):
            if arr[i]==k:
                return True
        return False
