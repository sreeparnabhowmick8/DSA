class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        res=[]
        for i in s:
            if i in "aeiouAEIOU":
                vowels.append(i)
        for i in s:
            if i not in "aeiouAEIOU":
                res.append(i)
            else:
                res.append(vowels.pop())
        return "".join(res)                    
        