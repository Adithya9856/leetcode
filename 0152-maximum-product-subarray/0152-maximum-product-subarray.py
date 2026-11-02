class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        left=1
        right=1
        maxp=float('-inf')
        for i in range(len(nums)):
            if left==0:
                left=1
            if right==0:
                right=1
            left*=nums[i]
            right*=nums[len(nums)-1-i]
            maxp=max(maxp,left,right)
        return maxp