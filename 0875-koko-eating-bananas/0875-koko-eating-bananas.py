class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low,high=1,max(piles)
        ans=high
        while low<=high:
            mid=low+(high-low)//2
            if self.caneat(piles,h,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def caneat(self,piles,h,k):
        hours=0
        for pile in piles:
            hours+=(pile+k-1)//k
        return hours<=h