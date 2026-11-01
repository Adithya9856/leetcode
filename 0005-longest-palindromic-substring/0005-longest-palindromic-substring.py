class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start=end=0

        for i in range(n):
            len1=self.expand(s,i,i)
            len2=self.expand(s,i,i+1)
            lenght=max(len1,len2)

            if lenght>(end-start):
                start=i-(lenght-1)//2
                end=i+lenght//2
        return s[start:end+1]
    def expand(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1

