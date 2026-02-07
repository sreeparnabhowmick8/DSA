class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        r=[]
        for i in range(len(l)-1,-1,-1):
           r.append(l[i])
        return " ".join(r)
         
        
        