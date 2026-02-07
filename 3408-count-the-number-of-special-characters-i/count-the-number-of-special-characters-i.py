class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small=[0]*26
        capital=[0]*26
        count=0
        for i in word:
            if i>='a' and i<='z':
                small[ord(i)-ord('a')]=1 #small=[1,1,1,...]
            else:
                capital[ord(i)-ord('A')]=1 #capital=[1,1,1,...]
        for i in range(26):
            if(small[i]==1 and capital[i]==1):
                count+=1 
        return count                   

        