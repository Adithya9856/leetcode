class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        sum=0
        lenght=float('inf')
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                lenght=min(lenght,right-left+1)
                sum-=nums[left]
                left+=1
        return lenght if lenght!=float('inf') else 0