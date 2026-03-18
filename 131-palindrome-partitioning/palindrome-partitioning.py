class Solution:
    def func(self,idx,s,path,res):
        if(idx==len(s)):
            res.append(path[:])
            return
        for i in range(idx,len(s)):
            r=s[idx:i+1]
            if(r==r[::-1]):
                path.append(r)
                self.func(i+1,s,path,res)
                path.pop()    
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        self.func(0,s,path,res)
        return res
        