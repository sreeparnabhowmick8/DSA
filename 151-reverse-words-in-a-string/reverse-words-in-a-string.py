class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        i,n=0,len(l)-1
        while(i<n):
            l[i],l[n]=l[n],l[i]
            i+=1
            n-=1
        return " ".join(l)    
         
        
        