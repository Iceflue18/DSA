class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)+1
        actual_sum=0
        for i in range(0,n-1):
            actual_sum += nums[i]
        expected_sum=n*(n-1)//2
        num=expected_sum-actual_sum
        return  num
        
