class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total=cur_min=cur_max=0
        max_sum=min_sum=nums[0]
        for num in nums:
            total+=num
            cur_max+=num
            max_sum=max(max_sum,cur_max)
            if cur_max<0:
                cur_max=0
            cur_min+=num
            min_sum=min(cur_min,min_sum)
            if cur_min>0:
                cur_min=0
        if max_sum<0:
            return max_sum
        return max(max_sum,total-min_sum)