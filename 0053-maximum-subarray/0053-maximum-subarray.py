class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=nums[0]
        csum=0
        for i in nums:
            csum+=i
            maxsum=max(csum,maxsum)
            if csum<0:
                csum=0
        return maxsum