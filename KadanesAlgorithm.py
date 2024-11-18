class Solution(object):
    def maxSubArray(self, nums):
        current_sum=0
        max_sum=nums[0]
        for num in nums:
            current_sum += num
            max_sum=max(current_sum,max_sum)
            if current_sum<0:
                current_sum=0
        return max_sum
