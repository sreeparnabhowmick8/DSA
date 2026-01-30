class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic={}
        rev = {}
        words=s.split()
        if(len(pattern)!=len(words)):
            return False
        for i in range(len(words)):
            if pattern[i] in dic and (dic[pattern[i]]!=words[i]):
                return False
            if words[i] in rev and rev[words[i]] != pattern[i]:
                return False    
            dic[pattern[i]]=words[i]
            rev[words[i]] = pattern[i]
        return True    



        