class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        stack=[]
        if(s==goal):
            return True
       
        n=len(s)
        for i in range(n):
            stack[:]=s[i+1:]+s[:i+1]
            temp=''.join(stack)
            if(temp==goal):
                return True
        return False        


        