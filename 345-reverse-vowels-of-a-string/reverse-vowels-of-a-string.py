class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l,r=0,len(s)-1
        while(l<r):
            if s[l] in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
                l+=1
                r-=1
            elif s[l] in "aeiouAEIOU" and s[r] not in "aeiouAEIOU":
                r-=1
            else:
                l+=1
        return "".join(s)                

        