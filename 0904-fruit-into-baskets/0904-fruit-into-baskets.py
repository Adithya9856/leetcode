class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        my_list={}
        left=0
        lenght=0
        for right in range(len(fruits)):
            my_list[fruits[right]]=my_list.get(fruits[right],0)+1
            if len(my_list)>2:
                my_list[fruits[left]]-=1
                if my_list[fruits[left]]==0:
                    del my_list[fruits[left]]
                left+=1
            if len(my_list)<=2:
                lenght=max(lenght,right-left+1)
        return lenght