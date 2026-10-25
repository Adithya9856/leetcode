class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq={}
        for num in range(len(nums)):
            if target-nums[num] in freq:
                return [freq[target-nums[num]],num]
            freq[nums[num]]=num
