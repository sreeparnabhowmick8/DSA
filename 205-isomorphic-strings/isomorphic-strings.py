class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        j=0
        s.split()
        t.split()
        if(len(s)!=len(t)):
            return False
        for i in s:
            if t[j] in dic.values():
                if i not in dic:
                    return False
            if i in dic:
                if(dic[i]!=t[j]):
                    return False
            dic[i]=t[j]
            j+=1
        return True                
        