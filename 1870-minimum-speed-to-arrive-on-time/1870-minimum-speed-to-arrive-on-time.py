class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        low,high=1,10**7
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if self.canarrive(dist,hour,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def canarrive(self,dist,hour,speed):
        time=0
        for i in range(len(dist)-1):
            time+=(dist[i]+speed-1)//speed
        time+=(dist[-1])/speed
        return time<=hour
  