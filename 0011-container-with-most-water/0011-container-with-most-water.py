class Solution:
    def maxArea(self, height: list[int]) -> int:
        most_water=float("-inf")
        n=len(height)
        left,right=0,n-1
        while left<right:
            lenght=min(height[left],height[right])
            width=right-left
            area=lenght*width
            most_water=max(area,most_water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return most_water