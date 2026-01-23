class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst=[char for char in s]
        start,end= 0,len(s)-1
        while start<end:
            if lst[start].isalpha() and lst[end].isalpha():
                lst[start],lst[end]= lst[end],lst[start]
                start+=1
                end-=1
            else:
                if (not lst[start].isalpha()):
                    start+=1
                elif (not lst[end].isalpha()):
                    end-=1
                else:
                    start+=1
                    end-=1
        return ''.join(lst)
        