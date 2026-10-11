class Solution:
    def reverse(self, x: int) -> int:
        temp=abs(x)
        reverse=0
        while temp!=0:
            remainder=temp%10
            reverse=reverse*10+remainder
            temp//=10
        if x<0:
            reverse=-reverse
        if reverse < -2**31 or reverse > 2**31-1:
            return 0
        return reverse          