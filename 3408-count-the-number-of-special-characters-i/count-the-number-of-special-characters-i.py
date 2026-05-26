class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small=[0]*26
        capital=[0]*26
        count=0
        for i in word:
            if i>='a' and i<='z':
                small[ord(i)-ord('a')]=1
            if i>='A' and i<='Z':
                capital[ord(i)-ord('A')]=1
        for i in range(26):
            if(small[i])==1 and capital[i]==1:
                count+=1
        return count                                       

        