class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        n=len(arr)
        prefix_sum=0
        max_length=0
        prefix_map={}
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum==k:
                max_length=i+1
            if(prefix_sum-k) in prefix_map:
                max_length=max(max_length,i-prefix_map[prefix_sum-k])
            
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum]=i
        return max_length
