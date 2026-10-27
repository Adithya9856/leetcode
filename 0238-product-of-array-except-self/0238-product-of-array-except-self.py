class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        ans[0]=1
        for i in range(1,n):
            ans[i]=ans[i-1]*nums[i-1]
        right_prod=1
        for i in range(n-1,-1,-1):
            ans[i]*=right_prod
            right_prod*=nums[i]
        return ans