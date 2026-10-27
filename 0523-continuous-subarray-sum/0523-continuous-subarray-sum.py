class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        rem={0:-1}
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            remainder=prefix_sum%k
            if remainder in rem:
                if i-rem[remainder] >=2:
                    return True
            else:
                rem[remainder]=i
        return False