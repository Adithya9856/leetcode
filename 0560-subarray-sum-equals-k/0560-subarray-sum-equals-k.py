class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        pre_sum=0
        freq={0:1}
        for num in nums:
            pre_sum+=num
            count+=freq.get(pre_sum-k,0)
            if pre_sum in freq:
                freq[pre_sum]+=1
            else:
                freq[pre_sum]=1
        return count