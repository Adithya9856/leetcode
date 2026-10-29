class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=csum=nums[0]
        for i in nums[1:]:
            csum=max(i,csum+i)
            maxsum=max(maxsum,csum)
        return maxsum