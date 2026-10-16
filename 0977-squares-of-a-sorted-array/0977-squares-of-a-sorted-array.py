class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            nums[left]=nums[left]**2
            left+=1
        nums.sort()
        return nums
