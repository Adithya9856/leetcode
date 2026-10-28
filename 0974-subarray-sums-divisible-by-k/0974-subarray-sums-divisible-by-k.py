class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        freq={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            rem=prefix_sum%k
            count+=freq.get(rem,0)
            freq[rem]=freq.get(rem,0)+1
        return count