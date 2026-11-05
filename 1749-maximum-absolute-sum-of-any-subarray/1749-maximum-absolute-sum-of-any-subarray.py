class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        cur_pos=cur_neg=0
        pos_sum=neg_sum=nums[0]
        for num in nums:
            cur_pos+=num
            pos_sum=max(pos_sum,cur_pos)
            if cur_pos<0:
                cur_pos=0
            cur_neg+=num
            neg_sum=min(neg_sum,cur_neg)
            if cur_neg>0:
                cur_neg=0
        return max(pos_sum,abs(neg_sum))