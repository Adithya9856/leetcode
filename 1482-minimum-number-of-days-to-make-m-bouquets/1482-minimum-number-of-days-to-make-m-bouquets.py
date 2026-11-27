class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        low,high=min(bloomDay),max(bloomDay)
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if self.canmake(bloomDay,m,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def canmake(self,bloomDay,m,k,day):
        bouq=0
        count=0
        for bloom in bloomDay:
            if bloom<=day:
                count+=1
                if count==k:
                    bouq+=1
                    count=0
            else:
                count=0
        return bouq>=m