class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            elif ch=="}":
                if not stack:
                    return False
                top=stack.pop()
                if top!="{":
                    return False
            elif ch=="]":
                if not stack:
                    return False
                top=stack.pop()
                if top!="[":
                    return False
            else:
                if not stack:
                    return False
                top=stack.pop()
                if top!="(":
                    return False

        return (len(stack)==0)