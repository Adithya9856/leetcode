class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=0
        for num in nums:
            total+=num
        left_sum=0
        for num in range(len(nums)):
            right_sum=total-left_sum-nums[num]
            if left_sum==right_sum:
                return num
            left_sum+=nums[num]
        return -1