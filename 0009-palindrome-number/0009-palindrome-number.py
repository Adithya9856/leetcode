class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        if temp<0:
            return False
        while temp!=0:
            rem=temp%10
            rev=rev*10+rem
            temp//=10
        if rev<-2**31 or rev>2**32-1:
            return False
        if rev==x:
            return True
        return False