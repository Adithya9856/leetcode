class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low,high=max(weights),sum(weights)
        ans=high
        while low<=high:
            mid=low+(high-low)//2
            if self.can_ship(weights,days,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def can_ship(self,weights,days,cap):
        d=1
        curr=0
        for weight in weights:
            if (curr+weight>cap):
                d+=1
                curr=weight
            else:
                curr+=weight
        return d<=days